#Write a program to find the second largest element in a list using nested loops.

li=[2,7,9,4,5]

for i in range(len(li)):
    for j in range(i+1,len(li)):
        if li[i]>li[j]:
            li[i],li[j]=li[j],li[i]
print("second largest:",li[-2])
        



