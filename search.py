def searching(l, w):
	a = "".join(l)
	#d = l
	b = a.lower()
	c = 0
	for i in b:
		if w in b:
			print("C is: ", c)
			return True
		#if i == w:
		#	return c
		else:
			c += 1
	print("C is: ", c)
	return "Not Found"

a = open("another1.txt")
b = a.read()
c = b.split()
print(searching(c, "ababua"))