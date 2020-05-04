def outer1(a=0,b=0):
    if a>0:
        a= int(input('Enter the value of a: '))
    if b>0:
        b= int(input('Enter the value of b: '))
    def inner1():
        return a+b
    return inner1()
def outer2():
    return outer1(a,b)+5
