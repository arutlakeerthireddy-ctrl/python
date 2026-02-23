#what is nested dictionary:a dictionary inside another dictionary
#Basic structure
"""d={
    key1:{subkey1:value1,subkey2:value2},
    key2:{subkey1:value1,subkey2:value2}
}"""
#example
student={
    "keerthi":{"branch":"csm","age":20,"roll":14},
    "uma":{"branch":"cse","age":18,"roll":73}
}
print(student)
#{'keerthi': {'branch': 'csm', 'age': 20, 'roll': 14}, 'uma': {'branch': 'cse', 'age': 18, 'roll': 73}}

#Accessing data
print(student['keerthi']['age'])#20
print(student["uma"]["branch"])#cse

#updating data
student["uma"]["roll"]=74
print(student)
#{'keerthi': {'branch': 'csm', 'age': 20, 'roll': 14}, 'uma': {'branch': 'cse', 'age': 18, 'roll': 74}}

#adding data
student["keerthi"]["grade"]="A"
print(student)

student["pavani"]={"branch":"csm","age":20}
print(student)
#{'keerthi': {'branch': 'csm', 'age': 20, 'roll': 14, 'grade': 'A'},
#  'uma': {'branch': 'cse', 'age': 18, 'roll': 74}, 
# 'pavani': {'branch': 'csm', 'age': 20}}