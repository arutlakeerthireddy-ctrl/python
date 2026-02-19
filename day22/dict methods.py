#dictionary methods
#accessing keys
#using[]
d={"name":"keerthi","age":21,"course":"csm"}
print(d["age"])#21

#get():
d={"name":"keerthi","age":21,"course":"csm"}
print(d.get("name"))#keerthi
print(d.get(21))


#keys:returns all keys
d={"name":"keerthi","age":21,"course":"csm"}
print(d.keys())#dict_keys(['name', 'age', 'course'])

#values:returns all values
print(d.values())#dict_values(['keerthi', 21, 'csm'])

#items:returns key-value pairs
print(d.items())#dict_items([('name', 'keerthi'), ('age', 21), ('course', 'btech')])

#update:adds or modifies
d.update({"branch":"csm"})
print(d)#{'name': 'keerthi', 'age': 21, 'course': 'csm', 'branch': 'csm'}

#pop():remove a specific key
d.pop("name")
print(d)#{'age': 21, 'course': 'csm', 'branch': 'csm'}

#popitem():removes last inserted
d.popitem()
print(d)#{'age': 21, 'course': 'csm'}

#clear():removes all items
d.clear()
print(d)#{}

#copy():creates shallow copy
d={"name":"keerthi","age":21,"course":"csm"}
d.copy()
print(d)#{'name': 'keerthi', 'age': 21, 'course': 'csm'}

#setdefault():if key exists returns value,inserts if not present
d.setdefault("a",0)
print(d)#{'name': 'keerthi', 'age': 21, 'course': 'csm', 'a': 0}






