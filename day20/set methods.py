#set methods
#add():adds a single element
s={1,2,3}
s.add(4)
s.add("hlo")
print(s)#{1, 2, 3, 4,'hlo'}

#update():adds multiple elements
s={1,2,3}
s.update(["hi",4,True])
print(s)#{1, 2, 3, 4, 'hi'}

#remove():Removes an element found error if not present
s={1, 2, 3, 4, 'hi'}
s.remove("hi")
print(s)#{1,2,3,4}

#s.remove('hlo')
print(s)#Error

#discard():removes an element,no error if not found
s={1,2,3,4}
s.discard(1)
print(s)#{2,3,4}

s.discard(5)
print(s)#{2,3,4}#no error

#pop():removes a random element
s={1,2,3,4}
s.pop()
print(s)#{2, 3, 4}

#clear():removes all elements
s={1,2,3,4}
s.clear()
print(s)#set()

#copy():creates duplicate set
s={"hi",1,2}
s.copy()
print(s)#{1, 2, 'hi'}



