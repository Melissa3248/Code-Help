# TTIC-specific Information

__TTIC help page: https://slurm.ttic.edu/__

Logging in to TTIC:

```ssh your_username@slurm.ttic.edu```

Path to the shared Willett-group directory where computing should be done:

```/share/data/willett-group```

Path to your own home directory:

```/home-nfs/your_username```

Logging out of the TTIC cluster:

```exit```

## Useful commands

Request GPU resources for an interactive job (see the TTIC help page for customization options):

```srun -p contrib-gpu --pty bash```

Request CPU resources for an interactive job: 

```TO DO```

Check the presence of a GPU:

```nvidia-smi```

