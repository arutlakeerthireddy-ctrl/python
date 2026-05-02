#Print numbers from 1 to N using recursion
#without recursion
def func(n):
    for i in range(1,n+1):
        print(i)
func(10)
#with recursion
def func(n):
    if n==0:
        return 
    func(n-1)
    print(n)
func(5)

#Print numbers from N to 1
def func(n):
    if n==0:
        return 
    print(n)
    func(n-1)
func(5)

#Find factorial of a number
#without recursion
def factorial(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact
print(factorial(5))
#with recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    return n*factorial(n-1)
print(factorial(5))







