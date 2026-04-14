#decorators with arguments:decorators that can handle functions which take parameters
def my_function(func):
    def wrapper(*args,**kwargs):
        print('before')
        result=func(*args,**kwargs)
        print('after')
        return result
    return wrapper
@my_function
def add(a,b):
    return a+b
print(add(5,6))



