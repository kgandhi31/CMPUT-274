# Read in the input
array = list(map(int, input().split()))

# Solve
counter = 1;
max_counter = 1;
for i in range(len(array) - 1):
	if array[i] == array[i + 1]:
		counter += 1
	else:
		counter = 1
	if counter > max_counter:
		max_counter = counter

# Output
print(max_counter)
