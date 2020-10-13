#!/bin/bash
#Author: Joan ENRIQUE-ROMERO
#Date:   %d_%m_%Y
#OAR -n Si
#OAR -O G16.%jobid%.o
#OAR -E G16.%jobid%.e
#OAR -l /nodes=1/core=8,walltime=4:00:00
#OAR --project docgrains


source /applis/site/env.bash
source /applis/site/cecic/gaussian16/env_g16.sh B.01/nehalem 


echo ${OAR_JOB_ID} == $(date) == Si.com >> /home/tinaccil/launched_jobs.txt
MY_INPUT_DIR=/home/tinaccil/atoms+/Si
MY_OUTPUT_DIR=/home/tinaccil/atoms+/Si
MY_INPUT_FILE=Si.com
MY_OUTPUT_FILE=Si.log


MY_SCRATCH_DIR=/bettik/tinaccil/g16

echo MY_SCRATCH_DIR=${MY_SCRATCH_DIR}
[ -d ${MY_SCRATCH_DIR} ] || mkdir -p ${MY_SCRATCH_DIR};
MY_JOB_SCRATCH_DIR=${MY_SCRATCH_DIR}/${OAR_JOB_ID}_Si
mkdir -p ${MY_JOB_SCRATCH_DIR}

echo MY_JOB_SCRATCH_DIR=${MY_JOB_SCRATCH_DIR}
cp -r ${MY_INPUT_DIR}/*.* ${MY_JOB_SCRATCH_DIR}

#-- Go to scratch dir --#
cd ${MY_JOB_SCRATCH_DIR}

#-- Run Gaussian --#
g16 < ${MY_INPUT_FILE} >${MY_OUTPUT_FILE}
mv ${MY_JOB_SCRATCH_DIR} ${MY_OUTPUT_DIR}/${OAR_JOB_ID}.Si
cd ${MY_OUTPUT_DIR}
rm -f G16.${OAR_JOB_ID}.o G16.${OAR_JOB_ID}.e

