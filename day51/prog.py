#Print Floyd’s Triangle.
n=int(input("Enter number: "))
num=1
for i in range(1,n+1):
    for j in range(1,i+1):
        print(num,end="")
        num+=1
    print()
    
'''
Enter number: 5
1
23
456
78910
1112131415  '''
    