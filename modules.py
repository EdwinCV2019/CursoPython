#Crear tus modulos
#Descargar modulos externos
#Usar modulos de python

import datetime
import imp
from lib2to3.pytree import convert
from traceback import print_tb

#from date importe timedelta , para simplificar y no escribir datetime

print(datetime.date.today())

import fmath

fmath.add(1,2)
fmath.substract(3,1)

from fmath import add, substract

add(5,4)
substract(7,2)

from colorama import Fore,Style,init
init(convert=True)
print(Fore.RED+"Hello World")
