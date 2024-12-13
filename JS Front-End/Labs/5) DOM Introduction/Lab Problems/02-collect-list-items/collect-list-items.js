function extractText() {
    // Get all list elements
    const listElements = document.querySelectorAll('ul li');
    // Get textarea element
    const textareaElement = document.querySelector('#result');
    // Update the textContent of the textarea
    for (let el of listElements) {
        textareaElement.value += el.textContent + '\n'
    }
}
