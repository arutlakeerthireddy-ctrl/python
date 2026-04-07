#Build a simple calculator using global variables to store the result
result=0
def cal(a,b,op):
    global result
    if op=='+':
        result=a+b
    elif op=='-':
        result=a-b
    elif op=='*':
        result=a*b
    elif op=='%':
        result=a%b
    elif op=='/':
        if b!=0: 
            result=a/b
        else:
            print("cannot divide by 0")
    elif op=='//':
        if b!=0:
            result=a//b
        else:
            print("cannot divide by 0")
    else:
        return "Invalid operator"
    return result

print(cal(5,8,'+'))

