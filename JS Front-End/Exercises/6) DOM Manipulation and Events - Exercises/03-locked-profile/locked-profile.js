document.addEventListener('DOMContentLoaded', solve);

function solve() {

    document.querySelector('main').addEventListener('click', (e) => {

        // If the targeted element is not a button we don't do anything
        if ( e.target.nodeName !== 'BUTTON' ) return NaN;

        // We get the profile element (we have 3 of them) that is closest to our target
        const profileEl = e.target.closest('.profile');

        const state = profileEl
            .querySelector('.radio-group input:checked')
            .getAttribute('id')

        // If the field is locked we don't do anything
        if (state.includes('Lock')) return NaN;

        // We get the hidden fields
        const hiddenFields = profileEl.querySelector('.hidden-fields');

        // We perform the logic
        if ( hiddenFields.classList.contains('active') ) {
            hiddenFields.classList.remove('active');
            e.target.textContent = 'Show less'
        } else {
            hiddenFields.classList.add('active');
            e.target.textContent = 'Show more'
        }
    })
}