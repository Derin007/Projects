
# to generate dictionary keys for letters with their values as the 
# occurence of the letter in the string
def histogram(s):
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d

h = "aransioladada"
#print(histogram(h))

#rewriting the previous function using the get method.
'''def histogram(s):
	#d = dict()
	a = []
	a = dict(s)
	for c in a:
		a.get(c)
		#if c not in d:
		#	d[c] = 1
		#else:
		#	d[c] += 1
	return d

print(histogram("aransioladada"))'''

def print_list(h):
	for c in h:
		print(c, h[c])
a = histogram(h)
print(a)