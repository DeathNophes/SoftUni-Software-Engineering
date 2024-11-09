function solve (currentSpeed, area) {

    const motorwayLimit = 130;
    const interstateLimit = 90;
    const cityLimit = 50;
    const residentialLimit = 20;

    function withinTheLimit (speed, speedLimit) {
        console.log(`Driving ${speed} km/h in a ${speedLimit} zone`)
    }

    function aboveTheLimit (speed, speedLimit) {
        let status = '';
        let difference = speed - speedLimit

        if (speed <= speedLimit + 20) status = 'speeding'
        else if (speed <= speedLimit + 40) status = 'excessive speeding'
        else status = 'reckless driving'

        console.log(`The speed is ${difference} km/h faster than the allowed speed of ${speedLimit} - ${status}`)
    }

    function processSpeed (speed, speedLimit) {
        if (speed <= speedLimit) {
            withinTheLimit(speed, speedLimit)
        } else {
            aboveTheLimit(speed, speedLimit)
        }
    }


    switch (area) {
        case "motorway":
            processSpeed(currentSpeed, motorwayLimit)
            break;

        case "interstate":
            processSpeed(currentSpeed, interstateLimit)
            break;

        case "city":
            processSpeed(currentSpeed, cityLimit)
            break;

        case "residential":
            processSpeed(currentSpeed, residentialLimit)
    }
}
