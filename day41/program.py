#Write a program to find the number of pairs whose product equals a given number

li=[1,2,3,4]
num=6
for i in range(len(li)):
    for j in range(i+1,len(li)):
        prod=li[i]*li[j]
        if num==prod:
            print(li[i],li[j])
