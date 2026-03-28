#variable length arguments
#*args:argument that pass multiple positional arguments to function ,stored as tuple
#example
def func(*nums):
    return nums
print(func(1,2,3))  #(1,2,3)

def func(*args):
    print(args)
func(1,2,3,4,5)  #(1,2,3,4,5)

#**kwargs:arguments that pass multiple keyword arguments to function ,stored as dictionary
#example
def func(**numbers):
    print(numbers)
func(name="keerthi",a=5)  #{'name': 'keerthi', 'a': 5}

def data(**details):
    return details
print(data(name="uma",b=0)) #{'name': 'uma', 'b': 0}

def college(**data):
    return data
print(college(a=1,b=9)) #{'a': 1, 'b': 9}

