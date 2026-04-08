#Write a program using the len() function on different data types.
li=[1,2,4,5,6]
s='keerthi'
t=(4,57657,46,77,8,9)
def func():
    return len(li)
def func1():
    return len(s)
def func2():
    return len(t)
print(func())
print(func1())
print(func2())

#Use the type() function to print the type of various variables.
x=9
s='hi'
f=6.9
li=[3,4,5]
def func():
    print(type(x))
    print(type(s))
    print(type(f))
    print(type(li))
func()

#What will max([3, 7, 2, 9]) return? Try with strings also.
def maximum(a,b,c,d):
    return max(a,b,c,d)
print(maximum(3,7,2,9))

s=['hi','abc','wow']
def strings():
    return max(s)
print(strings())

#Use sum() to add elements of a list.
li=[10,3,56,90]
def add_list():
    return sum(li)
print(add_list())