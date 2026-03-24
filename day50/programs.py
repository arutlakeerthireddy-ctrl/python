#Print a pyramid pattern using *.
n=int(input("Enter number: "))#5
for i in range(1,n+1):#i=1-5
    print(" "*(n-i),end="")#" "*(5-1)
    print("*"*(2*i-1))#"*"*1
'''
Enter number: 5
    *
   ***
  *****
 *******
*********   '''
    
    
#Print an inverted pyramid.
n=int(input("Enter number: "))
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1))
'''
Enter number: 5
*********
 *******
  *****
   ***
    *  '''
