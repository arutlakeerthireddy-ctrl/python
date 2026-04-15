# implement arithmatic operation using functions
def arithmetic_op(func):
    def wrapper(*args,**kwargs):
        return func(*args,**kwargs)*2
    return wrapper

@arithmetic_op
def add(a,b):
    return a+b
@arithmetic_op
def sub(a,b):
    return a-b
@arithmetic_op
def multiply(a,b):
    return a*b
@arithmetic_op
def division(a,b):
    return a/b
a=int(input())
b=int(input())
print(add(a,b))
print(sub(a,b))
print(multiply(a,b))
print(division(a,b))

# check even or odd for the given number using functions
def even_odd(func):
    def wrap(n):
        result=func(n)
        return f"The number is {result}"
    return wrap
n=int(input('Enter number:'))
@even_odd
def number(n):
    if n%2==0:
        return 'even'
    else:
        return 'odd'
print(number(n))
    
'''Enter number:8
The number is even'''