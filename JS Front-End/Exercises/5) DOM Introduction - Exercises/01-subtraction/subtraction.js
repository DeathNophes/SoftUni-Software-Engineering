function subtract() {
    // Get all the elements
    const inputElFirst = document.querySelector('#firstNumber');
    const inputElSecond = document.querySelector('#secondNumber');
    const resultEl = document.querySelector('#result');
    // Perform the calculation and assign it into a constant
    const result = Number(inputElFirst.value) - Number(inputElSecond.value);
    // Show the result on the resultEl, fixed to the second decimal point
    resultEl.textContent = result;
}