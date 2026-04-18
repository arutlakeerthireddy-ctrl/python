#preserving function metadata
#Functions in Python has metadata that can be accessed using the __name__ and __doc__ attributes
def func():
    return 'have a great day'
print(func.__name__) #func

#when the function is decorated the metadata of original function is lost

def deco(func):
    def wrap():
        return func().upper()
    return wrap
@deco
def changecase():
    return 'hi keer'
print(changecase.__name__)#wrap

#to fix this python has builtin function called functools.wraps that can be used to preserve original functions name and docstring
import functools
def deco(func):
    @functools.wraps(func)
    def wrap():
        return func().upper()
    return wrap
@deco
def changecase():
    return 'hi keer'
print(changecase.__name__)
#changecase
