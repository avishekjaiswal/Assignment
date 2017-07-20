def solve(numheads,numlegs):
	for i in range(numheads+1):
		j=numheads-i
        	if 2*i+4*j==numlegs:
            		return i,j
numheads=35
numlegs=94
print("\nThe solution puzzle: ")
solutions=solve(numheads,numlegs)

print ("{} number of chickens and {} number of rabbits".format(solutions[0],solutions[1]))