fin = open('another1.txt')
print(fin)
a = sum(1 for _ in fin)
b = 0
while b < a:
	c = fin.readline()
	#print(c)
	b += 1
"""for line in fin:
	word = line.strip()
	if len(word) > 8:
		print(word)"""
#for line in fin:
#print(fin.read())
"""line = fin.readline()
word = line.replace('a', '')
print(word)"""

	#a = len(word)
	#print(a)
	
	#print(word)

"""def has_no_e(s):
	#b = 0
	c = []
	for word in s:
		c = word
		if 'e'  in c:
			#print(word, end="")
			print("Word contains the letter 'e'")
		#else:
		#	print(word, end="")
			#print("Word contains the letter 'e'", end="")

has_no_e("Ade")"""

"""def avoids(w, s):
	b = 0
	a = []
	words = []
	words = w
	letters = []
	letters = s
	for i in words:
		while i <= words[:-1]:
			i[]
			for j in i:
				unitword = words.strip()
	#for i in unitword:
				if letters in unitword:
					print("Contains Word")
				else:
					print(letters)
			b = b + 1
		#else:
		#	return -1

print(avoids("Adebakin", "a"), end="")"""

"""def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	return True

#print(has_no_e("bellerin"))

def uses_only(word, available):
	for letter in word:
		if letter not in available:
			return False
	return True

#print(uses_only("floeace", "acefhlo"))

def uses_all(word, required):
	return uses_only(required, word)
	#""for letter in required:
	#	if letter not in word:
	#		return False
	#return True"""
#print(uses_all("aeioucdym", "bf"))"""

def avoids(word, letter):
	for i in word:
		if letter not in word:
			return True
	return False

#print(avoids("bellerin", "n"))

"""def is_abecedarin(word):
	previous = word[0]
	for c in word:
		if c < previous:
			return False
		previous = c
	return True"""

"""def is_abecedarin(word):
	if len(word) <= 1:
		return True
	if word[0] > word[1]:
		return False
	return is_abecedarin(word[1:])"""

"""def is_abecedarin(word):
	i = 0
	while i < len(word) - 1:
		if word[i + 1] < word[i]:
			return False
		i += 1
	return True

print(is_abecedarin("aabbccadddeeegghikloo"))"""

"""def is_palindrome(word):
	i = 0
	j = len(word) - 1

	while i < j:
		if word[i] != word[j]:
			return False
		i += 1
		j -= 1

	return True

print(is_palindrome("door"))"""

"""def cartalk(word):
	for a in word:
		i = 0
		if a[i] == a[i + 1]:
			b = a[i]
			i += 1
			return cartalk(word[1:])

print(cartalk("aabbccdd"))"""


#def is_triple_double(word):
   # return True if the word contains three consecutive
    #double letters.

	#i = 0
#	count = 0
#    while i < len(word)-1:
 #       if word[i] == word[i+1]:
  #          count = count + 1
   #         if count == 3:
    #            return True
     #       i = i + 2
      #  else:
       #     count = 0
        #    i = i + 1
#    return False


"""def find_triple_double():
    fin = open('words.txt')
    fin1 = fin.read()
    for line in fin1:
        word = line.strip()
        if is_triple_double(word):
            print (word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
print(find_triple_double())"""



#def has_palindrome(i, start, len):
"""return True if the integer i, when written as a string,
    contains a palindrome with length (len), starting at index (start).
    """
 #   s = str(i)[start:start+len]
  #  return s[::-1] == s
    
#def check(i):
"""check whether the integer (i) has the properties described
    in the puzzler
    """
 #   return (has_palindrome(i, 2, 4)   and
  #          has_palindrome(i+1, 1, 5) and
   #         has_palindrome(i+2, 1, 4) and
#            has_palindrome(i+3, 0, 6))

#def check_all():
"""enumerate the six-digit numbers and print any that satisfy the
    requirements of the puzzler"""

 #   i = 100000
  #  while i <= 999999:
   #     if check(i):
    #        print (i)
     #   i = i + 1

#print ('The following are the possible odometer readings:')
#print(check_all())


def str_fill(i, len):
    """return the integer (i) written as a string with at least
    (len) digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """ return True if the integers i and j, written as strings,
    are the reverse of each other"""
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details."""
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count = count + 1
            if flag:
                print (daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count
    

def check_diffs():
    """enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other."""
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print (diff, n)
        diff = diff + 1

"""print ('diff  #instances')
print(check_diffs())
print ('daughter  mother')
print(num_instances(18, True))"""