#what is set?
#set is a buitin datatype used to store multiple uniques elements
#characteristics
#unordered
#mutable
#no indexing
#no slicing
#do not allow duplicates
#elements must be immutable(int,float,string,tuple)

#creating set
s={1,2,3}
print(s)
#or
#using set() constructor
s=set((1,2,3))
print(s)#{1,2,3}

#we cannot access items in the set but we can loop through the set using for loop
s={10,20,30,40}
for i in s:
    print(i)

#set stores different datatypes
s={1,2,3,4}
s={"a","hi","keerthi"}
s={True,False}

#duplicates are not allowed
#set remove duplicates automatically
s={1,2,2,3,3,4,4}
print(s)#{1,2,3,4}

#True and 1 are considered as same value
#False and 0 are considered as same value
s={True,1,2,3}
print(s)#{True, 2, 3}

s={False,0,1,3}
print(s)#{False, 1, 3}