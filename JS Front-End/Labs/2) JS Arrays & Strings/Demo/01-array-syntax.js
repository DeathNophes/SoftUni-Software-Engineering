// Array literal
const names = ['Bob', 'Bill', 'Garfield', 'Riker'];

// Declare empty array
const empty = [];

// Dynamic length
console.log(empty.length);
console.log(empty);
empty.length = 10;
console.log(empty.length);
console.log(empty);

// Mixed Array
const mixed = ['Bob', true, 20, undefined]; // not recommended
console.log(mixed);

// Dense vs Sparse array
const denseArr = [undefined, undefined, undefined];
const sparseArr = []
sparseArr.length = 3;

console.log( denseArr.length === sparseArr.length );
console.log( denseArr );
console.log( sparseArr );

// Numbers Array
const digits = [0,1,2,3,4,5,6,7,8,9];
console.log(digits);

console.log(digits[0]);
console.log(digits[digits.length-1]);

// Access non-existing elements returns undefined
console.log(digits[40]);
console.log(digits[-1]);

// Set element
console.log(names);

names[0] = 'Marvin';
names[2] = 'Luke';
names[names.length] = 'Bender';

console.log(names);

// Array destructuring assignment
const [ firstName, secondName, thirdName, forthName, fifthName ] = names;

// Partial destructuring
// const [ firstName, secondName ] = names;

console.log(firstName);
console.log(secondName);
console.log(thirdName);
console.log(forthName);
console.log(fifthName)

// Partial destructuring using spread operator
const [ fName, sName, ...restNames] = names;

console.log(names);
console.log(fName);
console.log(sName);
console.log(restNames);

// iterate over array with for
for (let i = 0; i < names.length; i++){
    console.log(names[i]);
}

// iterate over array with for-of
console.log('--------------- for-of ---');
for ( const name of names ) {
    console.log(name);
}


// Comparing references
const a = [1, 2, 3];
const b = [1, 2, 3];

console.log(a == b);
console.log(a === b);