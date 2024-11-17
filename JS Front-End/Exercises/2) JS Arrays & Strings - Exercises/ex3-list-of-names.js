function solve (array) {

    let sortedArray = array.sort((a, b) => a.localeCompare(b))
    sortedArray.forEach(function (element, index) {
        console.log(`${index + 1}.${element}`)
    })
}
