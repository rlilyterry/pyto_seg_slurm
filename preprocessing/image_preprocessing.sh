#!/bin/bash

#SBATCH -n 1
#SBATCH -t 0-04:00
#SBATCH -p serial_requeue
#SBATCH --mem-per-cpu=1000
#SBATCH -o %A_%a.out
#SBATCH -e %A_%a.err
#SBATCH --mail-type=ALL
#SBATCH --mail-user=rlilyterry@fas.harvard.edu

img_dir=$1
colors=$2

source new-modules.sh
source activate PYTO_SEG_ENV
module load fiji/1.49j-fasrc01

python3 ~/code/pyto_seg_slurm/preprocessing/img_file_cleanup.py -d $img_dir

fiji --headless ~/code/pyto_seg_slurm/preprocessing/batch_merge_channels.py $img_dir $colors
