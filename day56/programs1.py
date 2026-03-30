#Keyword Arguments
#Write a function to display student details using keyword arguments.
def stud_details(name,age,roll):
    print(name,age,roll) #('uma', 19, 73)
stud_details(name="uma",age=19,roll=73)

#Create a function to calculate simple interest using keyword arguments.
def simple_interest(p,r,t):
    si=p*r*t/100
    return si #47.52
print(simple_interest(p=198,t=4,r=6))

#Write a function where you pass city and country using keywords and print them.
def city_country(city,country):
    return city,country  #('hyd', 'india')
print(city_country(city="hyd",country="india"))

#Create a function that takes length and width using keyword arguments and returns area.
def area(l,w):
    a=l*w
    return a  #45
print(area(l=5,w=9))
