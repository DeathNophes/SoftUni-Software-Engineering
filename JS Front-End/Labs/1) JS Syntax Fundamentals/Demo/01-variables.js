// use `let` and `const` to declare variables

// Rule: Always use `const` until we know that we
// ----- will need to change the value of the variable

let fullName = 'Iliyan Parmashki'; // Using camelCase for variable names
const age = 38; 

console.log( fullName, age );

/*
 * `let` and `const` – use block scope
 * when declared inside a block {} can NOT be accessed
 * from outside the block 
 * - - - - - - - - - - */

/*
 * Data Types:
 *
 * Number, Boolean, String, undefined, null
 * Symbol, BigInt (We will not use these)
 * Array, Object
 * - - - - - - - - - - */

let number = 10; // Number
let person = { name: 'George', age: 25 }; // Object
let array = [1, 2, 3]; // Array
let isTrue = true; // Boolean
let name = 'George'; // String
let empty = null; // null
let unknown = undefined; // undefined

// Change the value of the Variable
// There is no problem to change the value of the variable to a different type
fullName = 50;

console.log( fullName );

if ( fullName == 'Iliyan Parmashki' ) {
    var test = '123'; // var is the old way of declaring variables, it is not used anymore
}

/*
 * `var` – use function scope
 * can be accessed anywhere in the function,
 * including outside the initial block
 * - - - - - - - - - - */

console.log(test);