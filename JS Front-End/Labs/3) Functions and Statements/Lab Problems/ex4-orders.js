function solve (product, quantity) {
    const coffeePrice = 1.50;
    const waterPrice = 1.00;
    const cokePrice = 1.40;
    const snacksPrice = 2.00;
    let result = 0;

    switch (product) {
        case 'coffee': result = (quantity * coffeePrice); break;
        case 'water': result = (quantity * waterPrice); break;
        case 'coke': result = (quantity * cokePrice); break;
        case 'snacks': result = (quantity * snacksPrice); break;
    }

    console.log(result.toFixed(2))
}
