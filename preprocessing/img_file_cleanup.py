import os
import sys
import argparse
import re
import subprocess
import csv
import copy

parser = argparse.ArgumentParser(description = 'Eliminate thumb images and \
                                 rename files by stage position labels.')
parser.add_argument('-d', '--directory', 
                    required = True, 
                    help = 'output directory from microscopy, containing  \
                    images and stage_positions.STG file')
parser.add_argument('-s', '--stage_ref',
                    required = False, default = 'none provided',
                    help = 'file for retrieving stage position number:name \
                    lookup. defaults to stage_positions.STG or \
                    stage_positions.txt')
args = parser.parse_args()
directory = args.directory
s = args.stage_ref
def main():
    os.chdir(directory)
    if s != 'none provided':
        stage_ref = s 
    elif 'stage_positions.STG' in os.listdir():
        stage_ref = 'stage_positions.STG'
    elif 'stage_positions.txt' in os.listdir():
        stage_ref = 'stage_positions.txt'
    else:
        sys.exit('No stage position reference file provided.')
    print('stage reference file: ' + stage_ref)
    print('current working directory: ' + os.getcwd())
    subprocess.call("rm *thumb*", shell =
                    True) # rm thumbs
    stage_pos = []
    line = 0
    # rename files based on stage position document
    print('generating stage position reference table...')
    spos_f = open(stage_ref,'r')
    spos_reader = csv.reader(spos_f)
    for row in spos_reader:
        if line < 4:
            pass
        else:
            print('current line:')
            print(row)
            stage_pos.append(row[0])
        line = line + 1
    print('stage position name list:')
    print(stage_pos)
    img_files = [f for f in os.listdir() if '.tif' in f.lower()]
    img_files = tuple(img_files)
    print('list of image files:')
    print(img_files)
    # find stage positions for each image and match them to stage_positions file
    stage_re = re.compile('s\d+')
    stage_IDs = []
    for x in range(0,len(img_files)):
        stage_IDs.append(int(stage_re.search(img_files[x]).group()[1:]))
    renamed_img_files = ['']*len(img_files)
    for x in range(0,len(renamed_img_files)):
        renamed_img_files[x] = re.sub('s\d+',
                                      stage_pos[stage_IDs[x]-1],
                                      img_files[x]).lower()
    rename_dict = dict(zip(img_files, renamed_img_files))
    for key in rename_dict:
    # rename files
        os.rename(key,rename_dict[key].replace(' ','.'))

if __name__ == '__main__':
    main()





        



