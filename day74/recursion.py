#what is recursion?
#recursion is a programming technique where a function calls itself to solve problem
#instead of using loops,recursion breaks problem into smaller subproblems of same datatype

#syntax:
'''def function_name(parameters):
    if base_condition: #base case
       return Value
    #recursive case
    return function_name(modified_parameters)'''

#use
#factorial calculation
#fibonacci sequence
#searching/sorting algorithms
#trees/graphs traversal
#backtracking problems(like puzzles)
#example
def countdown(n):
    if n==0:
        return
    print(n)
    countdown(n-1)
countdown(5)
