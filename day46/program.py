#Write a program using a while loop that stops when the number reaches 10 using break.
i=1
while i>0:
    if i==10:
        break
    print(i)
    i+=1

#Write a program using a while loop to skip multiples of 5 using continue.
i=1
while i<20:
    if i%5==0:
        i+=1
        continue
    print(i)
    i+=1
