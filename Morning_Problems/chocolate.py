line = input().split()
chocolates = int(line[0])
jars = int(line[1])
count = 0

# write your code here
for i in range(jars):
	current_chocolates, max_chocolates = map(int, input().split())
	if chocolates <= (max_chocolates - current_chocolates):
		count +=1

print(count)
