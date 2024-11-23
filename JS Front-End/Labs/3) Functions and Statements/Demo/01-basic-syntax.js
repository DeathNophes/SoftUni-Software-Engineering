// Function Declaration
function printText(text) {
    console.log(text);
}

// Invoking function
printText('Something to log');

// Function hoisting
printSumResult(10, 20); // This can be called before initialisation

function printSumResult(first, second){
    console.log(first+second);
}

// Function expression
const substractNumbers = function(a, b) {
    console.log(a - b);
}

substractNumbers(3, 2);

// Return statement
function calculateSum(a, b) {
    return a + b;
}

// Save returned value as a variable
const result = calculateSum(10, 40);
console.log(result);

// Execute methon on returned result
const formattedResult = calculateSum(5,3).toFixed(2);
console.log(formattedResult);

// use in expression
const expressionResult = calculateSum(3,6) * 10;
console.log(expressionResult);

// create a function that validates array index
function isValidArrayIndex(arr, index) {

    let isValid = true;

    if ( ! Number.isInteger(index) ) {
        isValid = false;
    }

    if ( index < 0 || index >= arr.length ) {
        isValid = false;
    }

    return isValid;
}

console.log( isValidArrayIndex([1,2,3], 2) );
console.log( isValidArrayIndex([1,2,3], 4) );
console.log( isValidArrayIndex([1,2,3]) );

// Default Value
function printHeader() {
    console.log('header');
}

const defaultReturn = printHeader();
console.log(defaultReturn);

// IIFE - Immediately Invoked Function Expression
(function(){
    console.log('IIFE');
})();

// IIAE
(() => console.log('IIAE'))();
