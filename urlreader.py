#import urllib
from six.moves.urllib.request import urlopen


"""conn = urllib.urlopen('http://thinkpython.com/secret.html')
for line in conn.fp:
	print(line.strip())"""

link = 'http://thinkpython.com/secret.html'
f = urlopen(link)
myfile = f.read()
print(myfile)