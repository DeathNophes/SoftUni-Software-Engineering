document.addEventListener('DOMContentLoaded', solve);

function solve() {
    //Get the elements
    const inputElDays = document.querySelector('#days-input');
    const inputElHours = document.querySelector('#hours-input');
    const inputElMinutes = document.querySelector('#minutes-input');
    const inputElSeconds = document.querySelector('#seconds-input');

    // We will use seconds for the original converting as it is the smallest value
    const values = { days: 86400, hours: 3600, minutes: 60, seconds: 1};

    // We add the REFERENCE to the function to all submit buttons (best practise)
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', handleSubmitEvent)
    })

    function handleSubmitEvent (e) {
        e.preventDefault();

        const currentInputEl = e.target.querySelector('input[type="number"]');
        const currentValue = Number(currentInputEl.value);

        if (currentValue < 1) return false;

        const key = currentInputEl.getAttribute('id').split('-input')[0];
        const multiplier = values[key];

        updateValues( currentValue * multiplier )
    }

    function updateValues (secondsAmount) {
        inputElDays.value = Number( secondsAmount / values.days ).toFixed(2);
        inputElHours.value = Number( secondsAmount / values.hours ).toFixed(2);
        inputElMinutes.value = Number( secondsAmount / values.minutes ).toFixed(2);
        inputElSeconds.value = Number( secondsAmount / values.seconds ).toFixed(2);
    }
}