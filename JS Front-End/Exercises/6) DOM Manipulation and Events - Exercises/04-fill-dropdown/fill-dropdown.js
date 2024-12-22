document.addEventListener('DOMContentLoaded', solve);

function solve() {
    // Get all the elements
    const newItemTextEl = document.querySelector('#newItemText');
    const newItemValueEl = document.querySelector('#newItemValue');
    const selectEl = document.querySelector('#menu');

    const addBtnEl = document.querySelector('form input[type="submit"]');

    addBtnEl.addEventListener('click', (e) => {
        // We stop the page refresh
        e.preventDefault();

        const text = newItemTextEl.value;
        const value = newItemValueEl.value;

        const newOptionEl = document.createElement('option');
        newOptionEl.textContent = text;
        newOptionEl.value = value;

        selectEl.append(newOptionEl);

        newItemTextEl.value = '';
        newItemValueEl.value = '';

    })
}