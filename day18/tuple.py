#creating a tuple
t=(1,2,3,4)
print(t)
#or
t=1,2,3,4
print(t)#(1,2,3,4)
#using tuple() constructor
t=tuple((1,2,3,4))
print(t)

#single element tuple
t=("keerthi")
print(type(t))#<class 'str'>

#must use comma
t=("keerthi",)
print(type(t))#<class 'tuple'>

#Accessing elements
t=(10,20,30)
print(t[0])#[10]
print(t[-1])#[30]

#slicing
print(t[0:])#[10,20,30]
print(t[:3])#[10,20,30]
print(t[0:2])#[10,20]

#looping through tuple
t=(1,2,3,4)
for i in t:
    print(i)

#tuple length
t=(5,6,9,2)
print(len(t))#4

#Tuple methods(only 2)
t=(1,2,3,3,4)
print(t.count(3))#2
print(t.index(4))#4

#Tuple packing
t="keerthi",21,"hyd"

#unpacking
(a,b,c)=t
print(a)
print(b)
print(c)

#nested tuple
t=(1,3,(2,5))
print(t[2][0])#2

#concatenation
t1=(1,2,3)
t2=(4,5,6)
print(t1+t2)#(1,2,3,4,5,6)

#repetition
t1=(1,2,3)
print(t1*2)#(1, 2, 3, 1, 2, 3)

#converting list to tuple
li=[10,20,30]
print(tuple(li))#(10,20,30)

#tuple as a dictionary key
d={(1,2):'keerthi'}
print(d[(1,2)])#keerthi


