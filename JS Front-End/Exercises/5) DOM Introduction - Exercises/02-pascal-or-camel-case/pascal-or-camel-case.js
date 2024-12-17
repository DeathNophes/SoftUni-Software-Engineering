function solve() {
    // Take the inputText as an array of words with lowercase letters
    const inputText = document.querySelector('#text').value.toLowerCase().split(' ');
    // Take the naming convention's value, turn it to lowercase and trim it, so it is easier
    const convention = document.querySelector('#naming-convention').value.toLowerCase().trim();
    // Take the resultElement
    const resultElement = document.querySelector('#result');

    function capitaliseWord (word) {
        return word[0].toUpperCase() + word.slice(1)
    }

    // Create the switch with the naming convention
    switch (convention) {
        case 'camel case':
            resultElement.textContent = inputText[0] + inputText.slice(1).map(capitaliseWord).join('')
            break;
        case 'pascal case':
            resultElement.textContent = inputText.map(capitaliseWord).join('')
            break;
        default:
            resultElement.textContent = 'Error!'
    }
}