#default arguments
#arguments that have predefined arguments,used when no value is provided
# example
def data(a="guest"):
    print(a)
data()  #guest
data("hlo") #hlo

def clg(name="gnit"):
    print("hlo",name)
clg()  #hlo gnit
clg("gni")  #hlo gni

#Write a function to add two numbers where the second number has a default value of 10.
def add(a,b=10):
    print(a+b) #18
add(8)
add(5,0) #5

#Write a function to calculate the square of a number using a default exponent.
def square(n=10):
    return n*n
print(square())
print(square(2))
print(square(6))

#Create a function that prints a student's name and default course as "B.Tech".
def student(name,course="B.Tech"):
    print(name,course)
student("keerthi")
student("uma","gni")
student(1,2)

#Create a function that prints a student's name and default course as "B.Tech".
def student(name,course="B.Tech"):
    print(name,course)
student("keerthi")

#What will happen if you define a function with a default argument and pass None as a value?
def fun(a=0):
    return a
print(fun(None)) #None 

#Write a function where one parameter is mandatory and two have default values.
def func(c,a=0,b=0):
    return a-b-c #0
print(func(3))

#Create a function to append elements to a list using a default list argument
def list(li=None):
    if li is None:
        li=[1,2,3]
    li.append(10)
    return li  #[1, 2, 3, 10]
print(list())
    
#never use list,dict,set as default arguments
#use None+if condition