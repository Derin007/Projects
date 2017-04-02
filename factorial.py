"""def fibonacci(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n > 1:
		return n + fibonacci(n - 1)

#print("Enter a number here: ", n = int(input()))
print("Enter a number below:")
print("The fibonacci number is:",fibonacci(int(input())), end="")"""

"""def factorial(n):
	if n == 0:
		return 1
	elif n > 0:
		return n * factorial(n - 1)
	else:
		return -1

print("Enter a number below:")
print("The factorial is:", factorial(int(input())), end="")"""

"""def b(z):
	prod = a(z, z)
	print(z, prod)
	return prod

def a(x, y):
	x = x + 1
	return x * y

def c(x, y, z):
	sum = x + y + z
	pow = b(sum) ** 2
	return pow

x = 1
y = x + 1
print(c(x, y+3, x+y), end="")"""


"""def ack(m, n):
	if m == 0:
		return n + 1
	elif m > 0:
		if n < 0:
			return -1
		elif n == 0:
			return ack(m - 1, 1)
		else:
			return ack(m - 1, ack(m, n -1))
	else:
		return -1

print(ack(3, 4), end="")"""

"""def first(word):
	return word[0]

def last(word):
	return word[-1]

def middle(word):
	return word[1:-1]

word = "a"
print(middle(word), end="")"""


def is_power(a, b):
	if a % b == 0:
		c = a // b
		if (b ** c) % a == 0:
			return True
		else:
			a = "Number is a multiple, but not exponent"
			return a
	else:
		return False

print(is_power(128, 2), end="")

'''bruce = 5
print(bruce, end="")
bruce = 7
print(bruce, end="")'''

