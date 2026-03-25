#Print a half diamond pattern.
n=int(input("Enter number: "))
for i in range(1,n+1):
    print(" "*(n-i),end="")
    print("*"*i)
for j in range(n-1,0,-1):
    print(" "*(n-j),end="")
    print("*"*j)
'''
Enter number: 5
    *
   **
  ***
 ****
*****
 ****
  ***
   **
    *  '''

n=int(input("Enter number: "))
for i in range(1,n+1):
    print("*"*i)
for j in range(n-1,0,-1):
    print("*"*j)
    
'''
Enter number: 5
*
**
***
****
*****
****
***
**
*  '''