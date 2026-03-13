#Write a program to print all pairs of elements from a list.
li=[1,2,3]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        print(li[i],li[j])

#Write a program to count how many duplicate elements are present in a list.
li=[1,1,2,3,2,4]
count=0
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            count+=1
print(count)
