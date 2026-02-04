#Bitwise operators:
 Bitwise opearators work on the binary form(0's and 1's) of integers and perform operations bit by bit
#Bitwise AND(&)
compare each bit of two numbers
result bit is 1 if both bits are 1
EX:a=5
   b=2
print(a&b)

#Bitwise OR(|)
compares each bit
result bit is 1 if atleast one bit is 1
ex:print(a|b)

#Bitwise XOR(^)
compare each bit
result bit is 1 if both bits are different
ex:
print(a^b)

#Bitwise NOT(~)
Inverts all bits (0 → 1, 1 → 0).
Produces the 2’s complement result.
formula:~n=-(n+1)
ex:num=5
   print(~num)

#Bitwise left shift(<<)
Shifts bits to the left.
Adds zeros on the right.
Multiplies the number by 2ⁿ.
formula:x<<n=x*(2**n)
ex:x=5
   n=2
   print(x<<n)

#Bitwise right shift(>>)
Shifts bits to the right.
Removes bits from the right.
Divides the number by 2ⁿ.
formula:x>>n=x//(2**n)
ex:print(x>>n)

