def prompt1():
	return int(input())
	"""b = int(input())
	c = int(input())
	d = int(input())
	return a,b,c,d"""


def check_fermat(a, b, c, d):
	e = (a ** d) + (b ** d)
	if d <= 2:
		if e == (c ** d):
			print("This is the default and it works.")
		else:
			print("What's going on here, this should be default! Check digit ordering.")
	if d >= 3:
		if e == (c ** d):
			print("Holy smokes, Fermat was wrong!")
		else:
			print("No, that doesn't work")

print("Enter four numbers, Note fourth number is the exponent")
check_fermat(prompt1(), prompt1(), prompt1(), prompt1())
#check_fermat(prompt1())
