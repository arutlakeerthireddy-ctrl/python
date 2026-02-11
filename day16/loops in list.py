#looping in list
Looping in a list means accessing each element of the list one by one 
to perform some operation (like printing, checking conditions, calculating sum, etc.).

*A list can contain multiple values, and looping helps us avoid writing the same code again and again.

#Types of looping in a list
#using for loop
li=[1,2,3,4,5]
for i in li:
    print(i)

#using index(range+len)
li = [10, 20, 30]
for i in range(len(li)):
    print(li[i])

#using enumerate()
li = [10, 20, 30]

for index, value in enumerate(li):
    print(index, value)
