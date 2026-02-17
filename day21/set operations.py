#set operations
#union:combine all elements
A={1,2,3}
B={4,5}
print(A.union(B))#{1, 2, 3, 4, 5}
#or
print(A|B)

#intersection:common elements
a={1,2,4,3}
b={3,4,5,6}
print(a.intersection(b))#{3, 4}
#or
print(a&b)

#difference:elements in first but not second
a={1,2,3,4,5}
b={2,3,4,7,8}
print(a.difference(b))#{1,5}
#or
print(a-b)

#symmetric_difference:non common elements
a={1,2,3,4,5}
b={2,3,4,7,8}
print(a.symmetric_difference(b))
#or
print(a^b)

#subset:check if all elements of a in b
a={1,2}
b={1,2,3,4}
print(a.issubset(b))#True
print(b.issubset(a))#False

#superset:check if a contain b
a={10,20,30,40,50.3}
b={10,20}
print(a.issuperset(b))#true
print(b.issuperset(a))#False

#disjoint-no common elements
a={1,2,3}
b={4,5}
print(a.isdisjoint(b))#True

a={1,2,3}
b={2,3,4}
print(a.isdisjoint(b))#False