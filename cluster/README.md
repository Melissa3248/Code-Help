# Useful commands for Slurm-based clusters

Interrupt an interactive job:

```Ctr Z```

Submit a .sh file (file is scheduled to run when resources are available):

```sbatch your_file.sh```

Sample header for a .sh file: See ```sample.sh```

Copy a file from your local computer to the cluster (assumed to be executed in the local file's directory):

```scp local_file username@loginemail:path/to/destination/folder```

Copy a folder from your local computer to the cluster (assumed to be executed in the local folder's directory):

```scp local_folder username@loginemail:path/to/destination/folder```


Convert a file to a non-Windows encoding:
```dos2unix filename```

# Conda

Create a conda environment:

```conda create -n my_env_name```

Create a conda environment with a specific Python version:

```conda create -n my_conda_env3.9 python=3.9```

Create a conda environment with a previous Python and Pytorch versions: (More details at https://pytorch.org/get-started/previous-versions/)

Example: ```conda install pytorch==1.8.1 torchvision==0.9.1 torchaudio==0.8.1 cudatoolkit=10.2 -c pytorch```