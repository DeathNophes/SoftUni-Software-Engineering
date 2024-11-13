function solve (text, replacementWord) {
    let newText = text.replaceAll(replacementWord, '*'.repeat(replacementWord.length))
    console.log(newText)
}
