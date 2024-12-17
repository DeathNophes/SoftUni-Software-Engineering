function solve() {
    // Get all the elements
    const inputEl = document.querySelector('#input');
    const outputEl = document.querySelector('#output');
    // Get the sentences in the input
    const sentences = inputEl.value.split('. ');
    // Set the maximum amount of sentences a paragraph can hold
    const sentPerPar = 3;

    // Get the number of paragraphs we need to generate
    const numberOfParagraphs = Math.ceil(sentences.length / sentPerPar);

    let output = '';
    for (let i = 0; i < numberOfParagraphs; i++) {
        // We create a constant that tell us where we stand with every iteration
        const start = i * sentPerPar;
        const end = start + sentPerPar;

        output += '<p>'
        output += sentences.slice(start, end).join('. ')
        output += '</p>'
    }

    outputEl.innerHTML = output
}