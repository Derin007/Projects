def rotate_word(s, i):
	Result = ''
	for c in s:
		a = ord(c)
		if a >= ord('a') and a <= ord('z'):
			if a > ord('m'):
				a -= i
			else:
				a += i
		if a >= ord('A') and a <= ord('Z'):
			if a > ord('M'):
				a -= i
			else:
				a += i
		Result += chr(a)
	return Result

print(rotate_word("cheer", 7), end="")
