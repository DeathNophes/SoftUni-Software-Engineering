function solve() {
    // Get all the elements
    const inputEl = document.querySelector('#input').value;
    const toElStr = document.querySelector('#selectMenuTo').value.toLowerCase();
    const resultEl = document.querySelector('#result');

    // Turn a number from decimal to binary (2)
    function decimalToBinary(N) {
        return (N >>> 0).toString(2);
    }

    // Turn a number from decimal to hexadecimal (16)
    function decimalToHexadecimal (N) {
        return (N >>> 0).toString(16).toUpperCase()
    }

    if (toElStr === 'binary') {
        resultEl.value = decimalToBinary(Number(inputEl));
    } else if (toElStr === 'hexadecimal') {
        resultEl.value = decimalToHexadecimal(Number(inputEl));
    }
}