function convertToObject (text) {
    const textAsObject =  JSON.parse(text);
    const entries = Object.entries(textAsObject);

    for (const [property, value] of entries) {
        console.log(`${property}: ${value}`)
    }
}
