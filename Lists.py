from itertools import count
from msilib import PID_TITLE


demo_list=[1,'hello',1.34,True,[1,2,3]]
colors=['red','green','blue']

numberlist =list((1,2,3,4))
print(numberlist)

r=list(range(1,10))

print(r)

print(type(colors))
#print(dir(colors))
print('green' in colors) # Consulta si pertenece el elemento regresa booleno

colors[1] = 'yelow'

print(colors)

colors.append('violet') # solo acepta un elemento
colors.extend(('orange','green')) #se debe utilizar otro parentesis
print(colors)

colors.insert(1, 'pink')
print(colors)

colors.pop() # Elimina ultimo elemento
print(colors)

colors.pop(1) # Elimina el elemento en el index 1
print(colors)

# colors.clear() #Elimina todo
# print(colors)

colors.sort(reverse=True) # Ordena en orden alfabetico inverso
print(colors)

print(colors.index('yelow'))

print(colors.count('red'))