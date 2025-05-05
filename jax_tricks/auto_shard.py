import jax


def auto_shard(func, axis=0):
    """
    This takes in a jitable function "func" and transforms it into a function which automatically parallelizes the computation over all the gpus available to JAX. It does this over the first axis. Importantly, this means that
    the number of devices must divide the shape of the first axis
    """
    num_devices = jax.device_count("gpu")
