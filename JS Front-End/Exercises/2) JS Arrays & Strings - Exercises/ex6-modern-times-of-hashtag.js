function solve (text) {
    const regexPattern = RegExp("#[A-Za-z]+", 'g');
    let matches = text.match(regexPattern);
    let updatedMatches = matches.map(str => str.replace("#", ''));

    // let updatedMatches = matches.map(function (str) {return str.replace("#", '')})
    console.log(updatedMatches.join('\n'))
}
