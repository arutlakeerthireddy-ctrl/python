#builtin functions in sets
#len()
s={1,2,3,4,5,6}
print(len(s))#6

#max()
s={1,4,3,5,6,7}
print(max(s))#7

#min()
print(min(s))#1

#sorted()
print(sorted(s))#[1, 3, 4, 5, 6, 7]

#sum()
print(sum(s))#26

#set comprehension
s=[x*x for x in range(6)]
print(s)#[0, 1, 4, 9, 16, 25]
