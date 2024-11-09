function solve (number) {

    const numberAsString = number.toString()
    let sum = 0;
    let flag = true;

    for (let i = 0; i < numberAsString.length; i++) {
        sum += Number(numberAsString[i]);

        if (numberAsString[i] !== numberAsString[i + 1] && i < numberAsString.length - 1) {
            flag = false;
        }
    }

    console.log(flag)
    console.log(sum)
}
