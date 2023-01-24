import argparse
import numpy as np

def sample_function(p1,p2):
    return p1*p2


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--param_1", type=int, help = "descriptive information about what this variable is")
    parser.add_argument("--param_2", type=int, help = "descriptive information about what this variable is")
    args = parser.parse_args()

    param_1 = args.param_1
    param_2 = args.param_2
    output = sample_function(param_1, param_2)

    # maybe you want to save the output in a numpy file
    np.save("output.npy", output)
