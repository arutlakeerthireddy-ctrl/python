#Write a function that creates a local variable and prints it.
def func():
    x=9
    print(x)
func()

#Write a function that takes two numbers and prints their sum using local variables.
def add(a,b):
    result=a+b
    print(result)
add(6,9)

#Write a function where a variable is created inside a loop and printed outside the loop but inside the function.
def func():
    for i in range(1,10):
        x=i
    print(x)
func()
     