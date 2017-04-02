"""def reader(l):
	b = []
	for i in l:
		if i in b:
			pass
		else:
			b.append(i)
	c = " ".join(b)
	return c
a = open('test.txt')
b = a.read()
c = b.split()
#print(c)
print(reader(c))"""

def reader(l):
	b = []
	for i in l:
		if i in b:
			pass
		else:
			b.append(i)
	c = " ".join(b)
	return c
a = open('throughtelescope.txt')
b = a.read()
c = b.split('"')
#print(c)
print(reader(c))