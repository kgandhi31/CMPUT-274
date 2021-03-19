# read the input
string = input()

# solve the problem
odd_length = 1

for i in range(1, len(string)): 
    low = i - 1
    high = i + 1
    while low >= 0 and high < len(string) and string[low] == string[high]: 
        if high - low + 1 > odd_length: 
            odd_length = high - low + 1
        low -= 1
        high += 1

# print output
print(odd_length) 
