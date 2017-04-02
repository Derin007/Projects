"""def is_triangle(a, b, c):
	if a > (b + c) or b > (a + c) or c > (a + b):
		print("You cannot form a triangle with these numbers")
	else:
		print("You can form a triangle with these numbers")

is_triangle(4, 8, 12)"""

"""def compare(a, b):
	if a > b:
		#print(1)
		return 1
	elif a == b:
		#print(0)
		return 0
	else:
		return -1

def collection():
	return int(input())

print(compare(collection(), collection()), end="")"""

def is_between(x, y, z):
	if x <= y and y <= z:
		return True
	else: return False

print(is_between(1, 2, 3), end="")

