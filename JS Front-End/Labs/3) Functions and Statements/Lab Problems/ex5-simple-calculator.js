function solve (x, y, operator) {

    const operations = {
        'add': (a, b) => a + b,
        'subtract': (a, b) => a - b,
        'multiply': (a, b) => a * b,
        'divide': (a, b) => a / b
    }

    console.log(operations[operator](x, y))
}