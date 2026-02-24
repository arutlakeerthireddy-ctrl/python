#control statements:are used to control the flow of execution of a program
#control statements are three types:
#1.conditional statements
#2.looping statements
#3.jumping statements

#conditional statements:used for decision making
#these statements execute code based on condition

#if statement:executes block if condition is True
# syntax:
#if condition:
 #   statement

#example:
age=18
if age>=18:
    print("eligible to vote")

#if-else statements:executes one block if True,another if False
#syntax:
"""if condition:
    statement1
else:
    statement2"""

#example:
num=20
if num%2==0:
    print("even")
else:
    print("odd")

#if-elif-else statement:used when checking multiple conditions
#syntax:
"""if condition1:
    statement1
elif condition2:
    statement2
elif condition3:
    statement3
else:
    statement4"""

#example:
marks=85
if marks>=90:
    print("A grade")
elif marks>=75:
    print("B grade")
elif marks>=50:
    print("C grade")
else:
    print("Fail")

#Nested if(if inside if)
#used when we want to check condition inside another condition
#syntax:
"""if condition1:
    if condition2:
        statement"""

#Example:
age=20
citizen=True
if age>=18:
    if citizen==True:
        print("Eligible to vote")

    
   
     
