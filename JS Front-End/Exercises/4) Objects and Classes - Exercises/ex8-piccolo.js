function piccolo (array) {
    let parkingLot = {};

    for (let i = 0; i < array.length; i++) {
        const [direction, carNumber] = array[i].split(', ')

        if (direction === 'IN') {
            if (! parkingLot.hasOwnProperty(carNumber)) parkingLot[carNumber] = 1;
        } else {
            if (parkingLot.hasOwnProperty(carNumber)) delete parkingLot[carNumber];
        }
    }

    if (Object.entries(parkingLot).length > 0) {
        Object.entries(parkingLot)
            .sort()
            .forEach(pair => console.log(pair[0]))
    } else {
        console.log('Parking Lot is Empty')
    }
}
