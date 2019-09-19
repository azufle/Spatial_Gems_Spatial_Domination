#A minimal definition of a D-dimensional rectangle class
#defined by a list of length D min_vals (the "lower-left" corner) and
#a list of length D max_vals (the "upper-right" corner)
class Rectangle():
	def __init__(self, min_vals, max_vals):
		self.min_vals=min_vals
		self.max_vals=max_vals

#The maximum distance between two (one-dimensional) intervals
def max_dist(X_min,X_max,x):
	max1 = abs(x-X_min)
	max2 = abs(x-X_max)
	if (max1 >= max2):
		return max1
	else: 
		return max2

#The minimum distance between two (one-dimensional) intervals
def min_dist(X_min,X_max,x):
	if (x<X_min):
		return X_min-x
	elif (x<=X_max):
		return 0
	else:
		return x-X_max

#The spatial domination function, as defined in
#Emrich, Tobias, Hans-Peter Kriegel, Peer Kröger, Matthias Renz, and Andreas Züfle. 
#"Boosting spatial pruning: on optimal pruning of MBRs." 
#In Proceedings of the 2010 ACM SIGMOD International Conference on Management of data, 
#pp. 39-50. ACM, 2010.
#Takes three rectangles A, B, and R. 
#Decides if A dominates B with respect to R using a P-norm P as distance function.
#For Euclidean Distance use P=2
#For Manhattan Distance use P=1


def spatial_domination(A,B,R,P):
	sum = 0
	for i in range(0,len(A.min_vals)):
		max1 = max_dist(A.min_vals[i],A.max_vals[i],R.min_vals[i])**P-min_dist(B.min_vals[i],B.max_vals[i],R.min_vals[i])**P
		max2 = max_dist(A.min_vals[i],A.max_vals[i],R.max_vals[i])**P-min_dist(B.min_vals[i],B.max_vals[i],R.max_vals[i]**P)
		if (max1 >= max2):
			sum = sum+max1
		else:
			sum = sum+max2
	print(sum<0)
	return sum<0


#A simple test case in which rectangle A dominates rectangle B with respect to R using Euclidean Distance
A = Rectangle([0,2],[0,2])
B = Rectangle([0,0],[0,0])
R = Rectangle([2,2],[10,4])

spatial_domination(A,B,R,2)