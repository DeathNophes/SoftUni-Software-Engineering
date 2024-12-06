function storeProvisioning (stock, ordered) {
    let storage = {};

    for (let i = 0; i < stock.length; i += 2) {
        const foodItem = stock[i];
        storage[foodItem] = Number(stock[i + 1]);
    }

    for (let i = 0; i < ordered.length; i += 2) {
        const foodItem = ordered[i];
        const foodQuantity = Number(ordered[i + 1])

        if ( ! storage.hasOwnProperty(foodItem)) storage[foodItem] = 0;
        storage[foodItem] += foodQuantity;
    }

    for (let key in storage) {
        console.log(`${key} -> ${storage[key]}`)
    }
}
