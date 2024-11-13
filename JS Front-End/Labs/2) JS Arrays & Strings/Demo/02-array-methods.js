const cars = ['BMW', 'Audi', 'Mercedes', 'Toyota', 'Mazda'];
console.log(cars);
console.log(cars[0]);

// Pop - remove last element (mutating)
const lastCar = cars.pop();
console.log(cars);
console.log(lastCar);

// Shift - remove first element (mutating)
const firstCar = cars.shift();
console.log(cars);
console.log(firstCar);
console.log(cars[0]);

// Unshift - add element in the beginning of the array (mutating)
cars.unshift('BMW');
console.log(cars);

// Splice - Remove element at position (mutating)
const removedCars = cars.splice(5, 1);
console.log(cars);
console.log(removedCars);

// Reverse - Reverses the array index (mutating)
const reversedCars = cars.reverse();
console.log(cars);
console.log(reversedCars);
console.log(cars === reversedCars);
cars.reverse();
console.log(cars);
console.log(reversedCars);

// Join - create string from array (non-mutating)
const carsList = cars.join(', ');
console.log(carsList);

// slice - return shallow copy if a portion of an array (non-mutating)
console.log(cars);
const bestCars = cars.slice(1, 4);
console.log(bestCars);

// includes - check if element is in the array (non-mutating)
const hasBmw = cars.includes('BMW');
console.log(hasBmw);

// Index of - check if element is in the array and return index (non-mutating)
const indexOfBmw = cars.indexOf('BMW');
console.log(indexOfBmw);

// Index of returns -1 if the element is not found (non-mutating)
const indexOfCitroen = cars.indexOf('Citroen');
console.log(indexOfCitroen);

// forEach - executes code for every element of the array (non-mutating) (iterative)
cars.forEach(function(car){
    console.log(car);
});

function stingToLowerCase(string){
    return string.toLowerCase();
}

// map - create a new array with values based on the original array (non-mutating) (iterative)
const lowercaseCars = cars.map(stingToLowerCase);

console.log(lowercaseCars);
console.log(cars);

// find - return the first value found in the array or undefined (non-mutating)(iterative)
const carWithT = cars.find(function(car){
    return car.startsWith('T');
});
console.log(carWithT);

// filter - find all elements based on condition (non-mutating) (iterative)
const carWithM = cars.filter(function(car){
    return car.startsWith('M');
});
console.log(carWithM);


