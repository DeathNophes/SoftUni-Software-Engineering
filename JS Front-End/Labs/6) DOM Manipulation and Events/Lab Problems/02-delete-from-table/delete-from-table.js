function deleteByEmail() {
    // Get all the elements
    const inputStr = document.querySelector('input[name="email"]').value;
    const peopleEmails = document.querySelectorAll('table tbody tr td:last-child');
    const resultEl = document.querySelector('#result');

    if (! inputStr) return false;

    // Delete the required person
    peopleEmails.forEach(email => {
        if (email.textContent === inputStr) {
            email.parentElement.remove();
            resultEl.textContent = 'Deleted'
        } else {
            resultEl.textContent = "Not found."
        }
    })

    inputStr.value = '';
}
