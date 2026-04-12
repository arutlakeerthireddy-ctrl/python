#generator methods
#next():used to get next value from a generator
def gen():
    yield 1
    yield 2
g=gen()
print(next(g))
print(next(g))
#when no value are left ,it raises stop iteration

#send():used to send value into generator
def gen():
    x=yield
    print(x)
g=gen()
next(g)
g.send(10)

#throw():handle errors inside generator.used when we want to inject exceptions
def process():
    try:
        while True:
            x = yield
            print("Processing:", x)
    except ValueError:
        print("Invalid input!")

g = process()
next(g)
g.send(10)
g.throw(ValueError)

#close():used to stop execution
def task():
    try:
        while True:
            yield "Running"
    finally:
        print("Generator closed")
g = task()
print(next(g))
g.close()