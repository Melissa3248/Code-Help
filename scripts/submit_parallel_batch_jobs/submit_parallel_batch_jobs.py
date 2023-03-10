##################################################################################################################
#                                  How to change this file for your own purposes                                 #
##################################################################################################################
#
# 1. Rename the temp_job_folder variable to a short descriptor of this job (line 21)
# 2. Edit the ts variable to contain a list of tuples. The tuple should contain information corresponding to
#    a specification of one .sh file. The length of ts should correspond to the number of .sh files you would like
#    to submit jobs for. (lines 52-53)
# 3. Edit the names of the variables that are pulled from each tuple in the tx list. (lines 57-59)
# 4. Edit the .sh header in the run_job function to be consistent with a typical .sh header for your cluster. (lines35-41)
#    See Code-Help/cluster/{TTIC,LBNL,RCC} for example .sh files. Also be sure to edit the additional parameter
#    arguements (named param_1 and param_2) to be consistent with the parameter names in your python script
#    (named my_python_script.py here).
# 5. Comment out line 42 on your first run of this code to in order to check that the .sh files produced are correct.
#    It may also be good to run one .sh file produced to see if the desired results are produced w/o error.
##################################################################################################################

import os

# names a folder to be added in the current working directory named 'temp_job'
temp_job_folder = ‘temp_job’


# creates a folder in the current working directory named 'temp_job'
def mkdir_p(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
mkdir_p(temp_job_folder)

# given input parameters, writes a .sh file and submits a sbatch job
def run_job(temp_job_folder, job_name, param_1, param_2):
    job_file = ‘{}/{}_{}_{}.sh’.format(temp_job_folder, job_name, param_1, param_2)
    with open(job_file,‘w’) as fh:
        # the .sh file header may be different depending on the cluster
        fh.writelines("#!/bin/bash\n")
        fh.writelines("#SBATCH -n 1\n") # number of nodes to allocate for this job
        fh.writelines("#SBATCH -t HH:MM:SS") # max amount of time for the job
        fh.writelines("#SBATCH -j {}_{}_{}".format(job_name, param_1,param_2))
        fh.writelines("python /path/to/my_python_script.py\\\n") ################################# change python script
        fh.writelines("--param_1 {} \\\n".format(param_1))
        fh.writelines("--param_2 {} \\\n".format(param_2))
    os.system(‘sbatch {}’.format(job_file)) ###################### WARNING: comment this line the first time
                                                                            #          you run this file to check that the
                                                                            #          .sh files came out as inteneded. It may
                                                                            #          also be a good idea to run one of the
                                                                            #          generated .sh files.
count = 0

# ts stores a list of values that correspond to one .sh file. The length of ts is the number of .sh files you would like to create and submit jobs for.
# Edit the values of this variable for your own code
# the ts below has two values in the list, so two .sh files are created with the parameters in the tuple
ts = [("my_job", 1, 2), # this tuple corresponds to parameters for one .sh file
    ("my_job", 3, 4)]

for t_ix in ts:
    count += 1
    job_name = t_ix[0]
    param_1 = t_ix[1]
    param_2 = t_ix[2]

    run_job(temp_job_folder, job_name, param_1, param_2)
