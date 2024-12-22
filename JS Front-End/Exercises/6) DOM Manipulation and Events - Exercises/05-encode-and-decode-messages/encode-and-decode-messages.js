document.addEventListener('DOMContentLoaded', solve);

function solve() {
    // Get the required elements
    const mainEl = document.querySelector('main');
    const encodeAreaEl = document.querySelector('#encode textarea');
    const decodeAreaEl = document.querySelector('#decode textarea');

    function encode (message) {
        return  message
            .split("") // Split string into array of characters
            .map(char => String.fromCharCode(char.charCodeAt(0) + 1)) // Increment ASCII value
            .join(""); // Join the array back to a string
    }

    function decode (message) {
        return message
            .split("") // Split string into array of characters
            .map(char => String.fromCharCode(char.charCodeAt(0) - 1)) // Decrement ASCII value
            .join(""); // Join the array back to a string
    }

    mainEl.addEventListener('click', (e) => {
        // We stop the refresh of the page
        e.preventDefault();

        if ( e.target.nodeName !== 'BUTTON' ) return NaN;

        switch (e.target.textContent) {
            case 'Encode and send it':
                const encodedMsg = encode(encodeAreaEl.value)
                encodeAreaEl.value = '';
                decodeAreaEl.value = encodedMsg;
                break;

            case 'Decode and read it':
                const decodedMsg = decode(decodeAreaEl.value);
                decodeAreaEl.value = decodedMsg
                break;
        }
    })
}