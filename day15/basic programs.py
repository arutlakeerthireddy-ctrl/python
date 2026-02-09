#Write a program to create a list and print all elements.
li=[2,3,4,5,6]
print(li)

#Write a program to find the length of a list.
li=[2,3,4,5,6]
print(len(li))#5

#Write a program to access the first and last elements of a list.
li=[2,3,4,5,6]
print(li[0])#2
print(li[-1])#6

#Write a program to print elements at even index positions.
li=[2,3,4,5,6]
print(li[0::2])#[2,4,6]

#Write a program to print elements at odd index positions.
li=[2,3,4,5,6]
print(li[1::2])#[3,5]

#Write a program to check whether a list is empty or not.
li=[]
if len(li)==0:
    print("list is empty")
else:
    print("list is not empty")