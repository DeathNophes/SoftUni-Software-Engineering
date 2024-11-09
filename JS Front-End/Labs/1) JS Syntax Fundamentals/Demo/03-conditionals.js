// Arithmetic Operators

function arithmeticOperators(){
    
    let a = 15;
    let b = 5;
    let c;
    
    c = a + b; // 20
    console.log(c);
    
    c = a - b; // 10
    console.log(c);
    
    c = a * b; // 75
    console.log(c);
    
    c = a / b; // 3
    console.log(c);
    
    c = a % b; // 0
    console.log(c);
    
    c = a ** b; // 15**5 = 759375c
    console.log(c);
}

arithmeticOperators();

// Comparison Operators
function comparisonOperators() {
    console.log(1 == '1'); // true
    console.log(1 === '1'); // false
    console.log(3 != '3'); // false
    console.log(3 !== '3'); // true
    console.log(5 < 5.5); // true
    console.log(5 <= 4); // false
    console.log(2 > 1.5); // true
    console.log(2 >= 2); // true
}

comparisonOperators();

// Ternary Operator
console.log((5 > 7) ? 4 : 10); // 10

// If else
let a = 5;
let b = 10;

console.log( a, b );

if ( a > b ) {
    console.log('A is larger than B');
} else if ( a < b ) {
    console.log('A is smaller than B');
} else {
    console.log('A is equal to B');
}

let c = 200;

if ( typeof c === 'number' ) {
    // c can be 0 and still be valid check
}

if ( c === 0 ) {
    // c is the number zero
}


// Switch example
// Switch is used when we need to check for alist of specific values of a variable
const price = 1.60;
const expr = 'Papayas';

switch (expr) {
    case 'Oranges':
        if ( price < 1 ) {
            console.log('Cheap stuff here');
        } else {
            console.log('Expensive stuff here');
        }
        console.log('Oranges are $0.59 a pound.');
        break;
    case 'Mangoes':
        console.log('Oranges are $0.59 a pound.');
        break;
    case 'Papayas':
        console.log('Mangoes and papayas are $2.79 a pound.');
        break;
    default:
        console.log(`Sorry, we are out of ${expr}.`);
}

// Truthy and Falsy values 

function logTruthiness(val) {
    if (val) {
        console.log("Truthy!");
    } else {
        console.log("Falsy.");
    }
}

logTruthiness(3.14); // Truthy!
logTruthiness({}); // Truthy!
logTruthiness(NaN); // Falsy.
logTruthiness("NaN"); // Truthy!
logTruthiness ([]); // Truthy!
logTruthiness(null); // Falsy.
logTruthiness(""); // Falsy.
logTruthiness(undefined); // Falsy.
logTruthiness (0); // Falsy.
