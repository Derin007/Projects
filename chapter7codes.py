"""def countdown(n):
	while n > 0:
		print(n, end=" ")
		n = n -1
	print("Blast Off!")

print("Enter a number:")
countdown(int(input()))"""

"""def sequence(n):
	while n != 1:
		print(n, end=" ")
		if n % 2 == 0:
			n // 2
		else:
			n = n * 3 + 1
# This function doesn't terminate. DO NOT EXECUTE
print("Enter a number:")
sequence(int(input()))"""

def print_n(s, n):
	while n > 0:
		return
	print(s)
	print_n(s, n - 1)

def entry():
	return int(input(">"))

print("Enter 2 numbers:")
print(print_n(entry(), entry()))

"""def square(a):
	x = 3
	while True:
		print(a, end=" ")
		y = (x + a // x) // 2
		if y == a:
			break
		x = y10
#This function overflows DO NOT EXECUTE
square(int(input()))"""
