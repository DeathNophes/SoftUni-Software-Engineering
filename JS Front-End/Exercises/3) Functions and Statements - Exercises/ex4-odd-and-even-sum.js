function solve (number) {

    const digits = number.toString().split('').map(Number)
    const evenSum = digits.filter(d => d % 2 === 0).reduce((sum, d) => sum + d, 0)
    const oddSum = digits.filter(d => d % 2 !== 0).reduce((sum, d) => sum + d, 0)

    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)

    // const numAsString = String(number);
    // let evenSum = 0;
    // let oddSum = 0;

    // for (let i = 0; i < numAsString.length; i++) {
    //     const num = Number(numAsString[i]);

    //     if (num % 2 === 0) {
    //         evenSum += num
    //     } else {
    //         oddSum += num
    //     }
    // }

    // console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`)
}

