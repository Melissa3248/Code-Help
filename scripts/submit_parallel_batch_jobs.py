import os

# names a folder to be added in the current working directory named 'temp_job'
temp_job_folder = ‘temp_job’


# creates a folder in the current working directory named 'temp_job'
def mkdir_p(dir):
    if not os.path.exists(dir):
        os.mkdir(dir)
mkdir_p(temp_job_folder)

# given input parameters, writes a .sh file and submits a sbatch job
def run_job(temp_job_folder, t_start, t_stop):
    job_file = ‘{}/job_file_eki{:04d}.sh’.format(temp_job_folder, count)
    with open(job_file,‘w’) as fh:
        fh.writelines(“#!/bin/bash\n”)
        fh.writelines(“python ics.py\\\n”)
        fh.writelines(” --folder {} \\\n”.format(‘train’))
        fh.writelines(” --start_t {} \\\n”.format(t_start))
        fh.writelines(” --stop_t {} \\\n”.format(t_stop))
    os.system(‘sbatch -n 1 -c 64 {}’.format(job_file)) ###################### WARNING: comment this line the first time
                                                                            #          you run this file to check that the
                                                                            #          .sh files came out as inteneded. It may
                                                                            #          also be a good idea to run one of the
                                                                            #          generated .sh files.
count = 0

# ts stores a list of values that correspond to one .sh file. The length of ts is the number of .sh files you would like to create and submit jobs for.
# Edit the values of this variable for your own code
ts = [(32, 1096), (1096, 2192)]

for t_ix in ts:
    count += 1


    t_start = t_ix[0]
    t_stop = t_ix[1]

    run_job(temp_job_folder, t_start, t_stop)