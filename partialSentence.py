def partial(c):
	a = []
	e = ['(', ')', 'N', 'P', 'D', 'T', 'V', 'Z', 'G', 'B', 'S']
	for i in c:
		if i in e:
			pass
		else:
			a.append(i)
	e = "".join(a)
	return e

a = open("partial.txt")
b = a.read()
c = b.strip()
print(partial(c))