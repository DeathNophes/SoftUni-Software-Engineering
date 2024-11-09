function solve (startingYield) {

    if (startingYield < 100) {
        console.log(0)
        console.log(0)
        return;
    }

    const workerConsumables = 26;
    let currentYield = startingYield;

    let days = 0;
    let extractedSpice = 0;

    while (currentYield >= 100) {
        extractedSpice += currentYield;     // Every day that amount is extracted from the yield
        currentYield -= 10;                 // Every day we extract, the yield loses 10 of its amount
        days += 1;                          // Counts the days we extract

        extractedSpice -= workerConsumables; // Every day the workers take their share
    }

    // When the mine is no longer profitable workers get one more payment
    extractedSpice -= workerConsumables

    // Workers cannot receive more spice than there is in storage
    if (extractedSpice < 0) extractedSpice = 0;

    console.log(days)
    console.log(extractedSpice)
}
