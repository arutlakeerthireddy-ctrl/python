#*args (Variable Positional Arguments)
#Write a function to find the sum of any number of values using *args.
def values_sum(*args):
    return sum(args)
t=(3,4,5,8,9,1)
print(values_sum(1,3,5,6,7))
print(values_sum(*t))

#Create a function that prints all given arguments using *args.
def func(*numbers):
    print(*numbers)
func(1,2,3,4)

def func(*numbers):
    for num in numbers:
        print(num)
func(1,3,2,4)

#Write a function to find the largest number using *args.
def large_num(*largest):
    return max(largest)
print(large_num(9,4,3,1))