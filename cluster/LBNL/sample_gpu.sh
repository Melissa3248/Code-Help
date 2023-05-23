#!/bin/bash -l
#SBATCH --time=06:00:00
#SBATCH -C gpu # change gpu to gpu&hbm80g to request an 80GB memory node 
#SBATCH --account=m****_g
#SBATCH --nodes=16
#SBATCH --qos=regular
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user=user@domain.com
#SBATCH --ntasks-per-node=4
#SBATCH --gpus-per-node=4
#SBATCH --cpus-per-task=32
#SBATCH -J job_name
#SBATCH -o output_filename.out


# other qos options:
# - debug, limited time and # of submissions
# - overrun, use when the GPU allocation has depleted

# activate the conda environment if you've created one
source activate my_conda_env

# run the Python script
python script_name.py
