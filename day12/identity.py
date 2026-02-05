#identity operators
identity operators used to compare memory locations of two objects(not values)
#operators
is-returns True if both variables are point to same object
is not-returns True if both variables point  to different object

#programs
#1.Create two variables pointing to the same list and check is.
l1=[1,2,3,4]
l2=l1
print(l2 is l1)#True

#2.Create two identical lists separately and check is
l1=[4,5,6,7]
l2=[4,5,6,7]
print(l2 is l1)#False

#3.Check whether two integer variables with the same value use the same identity.
a=int(input("Enter num1:"))#5
b=int(input("Enter num2:"))#5
print(a is b)#True

#4.Compare two strings using is and observe the result.
s1="hii"
s2="hii"
print(s1 is s2)#True

#5.Write a program using is not with two different objects.
a=12
b=45
print(a is not b)#True

#6.Check identity of two empty lists.
l1=[ ]
l2=[ ]
print(l1 is l2)#False



