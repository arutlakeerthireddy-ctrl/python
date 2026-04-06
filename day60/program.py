#Create three nested functions and print a variable from the nearest enclosing scope.
def outer():
    x=89
    def inner1():
        x=20
        def inner2():
            print(x)
        inner2()
    inner1()
outer()

#Write a function where the inner function returns a value using an enclosing variable.
def outer():
    x=9
    def inner():
        return x
    print(inner())
outer()


#Create a closure that stores a number and returns a function to add another number to it.
def func():
    x=10
    def add(y):
        return x+y
    print(add(5))
func()

#Write a function where multiple inner functions modify the same enclosing variable using nonlocal.
def outer():
    x=70
    def inner1():
        nonlocal x
        x=90
        print('inner1:',x)
    def inner2():
        nonlocal x
        x=80
        print('inner2:',x)
    inner2()
    inner1()
outer()

#Create a counter function using enclosing scope that increments each time it is called.
def counter():
    x=8
    def counter1():
        nonlocal x
        x+=1
        print(x)
    return counter1
    
c=counter()
c()
c()
c()