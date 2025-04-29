from typing import Literal


def header(
    job_name: str,
    partition: str = "willett-gpu",
    logs_folder: str | None = None,
    time_limit: str | None = None,
    gpu_type: Literal["cpu"] | Literal["gpu"] | str = "gpu",
    num_gpus: int = 1,
    memory_in_gigabytes: int | None = None,
    cpus_per_task: int = 1,
    **kwargs,
):
    header = "#!/bin/bash \n\n"

    header += f"#SBATCH --job-name={job_name}\n"

    if time_limit:
        header += f"#SBATCH --time={time_limit}\n"

    header += f"#SBATCH --partition={partition}\n"

    if gpu_type != "cpu":
        header += f"#SBATCH --gres=gpu{":" + gpu_type if gpu_type != "gpu" else ""}:{num_gpus}\n"

    header += f"#SBATCH --mem={memory_in_gigabytes}G\n"

    header += f"#SBATCH --cpus-per-task={cpus_per_task}\n"

    header += f"#SBATCH --output={logs_folder}/{job_name}.out \n"
    header += f"#SBATCH --error={logs_folder}/{job_name}.err \n\n"

    for key, value in kwargs.items():
        header += f"#SBATCH --{key}={value}\n"

    header += "\n"

    return header
