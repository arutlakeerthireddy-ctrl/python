#positional only argument:
# These arguments must be passed in order (position-wise)
# You cannot use keyword names while calling them
#example
def func(a,b,/):
    print(a+b)
func(1,2) #3
#func(a=1,b=4) #wrong
# '/' means everything before it is positional-only

#keyword only arguments:
#These arguments must be passed using names (keywords)
#You cannot pass them positionally
def func(*,a,b):
    print(a-b)
func(a=9,b=3)
# * means everything after it is keyword-only

#mixed arguments
#combination of all arguments like position only,normal arguments,keyword only 
#syntax
def func(a,b,/,c,d,*,e,f):
    pass
#example
def func(a,b,/,c,*,d):
    print(a,b,c,d)
func(1,2,c=3,d=4)
#func(a=1,b=2,c=3,d=4) #wrong postional only error
#func(1,2,3,4) #keyword only error

#argument unpacking
#Used to pass multiple values easily

#using * (for list/tuple)
def func(a,b,c,d):
    print(a,b,c,d)
nums=[1,2,3,4]
func(*nums)
# *nums → converts list into separate values

#using **(for dictionary)
def func(name,age,b):
    print(name,age,b) #keerthi 21 9
dict={'name':"keerthi",'age':21,'b':9}
func(**dict)
