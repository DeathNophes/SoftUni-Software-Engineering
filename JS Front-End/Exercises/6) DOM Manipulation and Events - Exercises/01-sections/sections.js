document.addEventListener('DOMContentLoaded', solve);

function solve() {
   // Get the elements we will work with
    const formEl = document.querySelector('#task-input');
    const contentEl = document.querySelector('#content');

    formEl.addEventListener('submit', (e) => {
        e.preventDefault() // We do this to not refresh the page

        const sections = formEl.querySelector('input[type="text"]').value.split(', ')

        sections.forEach(el => {
            const newDivEl = document.createElement('div');
            const newParEl = document.createElement('p');

            newParEl.style.display = 'none'
            newParEl.textContent = el;

            newDivEl.append(newParEl);
            newDivEl.addEventListener('click', (e) => {
                e.target.querySelector('p').style.display = 'block';
            })

            contentEl.append(newDivEl);
        })
    })
}