#Multiples of 3 Generator
#Write a generator that yields numbers divisible by 3 up to n.
def divisible(n):
    for i in range(0,n+1):
        if i%3==0:
            yield i
n=int(input('Enter number:'))
for j in divisible(n):
    print(j)

#Even Numbers Generator
#Generate all even numbers from 1 to n.
def even_num(n):
    for i in range(2,n+1):
        if i%2==0:
            yield i
n=int(input('Enter number:'))
for j in even_num(n):
    print(j)

#Squares Generator
#Yield squares of numbers from 1 to n.
def square(n):
    for i in range(0,n+1):
        yield i*i
n=int(input("Enter number:"))
for j in square(n):
    print(j)

#String Iterator
#Given a string, yield each character one by one.
def word(s):
    for ch in s:
        yield ch
s=input("Enter character:")
for ch in word(s):
    print(ch)

#Count Down Generator
#Yield numbers from n to 1.
def count_down(n):
    for i in range(n,0,-1):
        yield i
n=int(input("Enter number:"))
for j in count_down(n):
    print(j)