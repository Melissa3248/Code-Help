#!/bin/bash -l
#SBATCH --time=06:00:00
#SBATCH -C cpu
#SBATCH --account=m****
#SBATCH --nodes=16
#SBATCH --qos=regular
#SBATCH --mail-type=begin,end,fail
#SBATCH --mail-user=user@domain.com
#SBATCH -J job_name
#SBATCH -o output_filename.out


# other qos options:
# - debug, limited time and # of submissions
# - overrun, use when the GPU allocation has depleted

# activate the conda environment if you've created one
source activate my_conda_env

# run the Python script
python script_name.py
