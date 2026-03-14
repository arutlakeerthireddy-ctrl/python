#Write a program to print elements that are present in the first list but not in the second list.
li1=[1,2,3,4]
li2=[3,4,5,6]
li=[]
for i in li1:
    found=False
    for j in li2:
        if i==j:
            found=True
            break
    if not found:
        li.append(i)
print(li)

