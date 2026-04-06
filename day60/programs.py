#programs on enclosing scope
#Write a function where an inner function prints a variable from the enclosing function.
def outer():
    x=9
    def inner():
        print(x)
    inner()
outer()

#Create a nested function where the inner function modifies an enclosing variable using nonlocal.
def outer():
    x=70
    def inner():
        nonlocal x
        x=50
        print(x)
    inner()
outer()

#Write a program where an inner function tries to modify an enclosing variable without using nonlocal. What happens?
def outer():
    x=90
    def inner():
        x=60
        print(x)
    inner()
outer()

#Define a variable in an outer function and access it inside two different inner functions.
def outer():
    x=34
    def inner1():
        print(x)
        def inner2():
            print(x)
        inner2()
    inner1()
outer()

#Write a nested function where the inner function shadows the enclosing variable.
def outer():
    x=9
    def inner():
        x=10
        print("inner:",x)
    inner()
    print('outer:',x)
outer()