#Write a program using a while loop that stops execution when the number reaches 6 using break.
i=1
while i>0:
    if i==6:
        break
    print(i)
    i+=1

#Write a program using a while loop to skip multiples of 3 using continue.
i=1
while i<=20:
    if i%3==0:
        i+=1
        continue
    print(i)
    i+=1
    

