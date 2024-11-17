function solve (array, step) {

    const newArr = []
    for (let i = 0; i < array.length; i++) {
        if (i % step === 0) newArr.push(array[i])
    }

    return newArr
}
