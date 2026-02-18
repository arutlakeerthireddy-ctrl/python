#Dictionary:dictionary is a builtin datatype used to store data in key-value pairs
#it is defined using curly braces{}
#example
student={"name":"keerthi","age":20,"branch":"csm"}
print(student)

#characteristics
#mutable-can modify values
#keys are unique
#keys are immutable(int,float,str,tuple)
#values can be duplicate
#unordered(maintain insertion order)
#indexed by keys(not position)

#creating dictionary
#normal way
d={"a":1,"b":2}

#using dict()
d=dict(a=1,b=3)
print(d)#{'a': 1, 'b': 3}

#from list of tuples
d=dict([("a",1),("b",2)])
print(d)#{'a': 1, 'b': 2}

#using fromkeys()
d=dict.fromkeys(["a","b","c"],1)
print(d)#{'a': 1, 'b': 1, 'c': 1}

