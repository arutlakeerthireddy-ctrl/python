#membership operator
Membership operators are used to check whether a value exists in a sequence 
like list, tuple, set, string, or dictionary.
#operators
in - returns True if the value is present 
not in - returns True if the value is not present.

#programs

#1.program to check if a character 'a' exists in the string "apple".
s="apple"
print("a" in s)#True

#2.Check whether "py" is not in the string "python".
s="python"
print("py" not in s)#False

#3.verify if the value 100 exists in a tuple (10, 20, 30, 40).
t=(10,20,30,40)
print(100 in t)#False

#4.Check whether the key "age" exists in the dictionary {"name": "Ravi", "age": 21}.
d={"name": "Ravi", "age": 21}
print("age"in d)#True

#5.Find whether 15 is not present in the set {5, 10, 20, 25}
s={5, 10, 20, 25}
print(15 not in s)#True

#6.Write a program to check if a number entered by the user exists in a predefined list.
num=int(input("Enter number:"))#14
li=[9,14,15]
print(num in li)#True

#7.You are validating a login system. How will you check whether a username
#  exists in a list of registered users?
reg_users=["keerthi","pavani","mallika"]
a=input("Enter username:")#pavani
print(a in reg_users)#True

#8.In an email validation program, 
# how do you verify that "@" and "." are present in the email string?
s="keerthireddy@gmail.com"
print("@" and "." in s)

#9 In a banking application, 
# how can you verify whether an account number exists in the database list?
li=[1001,1002,1003,1004]
num=1003
print(num in li)#True

#10.While reading user input, 
# how do you ensure the entered value is not in the list of restricted values?
li=[0,-1,-99]
value=int(input("Enter value:"))#10
print(value not in li)#True






