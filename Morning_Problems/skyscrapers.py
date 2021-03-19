num_buildings = int(input())

levels = []

for i in range(num_buildings):
	levels.append(int(input()))

sorted_levels = sorted(levels)

print(num_buildings) # at least 1 level

current_level = 1
for i in range(num_buildings):
	if sorted_levels[i] > current_level:
		for j in range(sorted_levels[i] - current_level):
			print(num_buildings-i)
			current_level = sorted_levels[i]
