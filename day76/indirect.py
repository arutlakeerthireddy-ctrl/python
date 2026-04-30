#indirect recursion:one function calls another function and that function calls first one.
def is_even(n):
    if n==0:
        return True
    return is_odd(n-1)
def is_odd(n):
    if n==0:
        return False
    return is_even(n-1)
print(is_even(6))
