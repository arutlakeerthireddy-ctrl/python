#what is list?
list is a built in datatype used to store multiple values in a single variable
Lists are written using square brackets [ ]
ex:
my_list=[1,2,3,4]

#characteristics:
1.They are ordered (each item has an index starting from 0)
2.Lists are mutable (you can change, add, or remove elements)
3.allow duplicates
4.allow indexing
5.They can store different data types (int, float, string, boolean, etc)

#creating list
a=[] #empty list
a=[2,3,4]
a=list((6,8,9)) #using list constructor

#Accessing list elements(indexing)
list=[3,4,9,0,4]
print(list[0]) #3
print(list[-1]) #4
print(list[2]) #9

#slicing a list
list=[3,4,9,0,4]
print(list[:4])#[3,4,9,0,4]
print(list[0:])#[3,4,9,0,4]
print(list[1:4])#[4,9,0,4]

#modifying a list(mutability)
list=[10,20,30,50]
list[1]=22
print(list)#[10,22,30,50]

#Adding elements
li=[1,2]
li.append(3) #add element at end
li.insert(0,5) #add at index
li.extend([4,5]) #add multiple elements

