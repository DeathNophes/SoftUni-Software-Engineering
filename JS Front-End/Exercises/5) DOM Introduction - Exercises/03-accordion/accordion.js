function toggle() {
    // Get the extra element
    const extraEl = document.querySelector('#extra');
    const buttonEl = document.getElementsByClassName('button')[0];

    // Check whether it is toggled or not and perform the action
    if (buttonEl.textContent === 'More') {
        extraEl.style.display = 'block';
        buttonEl.textContent = 'Less';
    } else {
        extraEl.style.display = 'none';
        buttonEl.textContent = 'More';
    }
}