#Write a program to compare two lists and check if they contain the same elements.
li1=[1,2,3,4]
li2=[3,4,5]
flag=False
for i in range(len(li1)):
    for j in range(len(li2)):
        if li1[i]==li2[j]:
            flag=True
if flag==True:
    print("contain same elements")
        
