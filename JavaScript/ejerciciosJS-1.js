//Ejercicios en javascript

console.log('Hello world')

if (5 > 2) {
    console.log('Five is greater than two')
}

//This is a comment

/*
This is a comment
written in
more than a just line*/

let carname = 'Volvo',
    x = 50

x = 5
let y = 10

console.log(x + y)

let z = x + y
console.log(z)

x = y = z = 'Orange'
console.log(x, y, z)

function myFunc() {
    var x = "Fantastic"
}
console.log(typeof (x))

let arrayX = ['apple', 'banana', 'cherry']
console.log(typeof (arrayX))

const diccionario = { "name": "John", "age": 30 }
console.log(typeof (diccionario))

let b = true
console.log(typeof (b))

let num = 5
console.log(parseFloat(5))

let num2 = 5.5
console.log(parseInt(num2))

function complex(real, imag) {
    return { real: real, imag: imag };
}

let complejo = complex(3, 4);
console.log(complejo.real, '+', complejo.imag, 'i');

let cadena = "Hello world"
console.log(cadena.length)
console.log(cadena[0])

console.log(cadena.substring(2, 5))

cadena = ' Hello world '
cadena = cadena.trim()
console.log(cadena)

console.log(cadena.toUpperCase())
console.log(cadena.toLowerCase())

cadena = cadena.replace('H', 'J')
console.log(cadena)

let age = 36
cadena = `My name is John, and I am ${age}`
console.log(cadena)

console.log(10 > 9)
console.log(10 + 5)
console.log(10 - 5)
console.log(10 / 5)
console.log(10 * 5)

let fruits = ["apple", "banana"]

if (fruits.includes("apple")) {
    console.log("Yes, apple is a fruit!")
}

//Listas
fruits = ["apple", "banana", "cherry"]
console.log(fruits[1])

fruits[0] = "kiwi"
console.log(fruits)

fruits.push("orange")
console.log(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.splice(1, 0, "lemon")
console.log(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.splice(fruits.indexOf("banana"), 1)
console.log(fruits)

fruits = ["apple", "banana", "cherry"]
console.log(fruits[fruits.length - 1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for (let i = 2; i < 5; i++) {
    console.log(fruits[i])
}

fruits = ["apple", "banana", "cherry"]
console.log(fruits.length)

fruits = ["apple", "banana", "cherry"]  //No existen las tuplas en JS
console.log(fruits[0])
console.log(fruits.length)
console.log(fruits[fruits.length - 1])

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
for (let i = 2; i < 5; i++) {
    console.log(fruits[i])
}

fruits = ["apple", "banana", "cherry"]  //No existen los conjuntos en JS 
if (fruits.includes("apple")) {
    console.log("Yes, apple is a fruit")
}

fruits = ["apple", "banana", "cherry"]
fruits.push("orange")
console.log(fruits)

fruits = ["apple", "banana", "cherry"]
more_fruits = ["orange", "mango", "grapes"]
more_fruits.forEach(function (fruit) {
    fruits.push(fruit)
})
console.log(fruits)

fruits = ["apple", "banana", "cherry"]
fruits.splice(fruits.indexOf("banana"), 1)
console.log(fruits)

car = {
    brand: "Ford",
    model: "Mustang",
    year: 1964
}

console.log(car.brand) 

// Los diccionarios son similares a los
// objetos

car.year = 2020
console.log(car)

car.color = "red"
console.log(car)

car =	{
    brand : "Ford",
    model : "Mustang",
    year : 1964
}
delete(car.model)
console.log(car)

// car.clear()
console.log(car)

let a = 50
b = 10
if(a>b){
    console.log("Hello World")
}

if(a==b){
    console.log("Yes")
}else{
    console.log("No")
}

let i = 1
while(i<6){
    console.log(i)
    i+=1
}

i = 1

while(i<6){
    if(i == 3){
        break
    }
    i+=1
}

console.log('\n')
i = 0
while(i<6){
    i+=1
    if(i == 3){
        continue
    }
    console.log(i)
}

console.log('\n')

i = 1
while(i < 6){
    console.log(i)
    i+=1
}
console.log("i is no longer less than 6")

fruits = ["apple", "banana", "cherry"]
for(x of fruits){
    console.log(x)
}

console.log('\n')

for(x of fruits){
    if(x == "banana"){
        continue
    }
    console.log(x)
}

for(let x=0;x<6;x++){
    console.log(x)
}

fruits = ["apple", "banana", "cherry"]
for(x of fruits){
    if(x == "banana"){
        break
    }
    console.log(x)
}

function my_function(){
    console.log("Hello from a function")
}

my_function()

function my_function1(fname,lnmae){
    console.log(my_function1)
}

function my_function2(x){
    return x+5
}

function variosParametros(...kids){
    console.log("The youngest child is " + kids[2])
}

variosParametros('Andres','Juan','John')

let f = (a) => a

class MyClass{
    x = 5
}

let p1 = new MyClass()
console.log(p1.x)

class Person{
    constructor(name,age){
        this.name = name
        this.age = age
    }
}

class Student extends Person{

}

class Person1{
    constructor(fname){
        this.firstname = fname
    }
    printname() {
        console.log(this.firstname)
    }
}

class Student1 extends Person1{
    
}

let student = new Student1("Mike")
student.printname()

// import {myFunction} from './myModule'
// console.log(Object.keys(myFunction));

