#!/bin/bash

#SBATCH --job-name={{ job_name }}
#SBATCH --time={{ job_timelimit }}
#SBATCH --partition=general
#SBATCH --gres=gpu:{{ num_gpus }}
#SBATCH --mem={{ memory }} # This line can be deleted if you don't need a lot of memory
#SBATCH --output={{ logs_folder }}/{{ job_name }}.out
#SBATCH --error={{ logs_folder }}/{{ job_name }}.err


# These lines log the info about the start of the job to the output file specified above
echo "`date` Starting Job"
echo "SLURM Info: Job name:${SLURM_JOB_NAME}"
echo "    JOB ID: ${SLURM_JOB_ID}"
echo "    Host list: ${SLURM_JOB_NODELIST}"
echo "    CUDA_VISIBLE_DEVICES: ${CUDA_VISIBLE_DEVICES}"
# Always good to make sure you are using the correct python version
which python


python script.py \
-arg_1 val_1 \
-arg_2 val_2
