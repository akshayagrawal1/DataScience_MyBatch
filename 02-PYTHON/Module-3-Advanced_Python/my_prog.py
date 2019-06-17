import sys
from os import mkdir

# create a directory 
name1 = sys.argv[1]
name2 = sys.argv[2]
mkdir(name1)
mkdir(name2)

#print('Libraries are imported sucessfully')