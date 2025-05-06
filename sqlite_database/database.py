from pathlib import Path
import sqlite3
import jaxtyping as jt
from dataclasses import dataclass
import equinox as eqx
from typing import Sequence

import os
from jax import numpy as jnp, random as jrand
from typing import Union, Literal, List
import numpy as np
import glob


# These are placeholders to represent more reasonable objects
################################################################


class Dataset(eqx.Module):
    train_data: jt.Array
    test_data: jt.Array


def make_dataset(ds_param_1: int, ds_param_2: int):
    return Dataset(
        train_data=jnp.ones(ds_param_1, ds_param_1),
        test_data=jnp.ones(ds_param_2, ds_param_2),
    )


class VAE(eqx.Module):
    params: Sequence[int]
    weights: jt.Array

    def __init__(self, vae_param_1: int, vae_param_2: int):
        self.params = (vae_param_1, vae_param_2)
        self.weights = jrand.uniform(jrand.key(0), [vae_param_1, vae_param_2])


class DDPM(eqx.Module):
    params: Sequence[int]
    weights: jt.Array

    def __init__(self, ddpm_param_1: int, ddpm_param_2: int):
        self.vae_params = (ddpm_param_1, ddpm_param_2)
        self.weights = jrand.uniform(jrand.key(0), [ddpm_param_1, ddpm_param_2])


################################################################


class Database:
    """
    This will contain the following tables:

    datasets (id, ds_param_1, ds_param_2)
    vae (id, vae_param_1, vae_param_2, ds_id, [checkpoint_id])
    ddpm (id, ddpm_param_1, ddpm_param_2, ds_id, vae_id, [checkpoint_id])


    When we have multiple returns from a read query, it is assumed that the most recent row is the one that is wanted
    e.g. multiple training sessions on the same model, with the most recent being the latest trained model. Thus,
    if a query is underdetermined (returning multiple things), we return the last row.

    We store the parameters of the models and dataset, as well as an id number to represent both recency and the file
    name on the hard drive. For the models, we also store the ids of the objects used in their training, so the dataset
    and, if applicable, the VAE used to generate the latents they were trained on.

    Finally, we store checkpoint ids to keep track of which models are fine-tunings of other ones. In practice, when saving
    the model, if it was a continuation of training an earlier model, you would include that ID in the saving procedure.
    """

    def __init__(self):
        self.file_location = Path(__file__).resolve().parent

        self.connection = sqlite3.connect(self.file_location / "database.db")
        self.cursor = self.connection.cursor()

        self.make_tables()

        create_directory_if_not_exists(self.file_location / "datasets")
        create_directory_if_not_exists(self.file_location / "vaes")
        create_directory_if_not_exists(self.file_location / "ddpms")

    def make_tables(self):
        """
        Put any tables you want to generate (and their attributes) here. Reference the documentation
        for a list of other valid types. Note that below, all arguments are required to not be null
        except for the checkpoint_id, since that isn't always applicable.
        """

        create_datasets_table = """
        CREATE TABLE IF NOT EXISTS datasets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            dataset_param_1 INTEGER NOT NULL,
            datset_param_2 INTEGER NOT NULL
        );
        """

        create_vae_table = """
        CREATE TABLE IF NOT EXISTS vae (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            vae_param_1 INTEGER NOT NULL,
            vae_param_2 INTEGER NOT NULL,
            ds_id INTEGER NOT NULL
            checkpoint_id INTEGER
        );
        """

        create_ddpm_table = """
        CREATE TABLE IF NOT EXISTS ddpm (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ddpm_param_1 INTEGER NOT NULL,
            ddpm_param_2 INTEGER NOT NULL,
            ds_id INTEGER NOT NULL,
            vae_id INTEGER NOT NULL,
            checkpoint_id INTEGER,
        );
        """

        self.execute_write(create_datasets_table)
        self.execute_write(create_vae_table)
        self.execute_write(create_ddpm_table)

    def execute_write(self, query, parameters=None):
        """
        Run write/insert commands and return the corresponding row id.
        """

        if parameters is None:
            res = self.cursor.execute(query)

        else:
            res = self.cursor.execute(query, parameters)

        self.connection.commit()
        return res.lastrowid

    def execute_read(self, query, parameters=None):
        """
        Run read commands and return all valid rows.
        """
        if parameters is None:
            res = self.cursor.execute(query)

        else:
            res = self.cursor.execute(query, parameters)

        self.connection.commit()
        return res.fetchall()

    def delete_entry(
        self,
        id: int | Literal["*"],
        table: Union[Literal["datasets"], Literal["vae"], Literal["ddpm"]],
    ):
        """
        Delete row id in given table. If id="*", remove all entries in that list.
        """
        user_input = input(
            "ARE YOU ABSOLUTELY SURE? ENTER 'I AM SUPER SURE' IF YOU ARE."
        )
        if user_input != "I AM SUPER SURE":
            print("Cancelling")
            return None

        del_string = (
            f"DELETE FROM {table}{"where id = " + str(id) if id != "*" else str()}"
        )
        self.execute_write(del_string)

        match table:
            case "datasets":
                file_name = self.file_location / f"datasets/ds_{id}.eqx"
            case "vae":
                file_name = self.file_location / f"vaes/vae_{id}.eqx"
            case "ddpm":
                file_name = self.file_location / f"ddpms/ddpm_{id}.eqx"

        for f in glob.glob(str(file_name)):
            os.remove(f)

    def clear_database(self):
        """
        Clear all tables and reset completely.
        """

        user_input = input(
            "ARE YOU ABSOLUTELY SURE? ENTER 'I AM SUPER SURE' IF YOU ARE."
        )
        if user_input != "I AM SUPER SURE":
            print("Cancelling")
            return None

        self.execute_write("DROP TABLE datasets")
        self.execute_write("DROP TABLE vae")
        self.execute_write("DROP TABLE ddpm")

        for file_name in [
            self.file_location / "datasets/ds_*.eqx",
            self.file_location / "vaes/vae_*.eqx",
            self.file_location / "ddpms/ddpm_*.eqx",
        ]:
            for f in glob.glob(str(file_name)):
                os.remove(f)

        self.make_tables()

    def save_dataset(self, dataset: Dataset, ds_param_1: int, ds_param_2: int):
        write_query = f"""
        INSERT INTO
            datasets (ds_param_1, ds_param_2)
        VALUES
            ({ds_param_1}, {ds_param_2})
        """

        id = self.execute_write(write_query)

        eqx.tree_serialise_leaves(self.file_location / f"datasets/ds_{id}.eqx", dataset)

    def _deserialize_dataset(self, id, ds_param_1, ds_param_2):

        blank_dataset = make_dataset(ds_param_1, ds_param_2)

        dataset = eqx.tree_deserialise_leaves(
            self.file_location / f"datasets/ds_{id}.eqx", blank_dataset
        )
        return dataset, id

    def load_dataset(self, ds_param_1: int, ds_param_2: int):
        """
        Load most recent dataset corresponding to the given parameters
        """
        read_query = f"""
SELECT 
    id
FROM
    datasets
WHERE
    datasets.ds_param_1 = {ds_param_1} AND
    datasets.ds_param_2 = {ds_param_2}
"""

        row = self.execute_read(read_query)[-1]
        id = row[0]

        return self._deserialize_dataset(id, ds_param_1, ds_param_2)

    def load_dataset_by_id(
        self,
        id: int,
    ):
        """
        Load dataset with given ID
        """

        read_query = f"""
        SELECT 
            ds_param_1, ds_param_2
        FROM
            datasets
        WHERE
            datasets.id = {id}
        """
        row = self.execute_read(read_query)[-1]
        ds_param_1, ds_param_2 = row
        return self._deserialize_dataset(id, ds_param_1, ds_param_2)

    def save_vae(
        self,
        model: VAE,
        dataset_id: int,
        checkpoint_id: int | Literal["NULL"] | None = None,
    ):
        """
        Save VAE. The unpacking at the front could be done more automatically, I just want to be verbose for explanation purposes.
        """
        vae_param_1 = model.params["vae_param_1"]
        vae_param_2 = model.params["vae_param_2"]

        checkpoint_id = "NULL" if checkpoint_id is None else checkpoint_id
        write_query = f"""
        INSERT INTO
            vae (vae_param_1, vae_param_2, dataset_id, checkpoint_id)
        VALUES
            ({vae_param_1}, {vae_param_2}, {dataset_id}, {checkpoint_id})
        """

        id = self.execute_write(write_query)

        eqx.tree_serialise_leaves(self.file_location / f"vaes/vae_{id}.eqx", model)

    def _deserialize_vae(
        self,
        id: int,
        vae_param_1: int,
        vae_param_2: int,
    ):
        blank_model = VAE(vae_param_1, vae_param_2)

        model = eqx.tree_deserialise_leaves(
            self.file_location / f"vaes/vae_{id}.eqx", blank_model
        )
        return model

    def load_vae(
        self,
        vae_param_1: int,
        vae_param_2: int,
        dataset_id: int | None = None,
        checkpoint_id: int | None = None,
    ):
        """
        Load most recent VAE corresponding to the given parameters
        """
        read_query = f"""
        SELECT 
            id, dataset_id, checkpoint_id
        FROM
            vae
        WHERE
            vae.vae_param_1 = {vae_param_1} AND
            vae.vae_param_2 = {vae_param_2} 
            {f"AND \n \t vae.dataset_id = {dataset_id}" if dataset_id is not None else str()} 
            {f"AND \n \t vae.checkpoint_id = {checkpoint_id}" if checkpoint_id is not None else str()}
        """

        row = self.execute_read(read_query)[-1]
        id, dataset_id, checkpoint_id = row
        return (
            self._deserialize_vae(id, vae_param_1, vae_param_2),
            id,
            dataset_id,
            checkpoint_id,
        )

    def load_vae_by_id(
        self,
        id: int,
    ):
        """
        Load VAE with given ID
        """
        read_query = f"""
SELECT 
    vae_param_1, vae_param_2, dataset_id, checkpoint_id
FROM
    vae
WHERE
    vae.id = {id}
"""

        row = self.execute_read(read_query)[-1]
        vae_param_1, vae_param_2, dataset_id, checkpoint_id = row
        return (
            self._deserialize_vae(
                id,
                vae_param_1,
                vae_param_2,
                dataset_id,
                checkpoint_id,
            ),
            id,
            dataset_id,
            checkpoint_id,
        )

    def save_ddpm(
        self,
        model: DDPM,
        T: int,
        vae_id: int,
        dataset_id: int,
        checkpoint_id: int | Literal["NULL"] | None = None,
    ):
        """
        Save DDPM, along with the T used for sampling
        """
        ddpm_param_1 = model.params["ddpm_param_1"]
        ddpm_param_2 = model.params["ddpm_param_2"]

        checkpoint_id = "NULL" if checkpoint_id is None else checkpoint_id
        write_query = f"""
        INSERT INTO
            ddpm (ddpm_param_1, ddpm_param_2, ds_id, vae_id, checkpoint_id)
        VALUES
            ({ddpm_param_1}, {ddpm_param_2}, {dataset_id}, {vae_id}, {checkpoint_id})
        """

        id = self.execute_write(write_query)

        eqx.tree_serialise_leaves(
            self.file_location / f"ddpms/ddpm_{id}.eqx", (model, T)
        )

    def _deserialize_ddpm(
        self,
        id: int,
        ddpm_param_1: int,
        ddpm_param_2: int,
    ):
        blank_model = DDPM(ddpm_param_1, ddpm_param_2)

        blank_T = 1

        model, T = eqx.tree_deserialise_leaves(
            self.file_location / f"ddpms/ddpm_{id}.eqx", (blank_model, blank_T)
        )
        return model, T

    def load_ddpm(
        self,
        ddpm_param_1: int,
        ddpm_param_2: int,
        vae_id: int | None = None,
        dataset_id: int | None = None,
        checkpoint_id: int | None = None,
    ):
        """
        Load most recent DDPM corresponding to the given parameters
        """

        read_query = f"""
        SELECT 
            id, vae_id, dataset_id, checkpoint_id
        FROM
            ddpm
        WHERE
            ddpm.ddpm_param_1 = {ddpm_param_1}
            ddpm.ddpm_param_2 = {ddpm_param_2}
            {f"AND \n \t vae.vae_id = {vae_id}" if vae_id is not None else str()} 
            {f"AND \n \t vae.dataset_id = {dataset_id}" if dataset_id is not None else str()} 
            {f"AND \n \t vae.checkpoint_id = {checkpoint_id}" if checkpoint_id is not None else str()}
        """

        row = self.execute_read(read_query)[-1]
        id, vae_id, dataset_id, checkpoint_id = row
        model, T = self._deserialize_ddpm(id, ddpm_param_1, ddpm_param_2)
        return (
            model,
            T,
            id,
            vae_id,
            dataset_id,
            checkpoint_id,
        )

    def load_ddpm_by_id(
        self,
        id: int,
    ):
        """
        Load DDPM with given id
        """
        read_query = f"""
        SELECT 
            ddpm_param_1, ddpm_param_2, vae_id, dataset_id, checkpoint_id
        FROM
            ddpm
        WHERE
            ddpm.id = {id} 
        """

        row = self.execute_read(read_query)[-1]
        ddpm_param_1, ddpm_param_2, vae_id, dataset_id, checkpoint_id = row
        model, T = self._deserialize_ddpm(id, ddpm_param_1, ddpm_param_2)

        return (
            model,
            T,
            id,
            vae_id,
            dataset_id,
            checkpoint_id,
        )


def create_directory_if_not_exists(dir_path):
    os.makedirs(dir_path, exist_ok=True)
