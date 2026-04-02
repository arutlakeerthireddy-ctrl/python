#Global scope
#variables created outside all functions
x=10 #global variable
def func():
    print(x)
func()

#modify global variable-use global
x=20
def func():
    global x
    x=9
    print(x)
func()

#builtin scope
#predefined names in python
#available everywhere
#examples
#print(),len(),sum()
def func(*args):
    return len(args)
print(func(1,3,2,4))



