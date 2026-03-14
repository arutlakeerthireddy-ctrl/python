#Write a program to remove duplicate elements from a list using nested loops.
li=[1,2,3,3,4,4]
for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            li.remove(li[j])
            break
print(li)

#Write a program to count how many times each element appears in a list.
li=[1,1,2,3,4,5]

freq={}
for i in range(len(li)):
    count=0
    for j in range(i+1,len(li)):
        if li[i]==li[j]:
            count+=1
        freq[li[j]]=count
print(freq)

