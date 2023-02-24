#Ejercicios en python

print("Hello world")

if 5 > 2:
    print("Five is greater than two")

#this is a comment 

'''
This is a comment
written in
more than a just line
'''

carname = "Volvo"
x = 50

x = 5
y = 10

print(x+y)

z = x+y
print(z)

x = y = z = "Orange"
print(x,y,z)

def myFunc():
    global x
    x = "fantastic"

print(type(x))

arrayX = ["apple","banana","cherry"]
print(type(arrayX))

tupla = ("apple","banana","cherry")
print(type(tupla))

diccionario = {"name" : "John", "age" : 36}
print(type(diccionario))

b = True 
print(type(b))

num = 5
print(float(5))

num2 = 5.5
print(int(num2))

complejo = 5
print(complex(5))

cadena = "Hello world"
print(len(cadena))

print(cadena[0])
print(cadena[2:5])

cadena = " Hello world "
cadena = cadena.strip()
print(cadena)

print(cadena.upper())
print(cadena.lower())
cadena = cadena.replace("H","J")
print(cadena)

age = 36
cadena = "My name is John, and I am {}"
print(cadena.format(age))

print(10>9)
print(10+5)
print(10-5)
print(10/5)
print(10*5)


fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits[0]="kiwi"
print(fruits)


