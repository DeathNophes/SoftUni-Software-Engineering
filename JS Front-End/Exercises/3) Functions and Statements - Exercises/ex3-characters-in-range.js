function solve (char1, char2) {

    // We use min() and max() to get start and end ASCII numbers
    // We use charCodeAt(0) because we treat the strings as arrays, and an index is required by that method
    const start = Math.min(char1.charCodeAt(0), char2.charCodeAt(0));
    const end = Math.max(char1.charCodeAt(0), char2.charCodeAt(0));
    let result = [];

    for (let i = start + 1; i < end; i++) {
        result.push(String.fromCharCode(i))
        // We use this method to add the character to the result array
    }

    console.log(result.join(' '))
}
