window.addEventListener("load", solve);

function solve() {
  // Get all the elements
    const eventNameEl = document.querySelector('#name');
    const eventDateEl = document.querySelector('#time');
    const eventDescriptionEl = document.querySelector('#description');
    const addBtnEl = document.querySelector('#add-btn');
    const previewListEl = document.querySelector('#preview-list');
    const archiveListEl = document.querySelector('#archive-list');

    // Function for creating the <li> and attaching the event listeners
    function createEventPreview (name, date, description, onEdit, onNext) {
        const previewEl = document.createElement('li')
        previewEl.innerHTML = `
            <article>
                <p>${name}</p>
                <p>${date}</p>
                <p>${description}</p>
            </article>
            <div class="buttons">
                <button class="edit-btn">Edit</button>
                <button class="next-btn">Next</button>
            </div>
        `

        // Attach event listeners directly
        const editBtn = previewEl.querySelector('.edit-btn');
        const nextBtn = previewEl.querySelector('.next-btn');

        // Use addEventListener to bind the handlers
        editBtn.addEventListener('click', (e) => onEdit(e));
        nextBtn.addEventListener('click', (e) => onNext(e));

        return previewEl;

    }

    // Function to handle the edit button
    function editHandler (e) {
            const closestLiElement = e.target.closest('li')
            const previewName = closestLiElement.querySelector('article p:nth-child(1)').textContent
            const previewDate = closestLiElement.querySelector('article p:nth-child(2)').textContent
            const previewDesc = closestLiElement.querySelector('article p:nth-child(3)').textContent

            eventNameEl.value = previewName
            eventDateEl.value = previewDate
            eventDescriptionEl.value = previewDesc

            closestLiElement.remove()
            addBtnEl.disabled = false
        }

    // Function to handle the next button
    function nextHandler (e) {
        const closestLiElement = e.target.closest('li')
        closestLiElement.querySelector('div .buttons').remove();

        const archiveBtnElement = document.createElement('button');
        archiveBtnElement.classList.add('archive-btn');
        archiveBtnElement.textContent = 'Archive';
        closestLiElement.appendChild(archiveBtnElement);

        archiveListEl.appendChild(closestLiElement);

        archiveBtnElement.addEventListener('click', (e) => {
            const closestLiElement = e.target.closest('li');
            closestLiElement.remove();
            addBtnEl.disabled = false
        })
    }

    // Helper function to clear the input fields
    function clearInputFields () {
        eventNameEl.value = '';
        eventDateEl.value = '';
        eventDescriptionEl.value = '';
    }

    // Event listener for the add button
    addBtnEl.addEventListener('click', (e) => {
        e.preventDefault();
        if (! eventNameEl.value || ! eventDateEl.value || ! eventDescriptionEl.value) return;

        const previewElement = createEventPreview(
            eventNameEl.value, eventDateEl.value, eventDescriptionEl.value, editHandler, nextHandler
        )

        previewListEl.appendChild(previewElement)

        addBtnEl.disabled = true
        clearInputFields()

    })
}