#Write a program to check whether a person can donate blood (age between 18 and 60 and weight ≥ 50 kg).
age=20
weight=50
if 18<age<60 and weight>=50:
    print("person can donate blood")
else:
    print("person cannot")

#Write a program to calculate bonus:
#Service > 5 years → 10% bonus
#Otherwise → No bonus
service=int(input("Enter no of years:"))
if service>5:
    print("10% bonus")
else:
    print("no bonus")