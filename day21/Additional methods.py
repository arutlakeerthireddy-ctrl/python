#Additional set methods
a={1,2,3,4,5}
b={3,4,5,6,7}

#intersection_update():update original set with common elements
a.intersection_update(b)
print(a)#{3,4,5}
#or


#difference_update():removes common elements from original set
a={1,2,3,4}
a.difference_update(b)
print(a)#{1,2}

#symmetric_difference_update():keeps only non common elements
a={1,2,3,4}
a.symmetric_difference_update(b)
print(a)#{1, 2, 5, 6, 7}

#frozenset()
a=frozenset([1,2,3])
b=frozenset({2,3,4,5})
print(a|b)#frozenset({1, 2, 3, 4, 5})
print(a&b)#frozenset({2, 3})
print({a-b})#{frozenset({1})}



