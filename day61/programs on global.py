#Write a function that increments a global variable every time it is called.
x=7
def func():
    global x
    x+=1
    print(x)
    
func()
func()
func()

#Create a global list and append elements to it inside a function.
li=[1,2,3,4]
def update_list():
    li.append(5)
    print(li)
update_list()

#Write a program where a global variable is shadowed by a local variable with the same name.
x=5
def func():
    x=9
    print(x)
func()
print(x)

#Use a global variable inside two different functions and show how changes affect both.
x=7
def func1():
    b=9
    print(x+b)
def func2():
    c=4
    print(x-c)
func2()
func1()

#Write a program that uses a global counter across multiple function calls
counter=0
def increment():
    global counter
    counter+=1
    print(counter)
increment()
increment()