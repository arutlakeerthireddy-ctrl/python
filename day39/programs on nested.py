#Write a program to find the largest number in a list using comparison with every other element using nested loops.
li=[4,5,6,7,3,9]
n=len(li)
for i in range(n):
    largest=True
    for j in range(i):
        if li[j]>li[i]:
            largest=False
if largest==True:
        print(li[i])
    
            