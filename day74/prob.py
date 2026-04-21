#filter():keeps only the elements that satisfy a condition
#filter(function,iterable)
nums=[1,2,3,4,5,6]
result=list(filter(lambda x:x%2==0,nums))
print(result) #[2, 4, 6]

#Filter all numbers greater than 10 from a list.
li=[0,5,10,15,20,25,30]
result=list(filter(lambda x:x>10,li))
print(result) #[15, 20, 25, 30]

#From a list of strings, filter words with length greater than 5.
li=['hi','keerthi','ummarani','hloo']
result=list(filter(lambda x:len(x)>5,li))
print(result) #['keerthi', 'ummarani']

#Filter all positive numbers from a list.
li=[-1,-2,5,6,8,-3]
result=list(filter(lambda x:x>0,li))
print(result) #[5, 6, 8]