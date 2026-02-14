#list comprehension
list comprehension is a short and powerful way to create new list
using a single line of code.
instead of writing multiple lines within a loop,we write it in one clean expression.

#basic syntax
[expression for item in iterable]
#ex
squares=[x*x for x in range(5)]
print(squares)#[0,1,4,9,16]

#with condition
[expression for item in iterable if condition]
#ex
even=[x for x in range(10) if x%2==0]
print(even)#[0,2,4,6,8]

#with if-else
[expression_if_true if condition else expression_if_false for item in iterable]
#ex
result=["even" if x%2==0 else "odd" for x in range(5)]
print(result)#['even','odd','even','odd','even']

#using list comprehension on existing list
li=[10,20,30]
new=[x+5 for x in li]
print(new)#[15,25,35]

