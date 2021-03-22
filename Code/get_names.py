# read the name of files
# input the file names to a .txt file

import os
import math

def input_names(dir):
    # search from directories
    for j in range(ord('A'), ord('Z')+1):
        for k in range(ord('A'), ord('Z')+1):
            # open & and append a .txt file
            with open('input_whole.txt', 'a+') as ipt:
                datanames = []
                for l in range(ord('A'), ord('Z')+1):
                    path = dir + chr(j) + '/' + chr(k) + '/' + chr(l)
                    # check if the path exists
                    if os.path.exists(path):
                        datanames = os.listdir(path)
                        for i in datanames:
                           ipt.write(''.join('/input/' + i + '\n'))

# make a new directory
def mkdir(path):
    folder = os.path.exists(path)
    if not folder:
        os.makedirs(path)

# split a .txt file to n files
def split_t(n, path):
    tdata = []
    count = 0
    split = math.ceil(10000/n)
    with open('input_whole.txt', 'r') as ori:
        d = ori.readline()
        while d or count == 10000:
            if count % split == 0:
                txtname = path + 'input_' + str(math.floor(count / split)) + '.txt'
                with open(txtname, 'w') as sipt:
                    for mdata in tdata:
                        sipt.write(mdata)
                    tdata = []
            count = count + 1
            tdata.append(d)
            d = ori.readline()

# input your path to millionsongsubset on PC or VM
origin_dir = your path to millionsongsubset + 'millionsongsubset/'
new_dir = origin_dir + 'input/'
input_names(origin_dir)
mkdir(new_dir)
split_t(10, new_dir)

