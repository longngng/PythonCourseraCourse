# -problem3_6.py *- coding: utf-8 -*-

import sys

# add your code here
infilename = sys.argv[1]
outfilename = sys.argv[2]

infile = open(infilename)
outfile = open(outfilename, 'w')

for line in infile:  
    num = len(line.strip('\n'))      
    #print(num)
    outfile.write(str(num))
    outfile.write('\n')

infile.close()
outfile.close()