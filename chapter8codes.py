"""def reverse(a):
	while a:
	#for i in a:
		if a != " ":
			b = a[::-1]
			print("Reversed string is: ", b)
			if b == a:
				print("Works")
			else:
				print("Bummer!")
		return 

reverse("roor")"""

"""prefixes = 'JKLMNOPQ'
suffix = 'ack'
#i = 0
for letter in prefixes:
	if letter == 'O':
		letter = letter + 'u'
		print(letter + suffix)
	elif letter == 'Q':
		letter = letter + 'u'
		print(letter + suffix)
	else:
		print(letter + suffix)
	#i = i + 1
	"""

"""a = "fruit"
print(a[:])"""

def find(word, letter, index):
	#index = 0
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return -1

print(find("aderinsola", "a", 0))

"""def count(word, letter):
	count = 0
	a = []
	b = 0
	for a in word:
		if letter == a[b]:
			count = count + 1
	print(count, end="")

count("abracadabra", "a")"""

"""def count(word, letter):
	count = 0
	a = []
	b = 0
	#c = b
	for a in word:
		if letter == a[b]:
			count = count + 1
	print(count, end="")

count("abracadabra", "a")"""

"""def count(word, letter):
	count = 0
	a = []
	b = 0
	#c = 0
	#while c <= b:
	#while word != " ":
	#	c = 0
	for a in word:
		if letter == a[b]:
			count = count + 1
		#c = c + 1
	print(count, end="")
	#c = c + 1

count("abracadabra", "a")"""

"""a = "rood"
b = []
while a:
	c = 0
	for i in a:
		if a != " ":
			b = a[::-1]
			print(b, end="")
		break
	c = c + 1"""
	#print(a)
	#b = a[::-1]
	#print(b)
"""if b == a:
	print("Works!")
else:
	print("Ouch! That sucks!")"""


"""def any_lowercase(s):
	for c in s:
		if c.islower():
			#b = c
			return True	#if lowercase in the middle, this doesn't
		else:			#perform as it should
			return False

def any_lowercase2(s):
	for c in s:
		if 'c'.islower():
			return 'True'
		else:
			return 'False'

def any_lowercase3(s):
		for c in s:
			flag = c.islower()
		return flag

def any_lowercase4(s):
	flag = False
	for c in s:
		flag = flag or c.islower()
	return flag

def any_lowercase5(s):
	for c in s:
		if not c.islower():
			return False		#This works well!
	return True


#print(any_lowercase2("ADERINSOLA"))


def rotate_word(s, i):
	holder = ""
	for v in s:
		c = ord(v)
		if c >= ord('a') and c <= ord('z'):
			if c > ord('m'):
				c -= i
			else:
				c += i
		elif c >= ord('A') and c <= ord('Z'):
			if c > ord ('M'):
				c -= i
			else:
				c += i
		holder += chr(c)
	return holder

print(rotate_word("The Quick Brown Fox Jumps Over The Lazy Dog", 13))"""







