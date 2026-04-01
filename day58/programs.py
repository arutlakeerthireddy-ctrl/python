#Positional-Only Arguments (/)
#Write a function using positional-only arguments to subtract two numbers.
#(Hint: use / in function definition)
def subtract(a,b,/):
    return a-b
print(subtract(9,5))

#Keyword-Only Arguments (*)
#Create a function where arguments must be passed only as keywords (use *).
#Example: calculate total price with tax.
def cal_price(*,price,tax):
    total=price+tax
    return total
print(cal_price(price=100,tax=5))
    
#Mixed All Types
#Write a function that uses positional, *args, keyword-only, and **kwargs all together.
def all_types(a,b,/,c,*args,d,e,**kwargs):
    return a,b,c,d,e,args,kwargs
print(all_types(1,2,8,7,8,d=0,e=7,name="keerthi",age=21))

#positional → / → normal → *args → keyword-only → **kwargs