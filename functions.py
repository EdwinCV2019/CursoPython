name= input("Cual es tu nombre : ")

#def hello(name="person"): # si la entrada es vacio retorna person .. hello()
def hello(name):
    print("Hello " + name)

hello(name)

def add(n1,n2):
    print(n1+n2)

add(10,12)

add = lambda n1,n2: print(n1+n2)    #otra forma de hacer una función

add(20,20)