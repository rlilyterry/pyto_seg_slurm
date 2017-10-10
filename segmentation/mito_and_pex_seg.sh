#!/bin/bash

#SBATCH -n 1
#SBATCH -t 0-04:00
#SBATCH -p serial_requeue
#SBATCH --mem-per-cpu=1500
#SBATCH -o %A_%a.out
#SBATCH -e %A_%a.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=nweir@fas.harvard.edu

img_dir=$1
high_threshold=$2
low_threshold=$3
ntasks=$4
source new-modules.sh
source activate PYTO_SEG_ENV

cd $img_dir
python3 ~/code/batch_segmentation/mito_and_pex_seg.py -d $img_dir -ht $high_threshold \
	-lt $low_threshold -n $SLURM_ARRAY_TASK_ID -a $ntasks
