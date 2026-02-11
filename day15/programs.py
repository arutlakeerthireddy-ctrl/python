#Write a program to find the sum of all elements in a list.
li=[10,20,30,40]
print(sum(li))#100

#Write a program to find the average of list elements.
li=[10,20,30,40]
total=sum(li)#100
avg=total/len(li)#100/4
print(avg)#25.0

#Write a program to multiply all elements in a list.
li=[1,2,3,4]
x=1
for i in li:
    x=x*i
    
print(x)#24

#Write a program to find the difference between max and min elements.
li=[1,2,3,4]
difference=max(li)-min(li)
print(difference)