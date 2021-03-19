# Read the input
n = int(input())

# Alice plays first
# Assume both players play optimally
# n = 1: Alice
# n = 2: Alice
# n = 3: Bob
# n = 4: Alice
# n = 5: Bob
# n = 6: Bob
# n = 7: Alice
# n = 8: Alice
# n = 9: Bob

# n = 14: Alice
# n = 15: Bob

# Bob wins on n values that are divisible by 3

if (n % 3) == 0:
	print("Bob wins")
else: 
	print("Alice wins")
