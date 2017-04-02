"""def countdown(n):
	if n <= 0:
		print("Blast Off!")
	else:
		print(n)
		countdown(n-1)

countdown(10)
"""
def do_n(f, arg):
	if arg <= 0:
		print("The End")
	else:
		print(f, arg)
		do_n(f, arg-1)

print("Enter a number below: ")
a = int(input())
do_n("Hey there!", a)