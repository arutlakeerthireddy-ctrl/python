#Write a program to find all pairs of numbers whose sum equals a given number.
#Example:
#List: [1,2,3,4,5]
#Target: 6

li=[1,2,3,4,5]
tar=6
for i in range(len(li)):
    for j in range(i+1,len(li)):
        sum=li[i]+li[j]
        if sum==tar:
            print(li[i],li[j])

        
