import statistics 
import sys 
import random 

if __name__ == "__main__":
    fileName = sys.argv[1]
    size = int(sys.argv[2])
    mu = float(sys.argv[3])
    sd = float(sys.argv[4])

vs = [random.gauss(mu=mu, sigma=sd) for i in range(size)]

print( f"Size: {size}")
print( f"Mean: requested={mu}, generated={statistics.mean(vs)}" )
print( f"Stddev: requested={sd}, generated={statistics.stdev(vs)}" )
    
with open(file=fileName, mode="w") as f:
        for v in vs:
            print( v, file=f )
