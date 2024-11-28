function solve (array) {
    for (let i = 0; i < array.length; i++) {
        const normalNum = array[i].toString();
        const reversedNum = normalNum.split('').reverse().join('')

        if (normalNum === reversedNum) {
            console.log(true)
        } else {
            console.log(false)
        }
    }
}
