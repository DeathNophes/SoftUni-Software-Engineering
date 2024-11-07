function solve (num1, num2) {
    let sum = 0;
    let log = '';
    for (let i = num1; i <= num2; i++) {
        log += i + ' ';
        sum += i;
    }
    console.log(log)
    console.log(`Sum: ${sum}`)
}
