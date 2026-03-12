#Write a program to find the sum of digits of a number using a while loop.

n=int(input("Enter number:"))
sum=0
while n>0:
    digit=n%10
    sum+=digit
    n=n//10
print(sum)

    
#write a program to check whether a number is Armstrong or not using a while loop.
n=int(input("Enter number:"))
temp=n
count=0
while n>0:
    n=n//10
    count+=1
sum=0
n=temp
while n>0:
    digit=n%10
    sum+=digit**count
    n=n//10
if sum==temp:
    print("armstrong")
else:
    print("not")


