function townList (array) {
    let towns = [];

    for (const item of array) {
        const [town, latitude, longitude] = item.split(' | ')
        towns.push({
            'town': town,
            'latitude': Number(latitude).toFixed(2),
            'longitude': Number(longitude).toFixed(2),
        })
    }

    for (const obj of towns) {
        console.log(obj)
    }
}
