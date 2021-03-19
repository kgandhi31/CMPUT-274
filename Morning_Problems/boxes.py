# read in the values for each item
num_boxes, num_items = map(int, input().split())

m_numbers = list(map(int, input().split()))

# now solve the problem
min_num = min(m_numbers)
print(num_boxes - min_num + 1)
