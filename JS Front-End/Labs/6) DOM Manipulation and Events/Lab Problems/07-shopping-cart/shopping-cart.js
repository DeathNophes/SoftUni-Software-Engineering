document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const resultEl = document.querySelector('textarea[disabled]');
    const prodCatalogueEl = document.querySelector('.shopping-cart');

    const products = {};

    prodCatalogueEl.addEventListener('click', (event) => {
        // We only proceed if a button is clicked
        if (event.target.nodeName !== 'BUTTON') return false;

        // We are getting the class of the button we clicked
        switch (event.target.getAttribute('class')) {
            case 'add-product':
                const productEl = event.target.closest('.product');
                const productName = productEl.querySelector('.product-title').textContent;
                const productPrice = Number(productEl.querySelector('.product-line-price').textContent);

                resultEl.value += `Added ${productName} for ${productPrice.toFixed(2)} to the cart.\n`

                // We want to show the final price of all the products
                if (! products.hasOwnProperty(productName)) products[productName] = 0;
                products[productName] += productPrice

                break;

            case 'checkout':
                // We take all the keys from the products
                const productNames = Object.keys(products)

                // We get the total price of the products
                const totalPrice = productNames.reduce((price, name) => price + products[name], 0);

                resultEl.value += `You bought ${productNames.join(', ')} for ${totalPrice.toFixed(2)}.`

                prodCatalogueEl.querySelectorAll('button').forEach(el => {
                    el.setAttribute('disabled', 'disabled');
                })

                break;
        }
    })
}
