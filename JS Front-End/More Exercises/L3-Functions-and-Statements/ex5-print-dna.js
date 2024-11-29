function printDna (length) {
    const sequence = 'ATCGTTAGGG' // The repeating sequence
    let index = 0;

    for (let i = 0; i < length; i++) {
        const firstSymbol = sequence[index % sequence.length];
        const secondSymbol = sequence[(index + 1) % sequence.length];
        index += 2 // Moves symbols ahead in the sequence

        if (i % 4 === 0) {
            console.log(`**${firstSymbol}${secondSymbol}**`)
        } else if (i % 4 === 1) {
            console.log(`*${firstSymbol}--${secondSymbol}*`)
        } else if (i % 4 === 2) {
            console.log(`${firstSymbol}----${secondSymbol}`)
        } else if (i % 4 === 3) {
            console.log(`*${firstSymbol}--${secondSymbol}*`)
        }
    }
}
