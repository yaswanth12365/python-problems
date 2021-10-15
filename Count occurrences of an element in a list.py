# Python code to count the number of occurrences
def countX(lst, x):
	return lst.count(x)

# Driver Code
lst = [8, 6, 8, 10, 8, 20, 10, 8, 8]
x = 8
print('{} has occurred {} times'.format(x, countX(lst, x)))
