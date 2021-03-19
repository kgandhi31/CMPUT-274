t = int(input())

speed = list(map(int, input().split()))

new_position = []

passes = 0

for i in range(len(speed)):
	new_position.append(i + t*(speed[i]))

for j in range(len(new_position)):
	for k in range(j, len(new_position)):
		if new_position[j] > new_position[k]:
			passes += 1

print(passes)
