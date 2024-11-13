function solve (numbers) {
    let evenSum = 0;
    let oddSum = 0;

    numbers.forEach(function (number) {
        if (number % 2 === 0) evenSum += number
        else oddSum += number
    })

    console.log(evenSum - oddSum)
}
