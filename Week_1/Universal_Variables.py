a = 5
def b() :  #function definition
    a = 10
    print(a)

b()
print(a)

def c() :
    global a #global means both side the definition 'a' have to work doesnt matter in or out of function
    a = 10
    print(a)

c()
print(a)