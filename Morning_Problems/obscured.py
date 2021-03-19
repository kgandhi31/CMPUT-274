num_list = list(map(int, input().split()))
output = ["X"]
stack = [[num_list[0], 0]]

for i in range(1, len(num_list)):
	if num_list[i] > stack[0][0]:
		output.append("X")
		stack = [[num_list[i], i]]
	elif num_list[i] == stack[0][0]:
		output.append(str(stack[0][1]))
		stack = [[num_list[i], i]]
	else:
		for j in range(len(stack)):
			if stack[-1-j][0] > num_list[i]:
				output.append(str(stack[-1-j][1]))
				if j!= 0:
					stack = stack[:len(stack)-j]
				if ((i+1) < len(num_list)) and (num_list[i+1] <= num_list[i]):
					stack.append([num_list[i], i])
				break

			if stack[-1-j][0] == num_list[i]:
				output.append(str(stack[-1-j][1]))
				stack = stack[:len(stack)-j]
				stack.append([num_list[i], i])
				break

print(*output)
