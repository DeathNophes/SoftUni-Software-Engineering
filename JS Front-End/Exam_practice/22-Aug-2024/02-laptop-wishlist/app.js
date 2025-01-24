window.addEventListener("load", solve);

function solve() {
    // Function that creates the desired element with their properties
    function createElement (tag, properties, container) {
        const element = document.createElement(tag);

        Object.keys(properties).forEach(key => {
            if (typeof properties[key] === 'object') {
                Object.assign(element[key], properties[key]);
            } else {
                element[key] = properties[key];
            }
        })

        if ( container ) container.append(element);

        return element;
    }

    // Get all the elements
    const inputs = [...document.querySelectorAll('form.laptop-info input')];
    const btnAddElement = document.querySelector('#add-btn');

    const listCheckElement = document.querySelector('#check-list');
    const listWishElement = document.querySelector('#laptops-list');

    const btnClearElement = document.querySelector('#laptops-container button.clear')

    // Create the event listeners
    btnAddElement.addEventListener('click', addHandler);
    btnClearElement.addEventListener('click', clearHandler)

    function createEntry ({ model, storage, price }) {
        // li.laptop-item > article > p, p, p, < button.btn.edit, button.btn.ok
        const entryEl = createElement('li', {className: 'laptop-item', dataset: {model, storage, price}}, listCheckElement);
        const articleEl = createElement('article', {}, entryEl);
        createElement('p', {textContent: model}, articleEl);
        createElement('p', {textContent: 'Memory: ' + storage + ' TB'}, articleEl);
        createElement('p', {textContent: 'Price: ' + price + '$'}, articleEl);
        createElement('button', {onclick: editHandler,className: 'btn edit', textContent: 'edit'}, entryEl)
        createElement('button', {onclick: confirmHandler,className: 'btn ok', textContent: 'ok'}, entryEl)

    }

    function addHandler (e) {
        e.preventDefault();
        const [ model, storage, price ] = inputs.map(field => field.value);

        if (! model || ! storage || ! price) return;

        createEntry({ model, storage, price });

        inputs.forEach(field => field.value = '');
        btnAddElement.disabled = true;

    }

    function clearHandler (e) {
        e.preventDefault();

        listWishElement.innerHTML = '';
    }

    function editHandler (e) {
        e.preventDefault();

        const entryEl = e.target.closest('li');
        const values = Object.values(entryEl.dataset);

        inputs.forEach((field, index) => field.value = values[index]);
        entryEl.remove();

        btnAddElement.disabled = false;

    }

    function confirmHandler (e) {
        e.preventDefault();

        const entryEl = e.target.closest('li');
        entryEl.remove()
        listWishElement.appendChild(entryEl)

        entryEl.querySelectorAll('button').forEach(btn => btn.remove());
        btnAddElement.disabled = false;

    }
}
  