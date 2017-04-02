a = "Hello my name is Derin"

def do_twice(f):
    f()
    f()

def print_spam(a):
    print(a)

do_twice(print_spam)