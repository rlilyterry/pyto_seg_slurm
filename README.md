# -= pyto_seg_slurm =-
Submission scripts for image pre-processing, [pyto_segmenter](https://github.com/deniclab/pyto_segmenter/) segmentation, and post-segmentation analysis on Harvard's Odyssey cluster

Author: Nicholas Weir, nweir[at]fas[dot]harvard[dot]edu

__Note:__ These scripts are currently designed for running on my personal RC account, and will require some fiddling with paths and other preparation to make it work for you. Ask me if you need help.

## Contents:
Three sets of scripts contained in separate sub-directories:

__preprocessing:__ For pre-segmentation processing of images acquired on the Murray/Garner lab spinning disk confocal.
- image_preprocessing.sh, img_file_cleanup.py, and batch_merge_channels.py: for automatically renaming image filenames based on stage position numbering and a stage_positions.STG reference table, then generating ImageJ/Fiji-format multi-channel images and maximum intensity projections.
- norm_camera.sh and .py: For normalizing camera background both within and across images according to a camera background channel acquired at each stage position/timepoint combination.

__segmentation:__ For performing segmentation on fluorescence microscopy images using pyto_segmenter. See the scripts for command-line arguments (more details will be explained in this readme soon)
- batch_pex_seg.sh, batch_pex_seg_cfp.sh, and batch_pex_seg.py: for segmenting foci visualized in either the red (batch_pex_seg.sh) or cyan (batch_pex_seg_cfp.sh) channels.
- batch_mito_seg.sh and .py: For segmenting reticular structures visualized in the cyan channel. _important note_: this script is optimized specifically for segmenting mitochondria using endogenously expressed Tom70-mTurquoise2 imaged at 35% laser power with a 100 ms exposure and 100 units EM gain. For other purposes, it will need to be modified.
- mito_and_pex_seg.sh and .py, mito_and_pex_seg_nooverlap.sh and .py: For segmenting both foci (red) and reticular structures (cyan). Same note as above for batch_mito_seg. nooverlap removes parts of reticular structures that overlap with foci (but not vice versa).

__analysis__: For post-segmentation analysis of segmented structures.
- parallel_analysis.sh and .py: for measuring fluorescence intensities in the yellow channel for objects segmented in either cyan or red above. outputs a .csv-formatted table of objects with intensity and volume for each object along with origin metadata.
- combine_outputs.sh and .py: for combining multiple .csv-formatted outputs generated using parallel_analysis.sh and .py.

Last updated: 10.10.2017
