#Write a program to sort a list in ascending order using nested loops (like simple sorting).
li=[4,2,8,9,5,7]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
            
print(li)

#Write a program to sort a list in descending order using nested loops.

li=[4,2,8,9,5,7]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]<li[j]:
            li[i],li[j]=li[j],li[i]
            
print(li)
