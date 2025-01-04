function attachEvents() {
    // Get all the elements
    const outputEl = document.querySelector('#messages');
    const inputs = document.querySelectorAll('#controls input[name]');
    const buttonSubmitEl = document.querySelector('#submit');
    const buttonRefreshEl = document.querySelector('#refresh');

    // Get the base URL
    const baseUrl = 'http://localhost:3030/jsonstore/messenger';

    buttonSubmitEl.addEventListener('click', () => {

        // From Node list to an array
        const [author, content] = [...inputs].map(field => field.value);

        // Check if there are inputs, if not return null
        if (! author || ! content) return;

        const body = {author, content}

        fetch(baseUrl, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify(body)
        })
            .then(response => response.json())
            .then(() => {
                buttonRefreshEl.click();
                // Clear the input fields
                inputs.forEach(field => field.value = '');
            })
            .catch(error => console.error(error))

    })

    buttonRefreshEl.addEventListener('click', () => {
        // Clear everything in the output field
        outputEl.textContent = '';

        fetch(baseUrl)
            .then(response => response.json())
            .then(messages => {

                // Combine messages into a single string
                outputEl.textContent = Object
                    .values(messages)
                    .map(message => `${message.author}: ${message.content}`)
                    .join('\n');

            })
            .catch(error => console.error(error))
    })

}

attachEvents();