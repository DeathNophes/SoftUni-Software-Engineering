function extract(elementId) {
    const text = document.querySelector('#' + elementId).textContent;
    const pattern = new RegExp('\\(([^()]+)\\)', 'g')

    return [...text.matchAll(pattern)].map(el => el[1]).join('; ')
}