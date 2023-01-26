#!/bin/bash
#SBATCH -N 1
#SBATCH -C cpu
#SBATCH -q regular
#SBATCH -J test
#SBATCH --mail-user=username@domain.com
#SBATCH --mail-type=ALL
#SBATCH -t HH:MM:SS
#SBATCH --output=%x.out

# change header based on which cluster you submit jobs on
python test.py
