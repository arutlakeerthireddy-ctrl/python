#**kwargs (Variable Keyword Arguments)
#Write a function to print all key-value pairs using **kwargs.
def details(**kwargs):
    print(kwargs) #{'name': 'keerthi', 'branch': 'csm'}
details(name='keerthi',branch='csm')


#Write a function that counts how many keyword arguments are passed.
def argument_count(**arguments):
    count=0
    for i in arguments:
        count+=1
    return count
dict={'name':"keer",'age':21}
print(argument_count(**dict))

