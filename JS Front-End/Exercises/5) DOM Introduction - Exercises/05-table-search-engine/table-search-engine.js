function solve() {
    // Get the table elements and the search string
    const students = document.querySelectorAll('table tbody tr');
    const searchStrEl = document.querySelector('#searchField');
    const searchStrValue = searchStrEl.value.toLowerCase().trim()

    // If there is no input at the search field => stop the program and do nothing
    if (searchStrValue === '') return false;
    // Reset the search field value
    searchStrEl.value = '';

    // Iterate through all the elements to look for matches
    students.forEach( student=> {
        student.classList.remove('select');
        if (student.textContent.toLowerCase().includes(searchStrValue)) {
            student.classList.add('select')
        }
    })
}