function solve (array) {
    const garage = {};

    array.forEach(car => {
        // We separate the garage number from the information
        const [garageNumber, carInfo] = car.split(' - ');
        // We create the entry in the object if it does not exist
        garage[garageNumber] = garage[garageNumber] || [];

        // We add the car into the garage
        garage[garageNumber].push(carInfo)
    })

    for (const [garageNumber, cars] of Object.entries(garage)) {
        console.log(`Garage № ${garageNumber}`);
        cars.forEach(car => {
            const formattedCar = car.replace(/: /g, ' - ');
            console.log(`--- ${formattedCar}`);
        })
    }
}
