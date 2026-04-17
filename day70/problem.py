'''One decorator multiplies result by 2
Another adds 10
If function returns 5, what happens when:
Multiply → then Add
Add → then Multiply'''
def multiply(func):
    def wrap():
        return func()*2
    return wrap
def add(func):
    def wrap():
        return func()+10
    return wrap
@multiply
@add
def operation():
    return 5
print(operation())#30

def multiply(func):
    def wrap():
        return func()*2
    return wrap
def add(func):
    def wrap():
        return func()+10
    return wrap
@add
@multiply
def operation():
    return 5
print(operation())#20