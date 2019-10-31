import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.
ext_to_mt = {}
for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    ext_to_mt[ext.lower()] = mt


for i in range(q):
    fname = input()  # One file name per line.
    mt = 'UNKNOWN' 

    if '.'  in fname:
        ext = fname.split('.')[len(fname.split('.'))-1].lower()
        if ext in ext_to_mt:
            mt =  ext_to_mt[ext] 
    print(mt)

