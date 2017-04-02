import string

def subtract(d1, d2):
	res = dict()
	for key in d1:
		if key not in d2:
			res[key] = None

	return res

a = open('throughtelescope.txt')
b = open('word1.txt')

#c = subtract(a, b)
#for word in c.keys():
	#print(word)

#print(subtract(a, b))

def linecount(filename):
	count = 0
	for line in open(filename):
		count += 1
	return count

print(linecount('subtractwords.py'))
