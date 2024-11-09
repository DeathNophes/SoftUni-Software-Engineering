
// Function Declaration
function solve(num1, num2) {
    console.log( num1 + num2 );
}

// Invoking the function
solve(5, 10);

function gradeText(name, grade) {
    // Concatenation
    console.log('The name is: ' + name + ', grade: ' + grade.toFixed(2) );
    // Interpolation
    console.log(`The name is: ${name}, grade: ${grade.toFixed(2)}`);
}

gradeText('Koko', 3.652);
