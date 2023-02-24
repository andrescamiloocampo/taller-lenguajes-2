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

#Variables

carname = "Volvo"
x = 50

x = 5
y = 10

print(x+y)

z = x+y
print(z)

x = y = z = "Orange"
print(x,y,z)

#ambito

def myFunc():
    global x
    x = "fantastic"

#Tipos de variables

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

#Strings

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

#listas

fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = ["apple", "banana", "cherry"]
print(fruits[1])

fruits[0]="kiwi"
print(fruits)

fruits.append("orange")
print(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.insert(1,"lemon")
print(fruits)

fruits = ["apple","banana","cherry"]
fruits.remove("banana")
print(fruits)

fruits = ["apple","banana","cherry"]
print(fruits[-1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

fruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Tuplas

fruits = ("apple", "banana", "cherry")
print(fruits[0])
print(len(fruits))
print(fruits[-1])

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Conjuntos

fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)

fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Diccionarios

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

car["year"] = 2020
print(car)

car["color"] = "red"
print(car)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")
print(car)

car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()
print(car)

#condicionales

a = 50
b = 10
if a > b:
  print("Hello World")

if a == b:
  print("Yes")
else:
  print("No")

#Ciclo while

i = 1
while i < 6:
  print(i)
  i += 1

i = 1

while i < 6:
  if i == 3:
    break
  i += 1

print('\n')
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

print('\n')

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#Ciclo for

print('\n')
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

print('\n')

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
   continue
  print(x)

for x in range(6):
  print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Funciones

def my_function():
  print("Hello from a function")

my_function()

def my_function(fname, lname):
  print(fname)


def my_function(x):
  return x + 5

def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function('Andres','Juan','Pedro')

#Funciones lambda

x = lambda a : a

#clases

class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

class Student(Person):
  pass


class Person:
  def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()


#Modulos

# import mymodule
# import mymodule as mx

# import mymodule
# print(dir(mymodule))

# from mymodule import person1