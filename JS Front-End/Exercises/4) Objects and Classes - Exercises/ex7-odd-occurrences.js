function solve (input) {

    const words = input.toLowerCase().split(' ');
    const matched = words.reduce((matched, word) => ({...matched, [word]: 0}), {});

    words.forEach(word => {
        if (matched.hasOwnProperty(word)) matched[word] += 1
    })

    const output = Object
        .entries(matched)
        .filter(el => el[1] % 2 !== 0)
        .reduce((output, [word, count]) => output + word + ' ', '')

    console.log(output)
}
