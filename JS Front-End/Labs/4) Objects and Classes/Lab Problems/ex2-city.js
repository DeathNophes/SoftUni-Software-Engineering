function city (cityObject) {
    const entries = Object.entries(cityObject);

    for (const [property, value] of entries) {
        console.log(`${property} -> ${value}`)
    }
}
