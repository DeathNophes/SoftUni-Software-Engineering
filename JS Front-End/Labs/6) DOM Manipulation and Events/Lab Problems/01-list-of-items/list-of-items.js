function addItem() {
    // Get all the elements
    const inputEl = document.querySelector('#newItemText');
    const itemsListEl = document.querySelector('#items');

    if (! inputEl.value) return false;

    // Create new li element with the text
    const newListEl = document.createElement('li');
    newListEl.textContent = inputEl.value;

    // Attach the new element to the list
    itemsListEl.appendChild(newListEl);

    // Reset the text inside the input field
    inputEl.value = '';
}
