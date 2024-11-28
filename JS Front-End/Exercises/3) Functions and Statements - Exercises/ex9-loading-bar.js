function solve (num) {
    const barsLength = 10;
    const barsFilled = '%'.repeat(num / barsLength);
    const barsLeft = '.'.repeat(barsLength - barsFilled.length);

    if (num === 100) {
        console.log(`${num}% Complete!\n[${barsFilled}]`)
    } else {
        console.log(`${num}% [${barsFilled + barsLeft}]\nStill loading...`)
    }
}
