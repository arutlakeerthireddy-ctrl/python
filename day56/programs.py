#Positional Arguments 
#Write a function to add two numbers using positional arguments.
def add(a,b):
    return a+b  #7
print(add(0,7))

#Create a function that prints name and age using positional arguments.
def student(name,age):
    return name,age  #('keerthi', 21)
print(student("keerthi",21))

#Write a function to find the maximum of three numbers using positional arguments.
def maximum(a,b,c):
    return max(a,b,c)  #9
print(maximum(2,9,7))

#Create a function that swaps two values passed as positional arguments.
def swaps(a,b):
    a,b=b,a
    return a,b  #5,4
print(swaps(4,5))