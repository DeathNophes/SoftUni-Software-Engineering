function solve (input) {
    let sortedArray = input.sort((a, b) => a - b) // Sort the array from smallest to biggest
    let inputLength = input.length

    let result = []
    for (let i = 0; i < inputLength; i++) {
        if (i % 2 === 0) {
            const el = sortedArray.shift() // The first element (smallest)
            result.push(el)
        } else {
            const el = sortedArray.pop() // The last element (biggest)
            result.push(el)
        }
    }

    return result;
}
