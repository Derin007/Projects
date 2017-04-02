def getUniqueItems(iterable):
    seen = set()
    result = []
    for item in iterable:
        if item not in seen:
            seen.add(item)
            result.append(item)
    a = str(result)
    return a
 
a = open('test.txt')
b = a.read()
c = b.strip()
d = c.split()
#print(d)
#d = tuple(c)
e = d[::-1]
#f = string.capwords(e)
g = list(c)
h = g.sort()
#print(g)
#f = 0
#print(len(d))
#while f < len(d):
#		g = str("".join(d[f]))
#	print(g)
#	f += 1
#if f < len()
#e = str("".join(d))
#print(e)
#a = ["asd","def","ase","dfg","asd","def","dfg"]
print (getUniqueItems(d))



"""a = ["asd","def","ase","dfg","asd","def","dfg"]
b = list(set(a))
seen = set()
result = []
for item in a:
    if item not in seen:
        seen.add(item)
        result.append(item)"""


"""import string

a = open('test.txt')
b = a.readline()
c = b.strip()
e = list(c[:])
f = str("".join(e))
g = f[::-1]
h = string.capwords(g)
print(h)
d = ["".join(word) for line in c for word in line.split() if word not in c]"""
#print(d)


"""a = open('test.txt')
b = a.read()
c = b.strip()
d = 0
e = ""
while c == True:
	for i in c:
		if i != c[d]:
			c[d] = i
			e = c[d]
			#print(e)


def find(word, index):
	#index = 0
	result = ""
	letter = " "
	while index < len(word):
		if word[index] == letter:
			#return index
			result = result
		else:
			result += letter
		print(result)
		index = index + 1

	#return -1

print(find(c, 0))"""
		#print(c, end="")
#if c[d] 





"""def unique(words):
	result = ""
	for word in words:
		a = 0
		i = ""
		if i not in word:
			#i = i + i[a]
			result = result + " " + i
		return result
	return result

print(unique("I am not a robot \n I am a human"), end="")"""


"""word_list = "I am not a robot I am a human"
unique_words = set(word_list)
for word in unique_words:
    #file.write(str(word) + "\n")
    a = str(word)
    print (a, end="")"""

a = open('test.txt')
b = a.read()
e = b.strip()
#print(e)
#e = list(b)
c = []
d = 0
for line in e:
	for word in line:
		x = ''
		j = [x for i in word if x in word and x not in i]
		#print(j)
		#h = " ".join(word)
		#print(h, end="")
		#f = "".join(word)
		#while f[h] == " ":   # or "\n":
		#	g = "".join(f)
		#	print(g, end="")
		#	h += 1
		#while int(word[d]) < len(line) - 1:
			#print(d)
			#c[d] += word
			#word = 
			#d += 1
		#print(c)
		#if word not in c:
		#	a = 0
			#c += word
			#c[d] += word
		
			#c = c + " " + word
		#print(c, end="")
	#print(line, end="")
#print(c, end="")
