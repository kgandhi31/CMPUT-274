# Read in the input
n = int(input())

dictionary = {}

for i in range(n):
	binary, word = input().split()
	dictionary[binary] = word

code = input()

# Solve the problem
idx_start = 0
idx_end = 1

while idx_end <= len(code):
	if code[idx_start:idx_end] in dictionary:
		print(dictionary[code[idx_start:idx_end]], end=" ")
		idx_start = idx_end
	idx_end += 1
