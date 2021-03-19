# read in the input
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())

# solve the problem
length = abs(x2 - x1)
width = abs(y2 - y1)
area = length*width

# output the result
print(area)
