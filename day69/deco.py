#multiple decorator calls
def decorator(func):
    def wrapper():
        return func().upper()
    return wrapper
@decorator
def func1():
    return 'hii keer'
@decorator
def func2():
    return 'hlo uma'
print(func1())
print(func2())