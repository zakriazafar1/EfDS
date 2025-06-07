# every now & then we have to write a python script 
# we need more parameters, we need the command line for this

import sys 
fileName = sys.argv()

with open(fileName, 'r') as file:
    lines = file.readlines()
    
print("The file has", len(lines), "lines.")