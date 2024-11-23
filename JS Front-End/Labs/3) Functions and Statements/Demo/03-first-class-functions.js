// Function that takes another function as a parameter
function executeOperation(operation, firstOperand, secondOperand) {
    return operation(firstOperand, secondOperand);
}

function sum(a, b) {
    return a + b;
}

// pass function by reference
const operationResult = executeOperation(sum, 10, 20);
console.log(operationResult); // 30

// pass anonymous function as an argument
const operationResult2 = executeOperation(function(a, b){
    return a - b;
}, 10, 2);
console.log(operationResult2);

// pass arrow function as an argument
const operationResult3 = executeOperation((a, b) => a * b, 2, 5);
console.log(operationResult3); // 10

// function can be assigned a value to a variable
// using a function expression (anonymous function)
const multiply = function(a, b) {
    return a * b;
}
console.log( multiply(2, 3) );

// using arrow function
const divide = (a, b) => a / b;
console.log(divide(10, 5));

// Returned by another function
function buildOperation(operationName){
    switch (operationName) {
        case 'sum':
            return function(a, b) {
                return a + b;
            }
        case 'multiplication':
            return function(a, b) {
                return a * b;
            }
    }
}

const sumOperation = buildOperation('sum');
console.log( sumOperation(20, 40) );
const multiplicationOperation = buildOperation('multiplication');
console.log( multiplicationOperation(20, 40) );