#Print increasing number triangle (1, 12, 123…).
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end="")
    
    print()
"""
Enter number: 6
1
12
123
1234
12345
123456  """

#Print decreasing number triangle.
n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print()
"""
Enter number: 6
123456
12345
1234
123
12
1   """  

#Palindrome Number Triangle
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
          print(j,end=" ")
    for  k in range(i-1,0,-1):
        print(k,end=" ")
    print()
    
"""
Enter number: 6
1 
1 2 1
1 2 3 2 1
1 2 3 4 3 2 1
1 2 3 4 5 4 3 2 1
1 2 3 4 5 6 5 4 3 2 1  """

