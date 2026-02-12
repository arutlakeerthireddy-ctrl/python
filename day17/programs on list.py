#Print all elements in reverse order.
li=[1,2,3,4,5]
for i in range(len(li)-1,-1,-1):
    print(li[i])

#using slicing
li=[1,2,3,4,5]
for i in li[::-1]:
    print(i)