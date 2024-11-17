function solve (base, increment) {
    const layers = Math.ceil(base / 2); // We find how many layers there will be
    const height = Math.floor(layers * increment)
    let currentBase = base;

    let materials = {
        "Stone": 0,
        "Marble": 0,
        "Lapis Lazuli": 0,
        "Gold": 0
    }

    for (let i = 1; i < layers; i++) {
        const totalBlocks = currentBase ** 2
        let outerLayer = (currentBase * 4) - 4;
        let innerLayer = totalBlocks - outerLayer;

        if (i % 5 === 0) {
            materials['Lapis Lazuli'] += outerLayer * increment
        } else {
            materials['Marble'] += outerLayer * increment
        }

        materials['Stone'] += innerLayer * increment
        currentBase -= 2;
    }

    materials['Gold'] += (currentBase ** 2) * increment


    for (let key in materials) {
        console.log(`${key} required: ${Math.ceil(materials[key])}`)
    }
    console.log(`Final pyramid height: ${height}`);
}
