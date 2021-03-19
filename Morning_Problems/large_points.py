# Good luck! Remember the points are *real*, not necessarily *integer*.
import math

num_circles = int(input())

x, y, r = [], [], []

for i in range(num_circles):
	x_input, y_input, r_input = map(float, input().split())
	x.append(x_input)
	y.append(y_input)
	r.append(r_input)

num_points = int(input())

for j in range(num_points):
	x_value, y_value = map(float, input().split())
	flag = False
	for k in range(num_circles):
		distance = math.sqrt((x_value - x[k])**2 + (y_value - y[k])**2)
		if distance < r[k]:
			flag = True
	
	if flag == True:
		print("Large")
	else:
		print("Small")
