#Create two sets and perform all possible set operations between them.
s1={1,2,3,4,5}
s2={3,4,5}
print(s1.union(s2))#{1, 2, 3, 4, 5}
print(s1.intersection(s2))#{3,4,5}
print(s1.difference(s2))#{1,2}
print(s1.symmetric_difference(s2))#{1,2}
print(s1.issubset(s2))#False
print(s2.issubset(s1))#True
print(s1.issuperset(s2))#True
print(s1.isdisjoint(s2))#False

#Check whether one set is a proper subset of another.
print(s1.issubset(s2))#False

#Check whether two sets are disjoint.
print(s1.isdisjoint(s2))#False

#Modify a set to keep only common elements using intersection_update().
s1={1,2,3}
s2={2,3,4}
s1.intersection_update(s2)
print(s1)#{2,3}

#Remove elements from a set that are present in another set using difference_update().
s1={1,2,3,4}
s2={3,4}
s1.difference_update(s2)
print(s1)#{1,2}

#Find symmetric difference using both operator ^ and method.
s1={1,2,3,4}
s2={3,4,5}
#using operator
print(s1^s2)#{1, 2, 5}
#using method
print(s1.symmetric_difference(s2))

#Add multiple elements from another iterable into a set using update().
s1={1,2,3,4}
s1.update({3,4,5,6})
print(s1)#{1, 2, 3, 4, 5, 6}

#Remove a random element and explain why it is random.
s1={1,2,3,4}
s1.pop()
print(s1)#{2,3,4}
 
#Convert a list into a set and explain what happens to duplicates.
li=[1,2,2,3,4]
s=set(li)
print(s)#{1, 2, 3, 4}

#Compare two sets using <, <=, >, >= operators.
s1={1,2,3,4,5}
s2={3,4,5}
print(s1<s2)#False
print(s1<=s2)#False
print(s1>s2)#True
print(s1>=s2)#True

