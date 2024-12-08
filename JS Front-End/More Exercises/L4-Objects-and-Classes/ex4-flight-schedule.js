function solve (array) {
    const flightsArray = array[0];
    const changesArray = array[1];
    const statusCheck = array[2][0];

    let flights = {};

    flightsArray.forEach(flight => {
        const [sector, destination] = flight.split(' ');

        flights[sector] = {'Destination': destination, 'Status': 'Ready to fly'};
    })

    changesArray.forEach(flight => {
        const [sector, status] = flight.split(' ');
        if (flights.hasOwnProperty(sector)) {
            flights[sector]['Status'] = status
        }
    })

    for (let key in flights) {
        if (flights[key]['Status'] === statusCheck) {
            console.log(flights[key])
        }
    }
}
