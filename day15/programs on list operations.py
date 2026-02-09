#Write a program to add an element to a list.
li=[1,4,7,9]
li.append(8)
print(li)#[1,4,7,9,8]

#Write a program to insert an element at a specific position.
li=[1,4,7,9]
li.insert(1,2)
print(li)#[1,2,4,7,9]

#Write a program to remove a specific element from a list.
li=[1,4,7,9]
li.remove(7)
print(li)#[1,4,9]

#Write a program to remove all occurrences of an element.
li=[1,4,7,4,9,4]
x=4
while x in li:
    li.remove(x)
print(li)#[1,7,9]

#Write a program to copy one list into another.
l1=[1,4,7,9]
l2=l1.copy()
print(l2)#[1,4,7,9]

#Write a program to clear all elements from a list.
li=[1,4,7,9]
li.clear()
print(li)#[]