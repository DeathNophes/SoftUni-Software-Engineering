function getInfo() {
    // Get all the elements and the input value
    const inputEl = document.querySelector('#stopId');
    const stopNameDivEl = document.querySelector('#stopName');
    const busesListEl = document.querySelector('#buses');

    // Construct the URL
    const url = `http://localhost:3030/jsonstore/bus/businfo/${inputEl.value}`;

    // Clear the list before a new request is sent
    busesListEl.innerHTML = '';

    fetch(url)
        .then(response => response.json())
        .then(busStop => {
            Object
                .entries(busStop['buses'])
                .forEach(bus => {
                    const newLi = document.createElement('li');
                    newLi.textContent = `Bus ${bus[0]} arrives in ${bus[1]} minutes`
                    busesListEl.appendChild(newLi);
                })
            stopNameDivEl.textContent = busStop['name'];
        })
        .catch(error => {
            stopNameDivEl.textContent = 'Error';
            console.error(error);
        })
}