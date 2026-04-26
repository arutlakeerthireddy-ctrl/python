#Types of recursion
#direct recursion:function calls itself directly
#def func():
 #   func()

def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n-1)
print(sum_n(8))

def print_nums(n):
    if n==0:
        return
    print_nums(n-1)
    print(n)
print_nums(5)

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
print(fact(5))

def sum_n(n):
    if n==0:
        return 0
    return n+sum_n(n-1)
print(sum_n(5))