// Object literal
let firstCat = { name: 'Zuza', age: 8 }
console.log( firstCat );

// Multiline literal
let secondCat = {
    name: 'Aria',
    age: 1,
    hairAmount: 'Lots',
    'does-it-like-to-be-petted': true,
    weight_in_grams: 800,
}

// Empty object
let someCat = {}

// Set property dynamically - with dot syntax
someCat.name = 'Boban';
someCat.age = 2;
someCat.isMale = true;

// Set property dynamically - with bracket syntax
someCat['isCrazy'] = true;

// Set property programmatically & dynamically - with bracket syntax
let sanityCheck = 'isCrazy';
console.log( someCat[sanityCheck] );

// Declare a method in object literal
const replicant = {
    name: 'Bob',
    isMoving: true,
    status: function(){
        console.log('Working on stuff ...');
    },
    isBusy: () => {
        console.log('Not busy ... atm.');
    },
    isAnnoyed() {
        console.log('Not annoyed');
    },
}

replicant.status();
replicant.isBusy();
replicant.isAnnoyed();

replicant.isBusy = () => {
    console.log('Always busy!');
}

replicant.isBusy();

const cup = {
    glassType: 'dasd',
    weight: '120g',
}


firstCat.sister = secondCat;
someCat.sister = secondCat;

console.log(secondCat);
console.log('---');
console.log(firstCat);
console.log(someCat);

secondCat.hairAmount = 'Not that much ...';
console.log('/////// After change');
console.log(secondCat);
console.log('---');
console.log(firstCat);
console.log(someCat);

// Object keys
console.log( Object.keys(secondCat) );

// Object values
console.log( Object.values(secondCat) );

// Object entries
console.log( Object.entries(secondCat) );

console.log( typeof secondCat.name );
console.log( typeof firstCat.sister );

console.log('---');

const secondCatKeys = Object.keys(secondCat);

for ( const key in secondCat ) {
    console.log(key, secondCat[key]);
}

for ( const key of secondCatKeys ) {
    console.log(key, secondCat[key]);
}

secondCatKeys.forEach(key => console.log(key, secondCat[key]));
