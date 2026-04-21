#map():takes input function and applies it to every element in list
#map(function,iterable)
nums=[1,2,3,4]
result=list(map(lambda x:x*2,nums))
print(result) #[2, 4, 6, 8]

#Convert all strings in a list to uppercase using map().
li=['hi','keer','how','are','you']
result=list(map(lambda word:word.upper(),li))
print(result) #['HI', 'KEER', 'HOW', 'ARE', 'YOU']

#Add 5 to every number in a list using map().
li=list(map(int,input("Enter:").split()))
result=list(map(lambda x:x+5,li))
print(result)
#Enter:1 2 3 4
#[6, 7, 8, 9]

#Find the length of each string in a list using map().
li=list(input("Enter:").split())
result=list(map(lambda string:len(string),li))
print(result) #[2, 3]

#Convert a list of integers to strings using map().
li=[11,20,3,3.4]
result=list(map(lambda x:str(x),li))
print(result) #['11', '20', '3', '3.4']