#lambda function:it is a small and anonymous function that defined in single line 
# using lambda keyword that can take any no of arguments and returns result automatically.
def add(): #normal function
    return 'hi'
print(add())

#lambda function
#lambda arguments:expression
add=lambda x:x+2
print(add(2))

square=lambda x:x*2
print(square(7))

#using multiple arguments
add=lambda a,b,c:a+b+c
print(add(2,5,3))

#lambda is used with map(),filter(),sorted()


