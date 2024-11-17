function solve (array) {
    const bitcoinPrice = 11949.16; // Price of 1 bitcoin in lev
    const gramOfGold = 67.51; // Price of 1 gram of gold in lev
    let currentDay = 0; // Day of mining

    let firstPurchasedBitcoinDay = 0;
    let purchasedBitcoins = 0;
    let totalMoney = 0;

    array.forEach(function (number) {
        currentDay += 1;
        let amount = number * gramOfGold // We get the total earned money
        if (currentDay % 3 === 0) {
            amount *= 0.7; // Every third day 30% of the money for that day is stolen
        }
        totalMoney += amount; // We add the money earned from the current day
        while (totalMoney >= bitcoinPrice) {
            totalMoney -= bitcoinPrice;
            if (purchasedBitcoins === 0) {
                firstPurchasedBitcoinDay = currentDay;
            }
            purchasedBitcoins += 1;
        }
    })

    console.log(`Bought bitcoins: ${purchasedBitcoins}`)
    if (purchasedBitcoins > 0) {
        console.log(`Day of the first purchased bitcoin: ${firstPurchasedBitcoinDay}`)
    }
    console.log(`Left money: ${totalMoney.toFixed(2)} lv.`)
}
