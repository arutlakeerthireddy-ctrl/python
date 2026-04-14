#Create a decorator that prints "Start" before a function and "End" after it.
def decorator(func):
    def wrap(*args,**kwargs):
        print("start")
        result=func(*args,**kwargs)
        print("end")
        return result
    return wrap
@decorator             #start
def sub(a,b):          #end  
    return a-b         #5
print(sub(7,2))

#Create a decorator that returns the sum of all arguments passed to the function
def deco(func):
    def wrapper(*args,**kwargs):
        result=func(*args,**kwargs)
        return result
    return wrapper
@deco
def add(*args):
    return sum(args)
print(add(1,2,3,4))