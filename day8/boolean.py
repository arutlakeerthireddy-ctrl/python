#what is boolean in python
In Python, a boolean data type is a built-in data type that can hold two possible values: 
True 
False
it is mainly used for decision making and comparisons.
    
#Boolean data type
Boolean datatype is called bool in Python.
True and False must start with a capital letter.
#Example of boolean in python
a = True
b = False
print(type(a))  # Output: <class 'bool'>
print(type(b))  # Output: <class 'bool'>

#How booleans are used
booleans are commonly used in :
1. Conditional Statements:
2. Loops
3. Comparisons

#Boolean from comparisons
booleans are often the result of comaprison operators
#ex:
x=2
y=8
print(x>=y)#False
print(x==y)#False
print(x<=y)#True

#Boolean with logical operators
Logical operators work with boolean values
and:True if both conditions are True
or:True if atleast one condition is True
not:reverse the result
#ex:
print(True and True)#True
print(True or False)#True
print(not True)#False

#Boolean in conditional statements
Booleans is mainly used in if else conditions
#ex:
age=18
if age>=18:
    print("Eligible to vote")#True
else:
    print("Not eligible")    

#Truthy and Falsy values
some values are treated as false automatically
#0
#none
#""
#[],{},()
everything else is treated as True

#ex:
print(bool(0))#False
print(bool("hi"))#True







