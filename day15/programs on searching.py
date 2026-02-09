#Searching & Checking
#Write a program to check if an element exists in a list.
li=[2,3,4,5,6]
print(3 in li)#True

#Write a program to find the index of an element.
li=[2,3,4,5,6]
print(li.index(5))#3

#Write a program to count occurrences of an element in a list.
li=[2,3,4,2,5,6]
print(li.count(2))#2

#Write a program to find the largest element in a list.
li=[2,3,4,5,6]
print(max(li))#6

#Write a program to find the smallest element in a list.
li=[2,3,4,5,6]
print(min(li))#2

#Write a program to find the second largest element in a list.
li=[2,3,4,1,5,]
li.sort()
print(li[-2])#4