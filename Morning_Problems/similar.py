# Read in the input
scores = list(map(int, input().split()))

# Solve the problem and output the result
output = max(scores.count(scores[0]), scores.count(scores[1]), scores.count(scores[2]))

if output == 3:
	print("same")
elif output == 2:
	print("similar")
else:
	print("distinct")
