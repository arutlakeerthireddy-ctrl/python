#Write a program to remove duplicates from a list.
li=list(map(int,input("Enter numbers:").split()))
unique=[]
for i in li:
    if i not in unique:
        unique.append(i)
print(unique)