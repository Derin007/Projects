"""def cumulative_sum(l):
	temp = 0
	result = []
	for i in l:
		temp += i
		result.append(temp)
	return result
l = [1, 2, 3, 4, 5, 6, 7]
print(cumulative_sum(l))"""

"""def chop(l):
	#a = del( l[0])
	a = l
	a.pop(0)
	a.pop(-1)
	#b = a.append(10)
	#b = a.pop(1) # l[0]
	#c = b.pop(7) # a[-1]
	print(a)
l = [1, 2, 3, 4, 5, 6, 7]
#print(chop(l))


def middle(l):
	chop(l)
print(middle(l))"""

"""def is_sorted(l):
	a = 0
	while a < len(l) - 1:
		for i in l:
			if l[i] <= l[i + 1]:
				j = 0
				#i += 1
			else:
				return False
		a += 1
	return True
l = [1, 2, 3, 4, 5, 6, 7]
print(is_sorted(l), end="")"""

"""def anagrams(s1, s2):
	a = 0
	while a < len(s1):
		for i in s2:
			if i in s1:
				continue
				#b = 0
			else:
				return False
		a += 1
	return True

a = "aderinsola"
b = "alosnireda"
print(anagrams(a,b), end="")"""



















