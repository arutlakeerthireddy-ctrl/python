#Write a program to find common elements between two lists.
li1=[1,2,3,4]
li2=[3,4,5]
li=[]
for i in range(len(li1)):
    for j in range(len(li2)):
        if li1[i]==li2[j]:
            li.append(li2[j])
print(li)
