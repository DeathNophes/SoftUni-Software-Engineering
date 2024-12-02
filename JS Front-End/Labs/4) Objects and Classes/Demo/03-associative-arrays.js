const replicant = {
    name: 'Bob',
    speed: 3000000000,
    'Current Location': undefined,
}
console.log( replicant );

console.log( replicant.hasOwnProperty('location') );

delete replicant;

console.log( replicant );