#Print a triangle where each row has same number (111, 222…).
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

"""
Enter number: 6
1
22
333
4444
55555
666666  """

#Reverse same-number triangle
n=int(input("Enter number: "))
for i in range(n,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()

"""
Enter number: 6
666666
55555
4444
333
22
1    """
        
#Print alternating 0 and 1 pattern
n=int(input("Enter number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        if (i+j)%2==0:
            print(1,end="")
        else:
            print(0,end="")
        
    print()
    
"""
Enter number: 6
1
01
101
0101
10101
010101  """