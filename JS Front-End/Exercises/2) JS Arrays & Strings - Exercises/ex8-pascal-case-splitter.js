function solve (string) {
    const regexPattern = RegExp("[A-Z][a-z]*", "g");
    let matches = string.match(regexPattern);
    console.log(matches.join(', '))
}
