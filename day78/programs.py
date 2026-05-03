#Find sum of first N natural numbers
#without recursion
def func(n):
    sum=0
    for i in range(n+1):
        sum+=i
    return sum
print(func(20))#210
#with recursion
def func(n):
    if n==0:
        return 0
    return n+func(n-1)
print(func(20))

