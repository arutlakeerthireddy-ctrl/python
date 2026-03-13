#Write a program to find the smallest number in a list using nested loops.
li=[2,4,5,1,4]
for i in range(len(li)):
    small=True
    for j in range(len(li)):
        if li[j]<li[i]:
            small=False
    if small==True:
        print(li[i])

#Write a program to check if a list contains duplicate values.
li=[1,2,3,3,1,4]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[j]==li[i]:
            duplicate=True
if duplicate==True:
    print("contains duplicate values")
else:
    print("not")

            
