##################################################################################################################
#                                  How to change this file for your own purposes                                 #
##################################################################################################################
#
# 1. Rename the temp_job_folder variable to a short descriptor of this job.
# 2. Replace the entries of parameter_names with the names of the variables you want to pass to the script (named
#    my_python_script.py here).
# 3. Edit the ts variable to contain a list of tuples. The tuple should contain information corresponding to
#    a specification of one .sh file. The first entry should be the title of the job, and the other entries should
#    be the arguments in parameter_names. The length of ts should correspond to the number of .sh files you would like
#    to submit jobs for.
# 4. Plug in the arguments to header with arguments for the cluster.
# 5. Comment out line 50 on your first run of this code to in order to check that the .sh files produced are correct.
#    It may also be good to run one .sh file produced to see if the desired results are produced w/o error.
##################################################################################################################

import os

from cluster_headers import header


# names a folder to be added in the current working directory named 'temp_job'
temp_job_folder = "temp_job"


# creates a folder in the current working directory named 'temp_job'
def mkdir_p(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)


mkdir_p(temp_job_folder)


# given input parameters, writes a .sh file and submits a sbatch job
def run_job(temp_job_folder, job_name, param_dict):

    job_title = f"{job_name}"

    for _, param in param_dict.items():
        job_title += f"_{param}"

    job_file = f"{temp_job_folder}/{job_title}.sh"

    # If you want to pass in arguments to SBATCH that I didn't set up in header function, put them in this dictionary.
    # name:value will be converted to:
    # #SBATCH --{name}={value}
    kwargs = {"example_1": "val_1", "example_2": "val_2"}

    job_header = header(
        job_name=job_name,
        partition="willett-gpu",
        logs_folder=temp_job_folder,
        time_limit=None,
        gpu_type="nvidia_l40s",
        num_gpus=1,
        memory_in_gigabytes=24,
        cpus_per_task=8,
        **kwargs,
    )

    with open(job_file, "w") as fh:
        fh.writelines(job_header)

        # If you want to create a virtual environment and install dependencies using requirements.txt, leave these lines
        # Otherwise comment them out
        fh.writelines(
            f"if [! -d {temp_job_folder}/.venv; then \n   python -m venv {temp_job_folder}/.venv \nfi\n"
        )
        fh.writelines(f"source ./{temp_job_folder}/.venv/bin/activate \n")
        fh.writelines("pip install -r requirements.txt \n")

        # Calling the actual script
        fh.writelines(
            "python /path/to/my_python_script.py\\\n"
        )  ################################# change python script

        for name, param in param_dict.items():
            fh.writelines(f"--{name} {param} \\\n")

    os.system(f"sbatch {job_file}")  # WARNING: comment this line the first time
    #          you run this file to check that the
    #          .sh files came out as inteneded. It may
    #          also be a good idea to run one of the
    #          generated .sh files.


count = 0

parameter_names = [
    "param_1",
    "param_2",
]

# ts stores a list of values that correspond to one .sh file. The length of ts is the number of .sh files you would like to create and submit jobs for.
# Edit the values of this variable for your own code
# the ts below has two values in the list, so two .sh files are created with the parameters in the tuple
ts = [
    ("name_a", 1, 5),  # this tuple corresponds to parameters for one .sh file
    ("name_a2", 3, 5),
    ("name_b1", 3, 5),
]

for idx, t in enumerate(ts):
    assert (
        len(t) == len(parameter_names) + 1
    ), f"Number of arguments at index {idx} ({len(t) - 1}) does not match number of parameter names ({len(parameter_names)})."

param_dicts = [
    (t[0], {name: val for name, val in zip(parameter_names, t[1:])}) for t in ts
]

for job_name, param_dict in param_dicts:
    count += 1
    run_job(temp_job_folder, job_name, param_dict)
