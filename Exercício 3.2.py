def do_twice(a,b):
    a(b)
    a(b)

def print_twice(iury):
    print(iury)
    print(iury)

def do_four(otaku,iury):
    do_twice(otaku,iury)
    do_twice(otaku,iury)

do_twice(print,'spam')
print('')

do_four(print,'spam')