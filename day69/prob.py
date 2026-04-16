'''You have two decorators:
One converts text to uppercase
One adds "!!!" at the end
If applied together, what should be the final output for "hello"?'''

def change_case(func):
    def wrapper():
        return func().upper()
    return wrapper
def add(func):
    def wrapper():
        return func()+"!!!"
    return wrapper
@change_case
@add
def greet():
    return 'hello'
print(greet())
#HELLO!!!

'''One decorator adds "Start-" and another adds "-End"
 What will be the output for "Python"?'''
def deco1(func):
    def wrap():
        return "start-"+func()
    return wrap
def deco2(func):
    def wrap():
        return func()+"-End"
    return wrap
@deco1
@deco2
def func1():
    return 'Python'
print(func1())