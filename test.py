#mylist = ['a', 'b', 'c', 'd', 'e']

#print(mylist[:4])
#count1, count2, count3 = 0
for i in range(1, 100, 1):
	if i % 3 == 0:
		if (i % 3 == 0) and (i % 5 == 0):
			print("FizzBuzz")
			#count1+1
		print("Fizz")
		#count2+1
	elif i % 5 == 0:
		if (i % 3 == 0) and (i % 5 == 0):
			print("FizzBuzz")
			#count1+1
		print("Buzz")
		#count3+1
	else:
		print(i)
"""print("FizzBuzz was printed: ", count1, "times")
print("Buzz was printed: ", count3, "times")
print("Fizz was printed: ", count2, "times")"""