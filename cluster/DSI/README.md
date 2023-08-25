# DSI Cluster-specific Information

A more detailed page for getting setup on the DSI cluster can be found at: https://github.com/meliao/cluster_startup

The login command to access the login node is 
```
ssh your_cnetid@fe01.ds.uchicago.edu
```


Logging out of the DSI cluster:

```
exit
```
Or `Ctrl+D`.

The DSI cluster has two partitions, `dev`, which is for debugging (10 minute time limit) and `general`, which has a 12 hour time limit.

## Useful commands

Request 1 GPU for an interactive job:
```
srun -p general --mem=80G --gres=gpu:1 --pty bash
```
Request 8 CPUs and 80GB of memory for an interactive job:

```
srun -p general --mem=80G -c 8 --pty bash
```

Submit a batch job that is written in job.sh
```
sbatch job.sh
```

Check the presence of a GPU:

```
nvidia-smi
```


Check how much disk storage you have left: 
```
csquota
```

### New Cluster Setup Notes
Here are a list of steps I've taken to set up on the DSI cluster:

1. Log in and set up SSH
    a. add the public key from your laptop (It's most likely in a file called `id_rsa.pub`) to the file `.ssh/authorized_keys` on the cluster.
2. Add information to local `.ssh/config`. For me, it looks like:
    ```
    Host dsi
    HostName fe01.ds.uchicago.edu
    User meliao
    IdentityFile ~/.ssh/id_rsa
    ForwardAgent yes
    ```
3. Download and install miniconda
    ```
    wget https://repo.anaconda.com/miniconda/Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
    sh Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
    ```
4. Clone a code repository :
    ```
    git clone git@github.com:meliao/lorentz_group_random_features.git
    ```
5. Set up conda environment. In my code repository I had a file called `env.yaml` that had a list of all of the packages I needed for this project. I created this file by going to my laptop (where I had the correct conda environment set up) and running `conda env export --from-history > env.yaml`. There are 2 steps to the setup, because sometimes getting the correct version of pytorch installed is tricky.
    a. Install everything except pytorch and CUDA:
    ```
    conda env create -f env.yaml
    ```
    b. Install pytorch/CUDA:
    ```
    srun --gres=gpu:1 --pty bash # Get on a node with a GPU
    conda activate environment_name # Substitute in the correct environment name

    # Do something to find out CUDA version. In this case it's 11.7
    ls -l /usr/local | grep cuda
    
    # Install pytorch that talks to the installed CUDA version
    conda install pytorch pytorch-cuda=11.7 -c pytorch -c nvidia

    # This line checks whether the newly-installed pytorch can access a GPU. Should print `True` if everything was successful
    python -c "import torch; print(torch.cuda.is_available())"
    ```

### TMUX

When you ssh to the SLURM server from your laptop, you request a GPU/CPU to run your experiemnts. However, if your laptop turns off or connection breaks, it may lead to loosing GPU/CPU too. To avoid it, TMUX can be used. 

After ssh'ing to the server (but before requestiong CPU/GPU), type 

```tmux```

or 

```tmux new -s sessionname```


It'll create a new TMUX session. This session will remain even after you accidentually discinnect from the cluster. In this tmux session, you can create new kinda terminal windows via ```ctrl b c``` and move between them via ```ctrl b n```(next) or  ```ctrl b p```(previous). Through these windows you can request and submit different jobs, and they run no matter if you're connected to a server.

After you create a TMUX session and connectiong to a server again you can type 

```tmux a```
```tmux a -t sessionname```

to attach to the exsisting tmux session. 

More shortcuts are available [here](https://gist.github.com/MohamedAlaa/2961058).

