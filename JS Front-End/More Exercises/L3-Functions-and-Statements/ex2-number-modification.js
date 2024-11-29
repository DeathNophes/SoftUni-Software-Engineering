function solve (num) {
    const numAsArray = num.toString().split('') // We make it an array

    const calculateAvgDigit = (arr) => {
        let sum = 0;
        for (let i = 0; i < arr.length; i++) {
            sum += Number(arr[i])
        }
        return (sum / arr.length);
    }

    while (calculateAvgDigit(numAsArray) <= 5) {
        numAsArray.push('9')
    }

    console.log(Number(numAsArray.join('')))
}
