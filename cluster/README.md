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