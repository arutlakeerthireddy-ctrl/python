#Write a Python function square_sum(n) that takes a number n and returns the sum of squares from 1 to n.
def square_sum(n):
    sum=0
    for i in range(1,n+1):
        sum+=i*i
    return sum
print(square_sum(20))
        