function solve (word, text) {

    // We turn the text to lowercase and split it into an array
    const textArray = text.toLowerCase().split(' ')

    if (textArray.includes(word.toLowerCase())) {
        console.log(word)
    } else {
        console.log(`${word} not found!`)
    }
}
