#Write a program to print numbers from 1 to 10 but stop when the number is 5 using break.
for i in range(1,10+1):
    if i==5:
        break
    print(i)

#Write a program to print only odd numbers from 1 to 10 using continue.
for i in range(1,10+1):
    if i%2==0:
        continue
    print(i)

#Write a program to demonstrate the use of pass inside a loop.
for i in range(1,10):
    if i%2==0:
        pass
    print(i)