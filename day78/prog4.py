#Write a Python function to check whether a number is prime or not.
def prime(n):
    if n < 2:
        return "Not Prime"
    for i in range(2, n):
        if n % i == 0:
            return "Not Prime"
    return "Prime"

print(prime(7))

