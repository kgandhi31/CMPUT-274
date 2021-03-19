# Input
num = int(input())
x_list = list(map(int, (input().split())))
y_list = list(map(int, (input().split())))

# Solve
max_product = 0

x_list.sort()
y_list.sort()

for i in range(num):
	max_product += x_list[i]*y_list[i]

print(max_product)
