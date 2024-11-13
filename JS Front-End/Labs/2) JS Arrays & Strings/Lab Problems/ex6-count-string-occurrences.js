function solve (text, searchWord) {
    const pattern = new RegExp(`\\b${searchWord}\\b`, 'g')
    let matches = text.match(pattern) || []
    console.log(matches.length)
}
