# TTIC-specific Information

__TTIC help page: https://slurm.ttic.edu/__

## Connecting off campus

If your computer is connected to the eduroam wifi network via your UChicago account, you can run this line in your terminal to log in:

```ssh your_username@slurm.ttic.edu```

If you are off campus, you will need a VPN to secure your connection. The following links give instructions for downloading Cisco AnyConnect Client on various operating systems:

Windows: https://uchicago.service-now.com/it?id=kb_article&kb=KB06000719

iOS: https://uchicago.service-now.com/it?id=kb_article&kb=KB06000727

MacOS: https://uchicago.service-now.com/it?id=kb_article&kb=KB06000725

After downloading Cisco AnyConnect, connect to ```vpn.uchicago.edu```. This will open a window to login to your UChicago account using 2FA.

## Filepath information 

Path to the shared Willett-group directory where computing should be done:

```/share/data/willett-group```

Path to your own home directory:

```/home-nfs/your_username```

Logging out of the TTIC cluster:

```exit```

The TTIC cluster has different partitions, explained in this section of the documentation: [link](https://slurm.ttic.edu/#understanding-partitions). Members of the Willett group have access to the `willett-gpu` and `willett-gpu`. 

## Useful commands

Request GPU resources for an interactive job (see the TTIC help page for customization options):

```srun -p contrib-gpu --pty bash```

Request CPU resources for an interactive job: 

```srun -p contrib-cpu --pty bash```

Check the presence of a GPU:

```nvidia-smi```

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

