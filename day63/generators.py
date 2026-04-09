#what is generators in python?
'''generator is a special type of function that return a values one by one,not returns all at once
it uses yield instead of return
it saves memory
it works well with large data'''

#Types of generators
'''
1.generator function:A function that uses the yield keyword to produce values one by one.
2.generator expression:A short and simple way to create generators using parentheses () (similar to list comprehension). '''

#example of generator function
def num():
    yield 1
    yield 2
    yield 3
for i in num():
    print(i)
#or
def num():
    yield 1
    yield 2
    yield 3
n=num()
print(next(n))
print(next(n))
print(next(n))

#example of generator expression
g=(i*i for i in range(5))

for i in g:
    print(i)





