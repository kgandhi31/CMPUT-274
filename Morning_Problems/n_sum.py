# Input
n, m = list(map(int, input().split()))

# Solve
num_sum = 0
numbers = []

while num_sum != m:
	temp = num_sum
	temp += n

	if temp <= m:
		num_sum += n
		numbers.append(n)

	n -= 1

print(len(numbers))
print(*sorted(numbers))
