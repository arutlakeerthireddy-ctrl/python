#function:is a reusable block of code that performs specific task
#why do we use?
#without functions:we write same code again and again
#with functions:write once-use many times

'''#syntax
def function_name(parameters):
    #code
    return result'''

#example
def add(a,b):
    result=a+b
    return result
print(add(2,3)) #call function

#types of functions
#buitin functions:print(),len(),sum()
#user defined functions:created by you
def greet(): #function without return
    print("hlo")
 
#function with return
def square(n):
    return n*n

#function with arguments
def add(a,b):
    return a+b

#function without arguments
def hlo():
    print("hlo")

#call functions:function will not run until u calls it
def greet():
    print("hlo")
greet()  #calling




