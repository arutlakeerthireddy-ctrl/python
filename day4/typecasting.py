#typecasting
type casting is the process of converting one datatype to another datatype.
#types of typecasting:
1.implicit typecasting
2.explicit typecasting
#1.implicit typecasting
it is done by python interpreter automatically without user intervention.
usually it converts a smaller datatype to a larger datatype to prevent data loss.
#example:
a=6 #int
b=23.6 #float
sum=a+b #int converting to float automatically
print(sum) #29.6
#2.explicit typecasting
it is done by the user to convert one datatype to another datatype using predefined functions.
#example:
#int to float
x=8
y=float(x)
print(y) #8.0
print(type(y)) #<class 'float'>
#float to int
p=9.7
q=int(p)
print(q) #9
print(type(q)) #<class 'int'>
#int to complex
m=5
n=complex(m)
print(n) #(5+0j)
print(type(n)) #<class 'complex'>
#float to complex
r=4.3
s=complex(r)
print(s) #(4.3+0j)
print(type(s)) #<class 'complex'>
#complex to float or int(not directly)
c=3+4j
#to convert complex to float or int,we need to extract real or imaginary part first
real_part=c.real
imag_part=c.imag
real_to_float=float(real_part)
imag_to_int=int(imag_part)
print(real_to_float) #3.0
print(type(real_to_float)) #<class 'float'>
print(imag_to_int) #4
print(type(imag_to_int)) #<class 'int'>
#string to int
s="35"
i=int(s)
print(i) #35
print(type(i)) #<class 'int'>
#string to float
s1="45.67"
f=float(s1)
print(f) #45.67
print(type(f)) #<class 'float'>
#string to complex
s2="6+7j"
c1=complex(s2)
print(c1) #(6+7j)
print(type(c1)) #<class 'complex'>
#int to string
num=50
s3=str(num)
print(s3) #'50'
print(type(s3)) #<class 'str'>
#float to string
num1=78.9
s4=str(num1)
print(s4) #'78.9'
print(type(s4)) #<class 'str'>
#complex to string
num2=2+3j
s5=str(num2)
print(s5) #'(2+3j)'
print(type(s5)) #<class 'str'>
#boolean to int
bool_val=True
int_val=int(bool_val)
print(int_val) #1
print(type(int_val)) #<class 'int'>
#boolean to float
bool_val2=False
float_val=float(bool_val2)
print(float_val) #0.0
print(type(float_val)) #<class 'float'>
#boolean to complex
bool_val3=True
complex_val=complex(bool_val3)
print(complex_val) #(1+0j)
print(type(complex_val)) #<class 'complex'>
#int to boolean
int_num=0
bool_from_int=bool(int_num)
print(bool_from_int) #False
print(type(bool_from_int)) #<class 'bool'>
#float to boolean
float_num=3.14
bool_from_float=bool(float_num)
print(bool_from_float) #True
print(type(bool_from_float)) #<class 'bool'>
#complex to boolean
complex_num=0+0j
bool_from_complex=bool(complex_num)
print(bool_from_complex) #False
print(type(bool_from_complex)) #<class 'bool'>
#string to boolean
str_val=""
bool_from_str=bool(str_val)
print(bool_from_str) #False
print(type(bool_from_str)) #<class 'bool'>
str_val2="Hello"
bool_from_str2=bool(str_val2)
print(bool_from_str2) #True
print(type(bool_from_str2)) #<class 'bool'>
#Note:any non-zero number or non-empty string converts to True in boolean typecasting.
#zero(0,0.0,0+0j) or empty string("") converts to False.
