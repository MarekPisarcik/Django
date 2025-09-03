

let meno = "Janko";
let age = 32;
let isStudent = false;

console.log(`Ahoj, volám sa ${meno}, mám ${age} a som študent: ${isStudent}.`);

/*
let number = prompt("Zadaj číslo:");

if (number > 0) {
    console.log("Pozitívne");
} else if (number < 0) {
    console.log("Negatívne");
} else {
    console.log("Nula");
}
*/

for (let i = 0; i <= 10; i++) {
    console.log(i);
}

let fruits = ["jablko", "banán", "hruška", "pomaranč"];
for (let fruit of fruits) {
    console.log(fruit);
}

function sum(a, b) {
    return a + b;
}
console.log(sum(5, 10));


function greet(name) {
    return `Ahoj, ${name}!`;
}

console.log(greet("Janko"));


let person = {
    name: "Janko",
    age: 32,
    city: "Nitra"
};

console.log(`Moje meno je ${person.name}, mám ${person.age} a bývam v ${person.city}`);


let day = 3;
switch (day) {
    case 1:
        console.log("Pondelok");
        break;
    case 2:
        console.log("Utorok");
        break;
    case 3:
        console.log("Streda");
        break;
    case 4:
        console.log("Štvrtok"); 
        break;
    case 5:
        console.log("Piatok");
        break;
    case 6:
        console.log("Sobota");
        break;
    case 7:
        console.log("Nedeľa");
        break;
    default:
        console.log("Neplatný deň");
}