#what is python scope?
#python scope is the region or area of a program where a variable recognized and can be accessed
#scope means where a variable can be used in code
def fun():
    x=9
    print(x) #local scope
fun()

#Types of python Scope(LEGB rule)
#L-local
#E-enclosing
#G-global
#B-builtin

#local scope
#variables created inside a function
#can be used only inside that function
#example
def func():
    x=8 #local
    print(x)  
func()
#print(x) #wrong

#Enclosing scope
#happens in nested function(function inside a function)
#inner function can access outer function variable
#example
def outer():
    x=30 #enclosing variable
    def inner():
        print(x)
    inner()
outer()

#modifying enclosing variable-use nonlocal
def outer():
    x=20
    def inner():
        nonlocal x
        x=90
        print(x)
    inner()
    #print(x) #90
outer()
#nonlocal keyword-Used to modify variable from enclosing scope