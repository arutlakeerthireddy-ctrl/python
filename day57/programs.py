#Default + Mixed Arguments
#Write a function with one default argument and one positional argument.
def func(a,name="keerthi"):
    return a,name
print(func(7))
print(func(7,"uma"))

#Create a function that greets a user with a default name if no name is provided.
def greet(name='raji'):
    return 'hlo',name
print(greet())
print(greet("keer"))

#Write a function to calculate power (base, exponent=2).
def cal_power(base,exponent=2):
    return base**exponent
print(cal_power(10))

#Create a function that takes 3 arguments (one default, two required).
def func(a,b,c=7):
    return a+b-c
print(func(1,9))
print(func(4,7,3))