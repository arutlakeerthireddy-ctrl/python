#looping in dictionary
s={"name":"uma","age":18,"course":"btech"}
#loop through keys
for key in s:
    print(key)
#if you want values with keys
for key in s:
    print(key,s[key])

#using .keys()
for i in s.keys():
    print(i)

#using .values()
for i in s.values():
    print(i)

#using .items()
for i in s.items():
    print(i)

#loop with index using enumerate()
for index,(key,value) in enumerate(s.items()):
    print(index,key,value)
    