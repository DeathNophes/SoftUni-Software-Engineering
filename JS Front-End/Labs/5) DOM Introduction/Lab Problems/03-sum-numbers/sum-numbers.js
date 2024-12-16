function calc() {
    // Get the first and the second elements plus the sum
    const num1Element = document.querySelector('#num1');
    const num2Element = document.querySelector('#num2');
    const sumElement = document.querySelector('#sum');
    // Calculate the sum and expose it
    sumElement.value = Number(num1Element.value) + Number(num2Element.value);
}