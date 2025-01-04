
function loadContacts (baseUrl, onSuccess) {
    fetch(baseUrl)
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error))
}

function createContact (baseUrl, contact, onSuccess) {
    fetch(baseUrl, {
        method: 'POST',
        body: JSON.stringify(contact)
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error))
}

function deleteContact (baseUrl, contact, onSuccess) {
    fetch(baseUrl + '/' + contact._id, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error))
}

function createElement (tag, properties, container = null) {
    const element = document.createElement(tag);
    Object.keys(properties).forEach(key => {
        if ( typeof properties[key] === 'object') {
            Object.assign(element.dataset, properties[key])
        } else {
            element[key] = properties[key];
        }
    })

    if (container) container.append(element);

    return element;
}

function init() {
    // Get the elements
    const btnLoadEl = document.querySelector('#btnLoad');
    const btnCreateEl = document.querySelector('#btnCreate');
    const phonebookEl = document.querySelector('#phonebook');

    // URL
    const baseUrl = 'http://localhost:3030/jsonstore/phonebook';

    loadContacts(baseUrl, (result) => {
        Object.values(result).forEach(createEntry)
    })

    function createEntry ({person, phone, _id}) {
        const entryEl = createElement(
            'li',
            {
                textContent: `${person}: ${phone}`,
                dataset: {person, phone, _id}
            },
            phonebookEl
        )

        createElement('button', {textContent: 'Delete', onclick: deleteEntryHandler}, entryEl)
    }

    function createEntryHandler () {
        const inputs = document.querySelectorAll('input[type="text"][id]')
        const [person, phone] = [...inputs].map(field => field.value)

        if ( ! person || ! phone ) return;

        const contact = { person, phone };

        createContact(baseUrl, contact, (result) => {
            createEntry(result);
        })

        inputs.forEach(el => el.value = '');

    }

    function deleteEntry (contact) {
        phonebookEl.querySelector(`li[data-_id="${contact._id}"]`).remove()
    }

    function deleteEntryHandler (e) {
        const entryEl = e.target.closest('li');
        const contact = Object.assign({}, entryEl.dataset)

        deleteContact(baseUrl, contact, (result) => {
            deleteEntry(result)
        })

    }

    btnCreateEl.addEventListener('click', createEntryHandler);
}

document.addEventListener('DOMContentLoaded', init);