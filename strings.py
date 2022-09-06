from ast import Index
from re import M


myStr="Hello World"

print("My name is Edwin, " + myStr)
print(f"My name is Edwin, {myStr}") # la f indica que lo que esta en {}
                                    # es llamado de una variable
print("My name is Edwin, {0}".format(myStr)) # otra forma

#print (dir(myStr))

print(myStr.upper()) #convertir todo a mayuscula

print(myStr.lower()) #todo en minusculas

print(myStr.startswith("Hello")) # El string inicia con la palabra Hello
                                 # regresa un booleano
print(myStr.endswith("World")) # El string finaliza con la palabra World
                                 # regresa un booleano
print(myStr.split())# separa elementos por espacios o comas, uno debe indicarlo

print(myStr.find(" ")) #busca un caracter y devuelve la posición del caracter
                       # Inicia el contador en 0 con el primer caracter
print(len(myStr))  #Arroja la longitud del string

print(myStr.index("e")) # Arroja el indice del caracter string, es un número

print(myStr.isnumeric()) # Consulta si es un numero

print(myStr.isalpha()) # Pregunta si es alfanumerico

print(myStr[-1]) # El primer elemento es H y ese tiene index 0
                 # por loque index -1 corresponde a la ultima.
