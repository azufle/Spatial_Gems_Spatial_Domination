class Rectangle():
	def __init__(self, min_vals, max_vals):
		self.min_vals=min_vals
		self.max_vals=max_vals

def max_dist(X_min,X_max,x):
	max1 = abs(x-X_min)
	max2 = abs(x-X_max)
	if (max1 >= max2):
		return max1
	else: 
		return max2

def min_dist(X_min,X_max,x):
	if (x<X_min):
		return X_min-x
	elif (x<=X_max):
		return 0
	else:
		return x-X_max

def spatial_domination(A,B,R,P):
	sum = 0
	for i in range(0,len(A.min_vals)):
		max1 = max_dist(A.min_vals[i],A.max_vals[i],R.min_vals[i])-min_dist(B.min_vals[i],B.max_vals[i],R.min_vals[i])
		max2 = max_dist(A.min_vals[i],A.max_vals[i],R.max_vals[i])-min_dist(B.min_vals[i],B.max_vals[i],R.max_vals[i])
		if (max1 >= max2):
			sum = sum+max1
		else:
			sum = sum+max2
	print(sum<0)
	return sum<0


A = Rectangle([0,2],[0,2])
B = Rectangle([0,0],[0,0])
R = Rectangle([2,2],[10,4])

spatial_domination(A,B,R,0)