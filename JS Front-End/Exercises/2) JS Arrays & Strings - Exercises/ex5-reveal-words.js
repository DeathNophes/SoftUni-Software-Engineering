function solve (words, sentence) {
    words = words.split(', ') // We turn the string into an array

    // We make a loop and iterate through all the words
    for (let w of words) {
        sentence = sentence.replace('*'.repeat(w.length), w);
    }

    console.log(sentence)
}
