num_bits, num_journeys = map(int, input().split())

sequence = input()

# start = end = []
start = []
end = []

for i in range(num_journeys):
	st, en = map(int, input().split())
	start.append(st)
	end.append(en)

# solve the problem
for j in range(num_journeys):
	one = False
	zero = False
	if start[j] == end[j]:
		if "1" in sequence[start[j]-1]:
			one = True
		else:
			zero = True
	else:
		if "1" in sequence[(start[j]-1):(end[j]-1)]:
			one = True
		if "0" in sequence[(start[j]-1):(end[j]-1)]:
			zero = True
	# output the answer
	if (one and zero) is True:
		print("both")
	elif one is True:
		print("one")
	else:
		print("zero")	
