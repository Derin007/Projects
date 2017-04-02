#for i in range(6, 1, -1):
#	for j in range(i, 1, -1):
#		print(" ", end="")
#	for k in range(i):
#		print("#", end="")
#	print("\n")

import sys
import string

for line in sys.stdin:

    a = line

    b = a[::-1]

    c = b.lower()

    d = string.capwords(c)

    print(d, end="")