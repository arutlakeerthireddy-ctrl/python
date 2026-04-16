'''You have two decorators:
One reverses the string
One adds "@@@" at the beginning
Applied like this:
Top: adds "@@@"
Bottom: reverses string
Input: "Python" '''

def add(func):
    def wrap():
        return "@@@"+func()
    return wrap
def reverse(func):
    def wrap():
        return func()[::-1]
    return wrap
@add
@reverse
def str_name():
    return "Python"
    
print(str_name()) #@@@nohtyP