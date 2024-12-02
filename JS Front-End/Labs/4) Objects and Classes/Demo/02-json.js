let secondCat = {
    name: 'Aria',
    age: 1,
    hairAmount: 'Lots',
    'does-it-like-to-be-petted': true,
    weight_in_grams: 800,
}

// Covert object to JSON
let secondCatAsJSON = JSON.stringify(secondCat);
console.log( secondCatAsJSON );
console.log( typeof secondCatAsJSON );

// Convert JSON to object
let convertedFromJSON = JSON.parse(secondCatAsJSON);
console.log( convertedFromJSON );
console.log( typeof convertedFromJSON );


let jsonString = '{ "testKey":"testValue", "testKey2":"testValue2" }';
let objectFromStringVar = JSON.parse( jsonString );
console.log( objectFromStringVar );
console.log( typeof objectFromStringVar );

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

// Covert object with method to JSON
let replicantAsJSON = JSON.stringify(replicant);
console.log( replicantAsJSON );
console.log( typeof replicantAsJSON );