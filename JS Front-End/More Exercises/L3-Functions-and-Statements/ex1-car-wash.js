function solve (array) {

    let result = 0;

    const commands = {
        'soap': () => result += 10,
        'water': () => result *= 1.20,
        'vacuum cleaner': () => result *= 1.25,
        'mud': () => result *= 0.90
    }

    for (let i = 0; i < array.length; i++) {
        switch (array[i]) {
            case 'soap': commands["soap"](); break;
            case 'water': commands["water"](); break;
            case 'vacuum cleaner': commands["vacuum cleaner"](); break;
            case 'mud': commands["mud"](); break;
        }
    }

    console.log(`The car is ${result.toFixed(2)}% clean.`)
}
