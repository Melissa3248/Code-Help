# Commands for computing on Perlmutter 

Request interactive GPU resources:

```salloc --nodes # --qos interactive --time 00:15:00 --constraint gpu --gpus # --account=m****_g```

Request interactive CPU resources:

```salloc --nodes # --qos interactive --time 00:15:00 --constraint cpu --account=m****```

View information about all running jobs:

```squeue --format="%.18i %.9P %.30j %.8u %.8T %.10M %.9l %.6D %R" --me```

Query real-time information about a running job:

```sstat -j <job#>```

Check submitted jobs (should only run this command once if necessary, it disrupts scheduling):

```sqs```


Sample .sh file to submit a CPU-based job: See ```sample_cpu.sh```

Sample .sh file to submit a GPU-based job: see ```sample_gpu.sh```
