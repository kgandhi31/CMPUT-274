# Read input here.
num_points = int(input())

# Solve problem here. Good luck!
from math import factorial

# combination formula: C(n, r) = n!/(n-r)!r!
output = int((factorial(num_points))/(factorial(num_points - 3)*factorial(3)))
print(output)
