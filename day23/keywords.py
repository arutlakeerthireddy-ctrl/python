#in:it checks if a key present in dictionary,not values
d={'a':10,'b':3,'c':0}
print('a' in d)#True
print(0 in d)#False

#not in:checks if doesn't exist
print('a' not  in d)#false
print('s' not in d)#True

#del:delete key
d={'a':10,'b':3,'c':0}
del d['b']
print(d)#{'a': 10, 'c': 0}


