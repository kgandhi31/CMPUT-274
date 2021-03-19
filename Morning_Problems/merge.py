# get list of vehicles in the left lane
left_lane = list(map(str, input().split()))

# now do something similar to get the list of vehicles in the right lane
right_lane = list(map(str, input().split()))

# Solve the problem
merged_list = []

for i in range(max(len(left_lane), len(right_lane))):
	if i < len(left_lane):
		merged_list.append(left_lane[i])

	if i < len(right_lane):
		merged_list.append(right_lane[i])

# Print the result

#print(*merged_list, sep = ' ')

print(' '.join(merged_list))
