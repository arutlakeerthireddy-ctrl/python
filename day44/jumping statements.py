#jumping statements:used to control flow of loop,they let you skip iterations
#exit loops,and do nothing in specific cases
#break:stops loop completely
#example
for i in range(5):
    if i==4:
        break
    print(i)
#output
"""0
1
2
3"""

#continue:skip current iteration and move to next one
#example
for i in range(5):
    if i==3:
        continue
    print(i)
#output
"""0
1
2
4"""

#pass:do nothing(placeholder)
#example
for i in range(5):
    if i%2==0:
        pass
    print(i)
#output
"""0
1
2
3
4"""
