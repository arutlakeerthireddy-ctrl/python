#Repeat tuple ("Hi",) four times.
t=("Hi",)
print(t*4)#('Hi', 'Hi', 'Hi', 'Hi')

#Check whether 20 exists in (10, 20, 30, 40).
t=(10, 20, 30, 40)
print(20 in t)#True

#Compare (1,2,3) and (1,2,4) using comparison operators.
t1=(1,2,3)
t2=(1,2,4)
print(t1==t2)#False
print(t1!=t2)#True
print(t1>t2)#False
print(t1<t2)#True
print(t1>=t2)#False
print(t1<=t2)#True

#Multiply all elements in t = (1,2,3,4) using a built-in function.
t=(1,2,3,4)
print(t[0]*t[1]*t[2]*t[3])#24


#Find the index of 30 in (10,20,30,40).
t=(10,20,30,40)
print(t.index(30))#2

#Join words in ("I","Love","Python") into a single string.
t=("I","Love","Python") 
print(" ".join(t))#I Love Python

