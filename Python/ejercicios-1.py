#Comentario en python
'''Comentario 
multilinea
'''
#Escritura
print('Hola mundo')

#Declaracion de variables

#Ninguna declaracion de variable se puede nombrar con un numero al inicio 
#y no puede tener caracteres especiales, tampoco puede ser nombrada con una palabra reservada

x = 10 #entero (int)
y = 10.0 #flotante (float)
word = "palabra" #string (str)

#Indentacion

if 5 > 2:
    print("Five is greater than two")

#Casting

numfloat = float(3)
numInt = int(3)
numStr = str(3)

print(numfloat,numInt,numStr)

#Visualizar el tipo de dato

print(type(numInt))

#Se pueden asignar multiples valores a varias variables en una sola linea

m,n,o = "hola",5,True

print(m,n,o)

#Desempaquetar una coleccion

fruits = ["apple","banana","cherry"]
a,b,c = fruits

print(a,b,c)

#Desempaquetar una tupla

fruitsT = ("apple","banana","cherry")
(green,yellow,red) = fruitsT

print(green,yellow,red)

#El '+' sirve para concatenar o como operador matematico segun el contexto

print(5+2)
print('5'+'2')

#Variables locales y globales

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

def func():
   x = "Fantastic"
   print("Python is " + x)

func()

#Las variables declaradas globales pueden ser utilizadas en cualquier ambito

def func2():
  global y
  y = "fantastic"

func2()

print("Python is " + y)

