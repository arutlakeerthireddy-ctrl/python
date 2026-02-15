1. #Find the sum of elements in `t = (10, 20, 30, 40)` without loops or conditions.
t=(10,20,30,40)
print(sum(t))#100

2. #Find the maximum and minimum values in `t = (5, 15, 25, 35)`
t = (5, 15, 25, 35)
print(max(t))#35
print(min(t))#5

3. #Find the length of `t = (1, 2, 3, 4, 5)` without using loops.
t=(1,2,3,4,5)
print(len(t))#5

4. #Reverse `t = (1, 2, 3, 4, 5)` using slicing.
t = (1, 2, 3, 4, 5)
print(t[-1:-6:-1])#(5,4,3,2,1)

5. #Concatenate `t1 = (1, 2)` and `t2 = (3, 4)`.
t1=(1,2)
t2=(3,4)
print(t1+t2)#(1,2,3,4)

6. #Convert list `[1, 2, 3, 4]` into a tuple.
li=[1,2,3,4]
print(tuple(li))#(1,2,3,4)


7. #Convert tuple `(10, 20, 30)` into a list and add `40`.
t=(10,20,30)
t=list(t)
t.append(40)
print(t)#[10,20,30,40]

8. #Convert string `"PYTHON"` into a tuple of characters.
s="PYTHON"
print(tuple(s))#('P', 'Y', 'T', 'H', 'O', 'N')

9. #Convert tuple `(1, 2, 3)` into string `"123"` without loops.
t=(1,2,3)
s1=str(t[0])
s2=str(t[1])
s3=str(t[2])
print(s1+s2+s3)#123

10.# Convert nested list `[[1,2],[3,4]]` into a tuple of tuples.
li=[[1,2],[3,4]]
t=tuple(li[0]),(tuple(li[1]))
print(t)#((1, 2), (3, 4))



11. #Repeat tuple `("Hi",)` four times.
12. #Check whether `20` exists in `(10, 20, 30, 40)`.
13. #Compare `(1,2,3)` and `(1,2,4)` using comparison operators.
14. #Multiply all elements in `t = (1,2,3,4)` using a built-in function.
15. #Find the index of `30` in `(10,20,30,40)`.
16. #Join words in `("I","Love","Python")` into a single string.
17. #Count occurrences of `"a"` in `("apple","banana","mango")`.
18. #Convert all strings in `("apple","banana","mango")` to uppercase.
19. #Access element `4` from `t = (1,2,(3,4),5)`.
20. #Flatten `((1,2),(3,4))` into `(1,2,3,4)` without loops.
