num_buses = int(input())

bus_numbers = [int(i) for i in input().split()]
bus_numbers.sort()

output = ""
i = 0
while i < len(bus_numbers):
	count = 1
	for j in range(i, len(bus_numbers)):
		if j != len(bus_numbers) - 1:
			if bus_numbers[j] +1 != bus_numbers[j+1]:
				break
			else:
				count += 1
	if count > 2:
		output += str(bus_numbers[i]) + "-" + str(bus_numbers[i+count-1]) + " "
		i += count
	else:
		output += str(bus_numbers[i]) + " "
		i += 1

print(output[0:-1])
