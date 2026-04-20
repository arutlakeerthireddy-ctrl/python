'''Check Even or Odd
Write a lambda function to check if a number is even or odd.
 Output should be "Even" or "Odd" '''

even_odd=lambda n:'even' if n%2==0 else 'odd'
print(even_odd(8))
print(even_odd(5))

'''Find Maximum of Two Numbers
Use a lambda function to return the larger of two numbers.'''
max_num=lambda a,b:max(a,b)
print(max_num(5,6))

max_num=lambda a,b:a if a>b else b
print(max_num(10,2))

'''Sort List of Tuples
Sort a list of tuples based on the second element using lambda.'''
li=[(1,9),(5,6),(8,7)]
sorted_li=sorted(li,key=lambda x:x[1],reverse=False)
print(sorted_li) #[(5, 6), (8, 7), (1, 9)]