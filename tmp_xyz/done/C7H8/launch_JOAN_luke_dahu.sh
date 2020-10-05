#!/bin/bash

# Gaussian 16
# WHAT DOES THIS SCRIPT DO??
#=======================================
# This script launches gaussian works
# in Luke. It first generates a batch
# which will be launched as a passive
# calculation through the batch scheduler
# oar.
# Usage: either you just execute it and
# it will ask you all needed data, or 
# you use flags after it:
#  -f file_name.dat(.com) 
#  -n number_of_cores (just 1 node)
#  -i input_dir_path (current) 
#  -o output_dir_dir (current)
#  -t max_time_job (in hours, max 96h, def 96)
#  -s submit_job (y/n, def y)
#  -nt node_type (standard (D.01), nehalem (E.01), sandybridge (E.01))
#		 (def standard)
#=======================================

# This script will generate the script to laung a Gaussian09 job.
echo "Work directory: ${PWD}"
cd ${PWD}

N_CORES=16
TIME=48 #hours
OUT_DIR=${PWD}
INP_DIR=${PWD}
submit="y"

#---------------------------
# Did the user use -f flags?
#---------------------------

if [ $# -eq 0 ] # if no arguments passed
then
   echo "Fill in:"
   # Number of cores
   read -p ">> Number of Cores (max 16): " N_CORES
   read -p ">> Input directory: " INP_DIR
   read -p ">> File name: " G_FILE_NAME
   read -p ">> Output directory: " OUT_DIR
   read -p ">> Time (hours, max 96): " TIME
   read -p ">> Submit directly? (y/n): " submit   
   read -p ">> Node type [DISABLED, input anything, like 'wookie']" NODE_TYPE
   #[standard (D.01)/nehalem (E.01)/sandybridge (E.01)]: " NODE_TYPE
   # since by now G16 is only installed for A.03, the last option is diabled.
else # some arguments passed
    while getopts n:f:i:o:t:s:nt: OPTION; do
        case "${OPTION}"
        in
            n)
                N_CORES=${OPTARG};;
            f)
                G_FILE_NAME=${OPTARG};;
    	    i)
		INP_DIR=${OPTARG};;
	    o)
		OUT_DIR=${OPTARG};;
            t)
                TIME=${OPTARG};;
            s)
		submit=${OPTARG};;
            nt)
		NODE_TYPE=${OPTARG};;
        esac
    done
fi

#if [ -z "$NODE_TYPE"  ]; then # if $NODE_TYPE is empty...
#    echo 'Node type D.01 (universal)'
#    NODE_TYPE="standard"
#fi


echo "Cores:   $N_CORES"
echo "G input: $G_FILE_NAME"


label=${G_FILE_NAME%.*} # label=name file wo extension
SCRIPT_NAME=script_$label.sh

SCRATCH_DIR=/bettik/$USER/g16

#---------------------------
# If script exists remove it
#---------------------------

if [ -e $SCRIPT_NAME ]; then
      rm -f $SCRIPT_NAME
  fi

#---------------------------
# Write in script
#---------------------------

# echo "line1
#       line2" >> myfile.dat

#cat <<EOT >> greetings.txt
#line 1
#line 2
#EOT #(EOT is a random string, could be FOO)



#-- Header --#
echo "#!/bin/bash
#Author: Joan ENRIQUE-ROMERO
#Date:   %d_%m_%Y
#OAR -n $label
#OAR -O G16.%jobid%.o
#OAR -E G16.%jobid%.e
#OAR -l /nodes=1/core=$N_CORES,walltime=$TIME:00:00
#OAR --project docgrains

" >> $SCRIPT_NAME

#-- Load envs & modules --#
echo "source /applis/site/env.bash
source /applis/site/cecic/gaussian16/env_g16.sh B.01/nehalem 

" >> $SCRIPT_NAME

#-- Setting some variables --#
echo "echo \${OAR_JOB_ID} == \$(date) == $G_FILE_NAME >> ${HOME}/launched_jobs.txt
MY_INPUT_DIR=$INP_DIR
MY_OUTPUT_DIR=$OUT_DIR
MY_INPUT_FILE=$G_FILE_NAME
MY_OUTPUT_FILE=${label}.log

" >> $SCRIPT_NAME

#-- Scratch dir --#
# If necessary,create scratch dir; will be locate at /scratch/$USER/<suffix> directory
echo "MY_SCRATCH_DIR=$SCRATCH_DIR

echo MY_SCRATCH_DIR=\${MY_SCRATCH_DIR}
[ -d \${MY_SCRATCH_DIR} ] || mkdir -p \${MY_SCRATCH_DIR};
MY_JOB_SCRATCH_DIR=\${MY_SCRATCH_DIR}/\${OAR_JOB_ID}_$label
mkdir -p \${MY_JOB_SCRATCH_DIR}

echo MY_JOB_SCRATCH_DIR=\${MY_JOB_SCRATCH_DIR}
cp -r \${MY_INPUT_DIR}/*.* \${MY_JOB_SCRATCH_DIR}

#-- Go to scratch dir --#
cd \${MY_JOB_SCRATCH_DIR}

#-- Run Gaussian --#
g16 < \${MY_INPUT_FILE} >\${MY_OUTPUT_FILE}
mv \${MY_JOB_SCRATCH_DIR} \${MY_OUTPUT_DIR}/\${OAR_JOB_ID}.$label
cd \${MY_OUTPUT_DIR}
rm -f G16.\${OAR_JOB_ID}.o G16.\${OAR_JOB_ID}.e
" >> $SCRIPT_NAME

#---------------------------
# submit project
#---------------------------
chmod +x $SCRIPT_NAME

if [ $submit = "y" ]; then
   oarsub -S ./$SCRIPT_NAME
fi

