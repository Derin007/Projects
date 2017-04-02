#def dictionaryReader():
"""a = open('word1.txt')
b = a.read()
d = b.
c = dict()
for word in b:
	c[word] = 'ade'

#c = dict()
print(c, end='')"""

def histogram(s, *args):
	d = dict()
	a = len(s)
	probability = 0
	for i in s:
		if i not in d:
			d[i] = 1
		else:
			d[i] += 1
		#d[i] = 1
	for c in s:
		d[c] = d.get(c, 0)
		#if c not in d:
			#d[c] = 1
		#else:
			#d[c] += 1
	#return d.keys()
	for i in args:
		if i in d.keys:
			print(i)
			#probability = i / a

	#return probability
	return d

h = histogram('aladewuar', ('a', 'b'))
print(h, end="")

"""def reverse_lookup(d, v):
	a = []
	for k in d:
		if d[k] == v:
			a = k
			#return k
		else:
			a.append(k)  #This line creates a list of the keys
	return a
	#raise ValueError

h = histogram('aladewuar')
#print(h)
k = reverse_lookup(h, 2)
print(k, end='')"""


"""def invert_dict(d):  #Do exercise 11.5 with this
	inv = dict()		#Get it done this weekend
	a = []				#3/17 - 3/19
	for (key, value) in d:
		a = d.setdefault(key, None)
		val = d[key]
		if val not in inv:
			inv[val] = [key]
		else:			
			inv[val].append(key)
	return a

h = histogram('aladewuar')
inv = invert_dict(h)
print(inv)"""


"""known = {0:0, 1:1}

def fibonacci(n):
	if n in known:
		return known[n]

	res = fibonacci(n - 1) + fibonacci(n - 2)
	known[n] = res
	return res

print(fibonacci(10))
print(known)


 def sumall(*args):
    sum = 0
    for i in args:  #funtion to sum any number of
        sum += i 	#parameters passed to a funtion
    return sum 		# the sum() take only 2 parameters

print(sumall(1,2,3,4))"""