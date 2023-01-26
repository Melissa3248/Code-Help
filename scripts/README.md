# Useful General Purpose Scripts

__submit_parallel_batch_jobs__: contains two python scripts: submit_parallel_batch_jobs.py contains code to submit a large number of sbatch jobs for different input parameters. In this example script, it runs the file my_python_script for various parameter inputs. my_python_script.py parses the input arguments given by the submit_parallel_batch_jobs.py file, and performs some computations based on a given set of input parameters. Both scripts require editing in order to be used for your purposes.

__logging_to_out_file__: contains an example .sh file and .py file to save information to a .out file for an sbatch job (adding print statements in the .py file does not get saved to the .out file). The output of this example is shown in the test.out file.
