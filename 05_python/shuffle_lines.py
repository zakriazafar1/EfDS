import sys 
import random

if __name__ == "__main__":
    inFileName = sys.argv[1]
    outFileName = sys.argv[2] 

with open(file=inFileName, mode="r") as f:
   lines = f.readlines()

random.shuffle(lines)
with open(file=outFileName, mode="w") as f:
    f.writelines(lines)


    
    

    
    




