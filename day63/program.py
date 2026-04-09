#problem on generators

''' print the one by one values as per the user input 
 input: 100
 output: line by line values which are divisible by 3'''

def num(n):
    for i in range(n):
        if i%3==0:
            yield i
n=int(input("Enter num:"))
for j in num(n):
    print(j)
