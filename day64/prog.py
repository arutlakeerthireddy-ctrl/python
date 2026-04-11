#Factorial Generator
#Yield factorial values up to n.
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
        yield fact
n=int(input("Enter number:"))
for j in factorial(n):
    print(j)
    
'''Enter number:5
1
2
6
24
120 '''

