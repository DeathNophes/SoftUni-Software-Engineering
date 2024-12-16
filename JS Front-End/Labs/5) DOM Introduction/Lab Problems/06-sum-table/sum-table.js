function sumTable() {
    // Get all the price elements and the sum element
    const priceElements = document.querySelectorAll('table tbody tr:not(:last-child) td:last-child');
    const sumElement = document.querySelector('#sum');
    // Add them to a result
    // Show the result on the sum field
    sumElement.textContent = [...priceElements]
        .map(el => Number(el.textContent))
        .reduce((sum, num) => sum + num, 0)
        .toFixed(2);
}