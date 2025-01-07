function loadMatches (baseUrl, onSuccess) {
    fetch(baseUrl)
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error));
}

function createMatch (baseUrl, match, onSuccess) {
    fetch(baseUrl, {
        method: 'POST',
        body: JSON.stringify(match)
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error));
}

function updateMatch (baseUrl, match, onSuccess) {
    fetch(baseUrl + match._id, {
        method: 'PUT',
        body: JSON.stringify(match)
        })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error));
}

function deleteMatch (baseUrl, match, onSuccess) {
    fetch(baseUrl + match._id, {
        method: 'DELETE'
    })
        .then(response => response.json())
        .then(onSuccess)
        .catch(error => console.error(error));
}

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

function init () {
    const baseUrl = 'http://localhost:3030/jsonstore/matches/';

    const fields = [...document.querySelectorAll('#form form input[type="text"]')];
    const listEl = document.querySelector('#list');
    const addMatchBtn = document.querySelector('#add-match');
    const editMatchBtn = document.querySelector('#edit-match');

    addMatchBtn.addEventListener('click', createHandler);
    editMatchBtn.addEventListener('click', updateHandler);

    function loadEntries () {
        listEl.innerHTML = '';
        loadMatches(baseUrl, (result) => {
            Object.values(result).forEach(createEntry)
        })
    }

    function createEntry ({ host, score, guest, _id }) {
        const entryEl = createElement('li', {className: 'match', dataset: {host, score, guest, _id}}, listEl);
        const infoEl = createElement('div', {className: 'info'}, entryEl);
        createElement('p', {textContent: host}, infoEl);
        createElement('p', {textContent: score}, infoEl);
        createElement('p', {textContent: guest}, infoEl);
        const buttonsEl = createElement('div', {className: 'btn-wrapper'}, entryEl);
        createElement('button', {className: 'change-btn', textContent: 'Change'}, buttonsEl);
        createElement('button', {className: 'delete-btn', textContent: 'Delete'}, buttonsEl);

        buttonsEl.querySelector('.change-btn').addEventListener('click', changeHandler);
        buttonsEl.querySelector('.delete-btn').addEventListener('click', deleteHandler);
    }

    function deleteEntry ({host, score, guest, _id}) {
        listEl.querySelector(`li[data-_id="${_id}"]`).remove()
    }

    function createHandler (e) {
        e.preventDefault();

        const [ host, score, guest ] = fields.map(field => field.value);

        if (! host || ! score || ! guest) return;

        const match = {host, score, guest};

        createMatch(baseUrl, match, (result) => {
            createEntry(result);
        })

        fields.forEach(field => field.value = '');

    }

    function changeHandler (e) {
        const entryEl = e.target.closest('li');
        const values = Object.values(entryEl.dataset);

        entryEl.classList.add('active');

        fields.forEach((field, index) => field.value = values[index]);

        addMatchBtn.disabled = true;
        editMatchBtn.disabled = false;
    }

    function updateHandler (e) {
        e.preventDefault();

        const [ host, score, guest ] = fields.map(field => field.value);

        const entryEl = listEl.querySelector('.active');

        if (! host || ! score || ! guest) return;

        const match = {host, score, guest, _id: entryEl.dataset._id};

        updateMatch(baseUrl, match, (result) => {
            loadEntries();
            fields.forEach(field => field.value = '');
            addMatchBtn.disabled = false;
            editMatchBtn.disabled = true;
        })
    }

    function deleteHandler (e) {
        const entryEl = e.target.closest('li');
        const match = Object.assign({}, entryEl.dataset);

        deleteMatch(baseUrl, match, (result) => {
            deleteEntry(result)
        })
    }

    loadEntries();
}

document.addEventListener('DOMContentLoaded', init)