//Ejercicios en javascript

console.log('Hello world')

if(5>2){
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

console.log(x+y)

let z = x+y
console.log(z)

x = y = z = 'Orange'
console.log(x,y,z)

function myFunc(){
    var x = "Fantastic"
}
console.log(typeof(x))

let arrayX = ['apple','banana','cherry']
console.log(typeof(arrayX))

const diccionario = {"name":"John","age":30}
console.log(typeof(diccionario))

let b = true
console.log(typeof(b))

let num = 5
console.log(parseFloat(5))

let num2 = 5.5
console.log(parseInt(num2))

function complex(real, imag) {
    return {real: real, imag: imag};
}

let complejo = complex(3, 4);
console.log(complejo.real,'+',complejo.imag,'i'); 

let cadena = "Hello world"
console.log(cadena.length)
console.log(cadena[0])

console.log(cadena.substring(2,5))

cadena = ' Hello world '
cadena = cadena.trim()
console.log(cadena)

console.log(cadena.toUpperCase())
console.log(cadena.toLowerCase())

cadena = cadena.replace('H','J')
console.log(cadena)

let age = 36
cadena = `My name is John, and I am ${age}`
console.log(cadena)

console.log(10>9)
console.log(10+5)
console.log(10-5)
console.log(10/5)
console.log(10*5)

let fruits = ["apple", "banana"]

if(fruits.includes("apple")){
    console.log("Yes, apple is a fruit!")
}

fruits = ["apple", "banana", "cherry"]
console.log(fruits[1])

fruits[0]="kiwi"
console.log(fruits)