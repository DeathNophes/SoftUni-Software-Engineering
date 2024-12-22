document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const emailEl = document.querySelector('#email');
    const pattern = new RegExp('[a-z]+@[a-z]+\\.[a-z]+', 'g')

    emailEl.addEventListener('change', (event) => {

        if ( !pattern.test(event.currentTarget.value) ) {
            event.currentTarget.classList.add('error');
        } else {
            event.currentTarget.classList.remove('error');
        }
    });
}
