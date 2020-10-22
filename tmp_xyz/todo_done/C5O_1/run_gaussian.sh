#!/bin/sh
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=24
#SBATCH --ntasks=24
#SBATCH --time=24:00:00
#SBATCH --constraint=HSW24
mkdir /scratch/cnt0027/pag0797/spantaleone/GAUSSIAN/gauss_scratch/C5O_1X
. $g16root/home/spantaleone/g16/bsd/g16.profile
export GAUSS_SCRDIR=/scratch/cnt0027/pag0797/spantaleone/GAUSSIAN/gauss_scratch/

g16 $1
rm -r /scratch/cnt0027/pag0797/spantaleone/GAUSSIAN/gauss_scratch/C5O_1X
