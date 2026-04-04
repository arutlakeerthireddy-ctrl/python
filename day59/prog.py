#Write a function that creates a variable inside it and try accessing it outside the function.
def func():
    x=7
    return x
print(func())

def func():
    global x
    x=4
func()
print(x)
