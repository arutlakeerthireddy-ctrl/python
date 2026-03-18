#Write a program to count the number of equal pairs (i, j) in a list
#  where i < j and list[i] == list[j].
li=[1,2,3,4,5,2,3,4]
count=0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            count+=1
print(count)
