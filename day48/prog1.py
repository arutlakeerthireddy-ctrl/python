#Print a pattern of numbers from 1 to n in each row.
n=int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()

"""
1 2 3 4 5 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5 """

#end=" " → keeps printing on same line
#print() → moves to next line