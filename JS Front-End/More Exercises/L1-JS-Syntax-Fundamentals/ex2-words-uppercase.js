function solve (text) {

    // Extract the words
    let words = text.match(/\w+/g);

    // Convert each word to uppercase
    let uppercaseWords = words.map(word => word.toUpperCase());

    // Join the words with ", " separator
    let result = uppercaseWords.join(', ');

    // Output the result
    console.log(result);
}
