# Input
length, width = map(int, (input().split()))

# Solve
radius = min(length/2, width/2)
cost_radius = 2*radius

longer_side = max(length, width)
shorter_side = min(length, width)

if (length == width):
	cost_k_sections = 4*(shorter_side/2)*(longer_side/2)*10
else:
	cost_k_sections = (4*shorter_side*(longer_side/2)*1) + (4*shorter_side*(longer_side/2)*2)

cost_total = int(cost_radius + cost_k_sections)
print(cost_total)


