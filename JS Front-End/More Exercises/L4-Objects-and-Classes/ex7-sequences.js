function solve (array) {
    const sequences = [];

    array.forEach(arr => {
        // Parse the string into an array of numbers
        const numbersArray = JSON.parse(arr);
        // Sort the array in descending order
        const sortedArray = numbersArray.sort((a, b) => b - a)

        // Check if this sequence already exists in the array
        let exists = false;
        sequences.forEach(sequence => {
            if (JSON.stringify(sortedArray) === JSON.stringify(sequence)) {
                exists = true
            }
        })

        // If the sequence does not exist - add it in the array
        if (exists === false) {
            sequences.push(sortedArray)
        }
    })

    // Sort the sequences by length
    sequences.sort((a, b) => a.length - b.length);

    sequences.forEach(sequence => {
        console.log(`[${sequence.join(', ')}]`)
    })
}
