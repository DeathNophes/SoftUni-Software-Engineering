function solve() {
    const infoEl = document.querySelector('#info span');
    const departBtn = document.querySelector('#depart');
    const arriveBtn = document.querySelector('#arrive');

    const baseUrl = `http://localhost:3030/jsonstore/bus/schedule/`;

    let nextStopId = `depot`;
    let currentStopName = ``;

    function depart() {
        fetch(baseUrl + nextStopId)
            .then(response => response.json())
            .then(data => {
                currentStopName = data['name'];
                nextStopId = data['next'];
                infoEl.textContent = `Next stop ${currentStopName}`;
            })
            .catch(error => console.error(error));

        // Change the buttons
        departBtn.setAttribute('disabled', 'true');
        arriveBtn.removeAttribute('disabled');

    }

    function arrive() {
        infoEl.textContent = `Arriving at ${currentStopName}`

        // Change the buttons
        departBtn.removeAttribute('disabled');
        arriveBtn.setAttribute('disabled', 'true');
    }

    return {
        depart,
        arrive
    };
}

let result = solve();