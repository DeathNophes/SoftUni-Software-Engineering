class Storage {
    constructor(capacity) {
        this.capacity = capacity;
        this.storage = [];
        this.totalCost = 0;
    }

    addProduct (product) {
        this.storage.push(product)
        this.totalCost += product['price'] * product['quantity']
        this.capacity -= product['quantity']
    }

    getProducts () {
        // We return the storage, which is an array of objects,
        // so we turn every product into string then join them
        return this.storage.map(product => JSON.stringify(product)).join('\n')
    }
}
