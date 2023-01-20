# Useful commands for Slurm-based clusters

Interrupt an interactive job on Windows:

```Ctr Z```

Interrupt an interactive job on Linux, MacOS:

```Ctr D```

Submit a .sh file (file is scheduled to run when resources are available):

```sbatch your_file.sh```

Sample header for a .sh file (different for each cluster and whether the job uses GPUs or CPUs): 

See ```{TTIC, LLNL, RCC}/sample_{cpu,gpu}.sh```

Copy a file from your local computer to the cluster (assumed to be executed in the local file's directory):

```scp local_file username@loginemail:path/to/destination/folder```

Copy a folder from your local computer to the cluster (assumed to be executed in the local folder's directory):

```scp local_folder username@loginemail:path/to/destination/folder```

Cancel a specific scheduled job:

```scancel <job#>```

Cancel all jobs associated with your account:

```scancel -u your_username```

# Conda

Create a conda environment:

```conda create -n my_env_name```

Create a conda environment with a specific Python version:

```conda create -n my_conda_env3.9 python=3.9```

Create a conda environment with a previous Python and Pytorch version: (More details at https://pytorch.org/get-started/previous-versions/)

Example: ```conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=10.2 -c pytorch```

## Keeping track of conda environments in env.yaml files

Often it's useful to make a list of all of the packages you've downloaded for your conda environment. This can allow you to save a file and set up an identical conda environment on a different computer. This command creates a conda environment file named `env.yaml`: 
```
conda env export --from-history > env.yaml
```
To set up a new conda environment using the file you've just created, use the command 
```
conda env create -f env.yaml
```

## Conda cheat sheet

This [cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf) has the answer to most conda questions.

# Setting up SSH 

Setting up SSH authentication keys is important for working with remote clusters. This is a good resource for setting up, transferring, and using your SSH authentication keys: [https://goteleport.com/blog/how-to-set-up-ssh-keys/](https://goteleport.com/blog/how-to-set-up-ssh-keys/)