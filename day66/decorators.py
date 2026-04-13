#what is decorator
#decorator is the function that modifies or extends the behaviour of another function without changing its code
# decorator=wrapper function
def decorator(func):
    def wrapper():
        print('before function')
        func()
        print('after function')
    return wrapper
@decorator
def greet():
    print('hlo')
greet()

#why do we use decorators?
#avoid repeating code
#add extra functionality
#keep code clean

#types of decorator
#function decorator:it is normal function that takes another func as input and returns new function(wrapper)
def changecase(func):
    def inner():
        return func().upper()
    return inner
@changecase
def my_func():
    return 'keerthi'
print(my_func())
#If decorator uses .upper(), .lower(), math, etc., the function must return a value