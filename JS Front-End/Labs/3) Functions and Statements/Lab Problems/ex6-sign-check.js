function solve (numOne, numTwo, numThree) {
    const array = [numOne, numTwo, numThree];
    const negativeNumbers = array.filter(num => num < 0).length;

    if (negativeNumbers % 2 === 0) {
        console.log('Positive')
    } else {
        console.log('Negative')
    }
}
