#How to count lines in a text document or file

a = open('test.txt')
b = sum(1 for _ in a)
print(b)