#loops are used to repeat a block of code multiple times until the condition is satisfied
#looping concepts are
#1.for loop:used when we know how many times the loop should run.it iterates over sequence like
#list,string,tuple,range
#syntax:
#for variable in sequence:
#   statement
#example:printing numbers
for i in range(0,5):
    print(i)

#2.while loop:executes block of code as long as condition is true.it is useful when no.of iterations is unknown
#syntax
#while condition:
#    statements
#example
i=1
while i<=5:
    print(i)
    i+=1

#3.nested loop:loop inside another loop.the inner loop executes completely for every iteration of outer loop
for i in range(0,3):
    for j in range(0,4):
        print(i,j)