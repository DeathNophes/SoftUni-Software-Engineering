function storeProducts(products) {
    const catalogue = {};

    products.forEach(pair => {
        const [name, price] = pair.split(' : ');

        // Initialize the letter category if it doesn't exist, and add the product
        catalogue[name[0]] = catalogue[name[0]] || {};
        catalogue[name[0]][name] = price;
    });

    // Sort the products within each letter category and the top-level keys
    Object.keys(catalogue).sort().forEach(letter => {
        const sortedProducts = Object.entries(catalogue[letter])
            .sort((a, b) => a[0].localeCompare(b[0]));

        // Change the original positions of the entries
        catalogue[letter] = Object.fromEntries(sortedProducts);
    });



    // Sort the keys and print the catalogue
    Object.keys(catalogue).sort().forEach(letter => {
        const entries = Object.entries(catalogue[letter]);

        console.log(letter);
        entries.forEach(([product, price]) => {
            console.log(`  ${product}: ${price}`);
        });
    });
}
