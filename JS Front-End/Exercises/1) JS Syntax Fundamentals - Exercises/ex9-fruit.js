function solve (typeOfFruit, weightInGrams, pricePerKilogram) {

    let weightInKilograms = weightInGrams / 1000;
    let money = weightInKilograms * pricePerKilogram

    console.log(`I need $${money.toFixed(2)} to buy ${weightInKilograms.toFixed(2)} kilograms ${typeOfFruit}.`)
}
