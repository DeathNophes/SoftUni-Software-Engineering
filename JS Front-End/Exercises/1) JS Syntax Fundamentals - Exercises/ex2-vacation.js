function solve (groupOfPeople, typeOfGroup, day) {

    let price;
    switch (typeOfGroup) {
        case "Students":
            if (day === 'Friday') price = groupOfPeople * 8.45
            else if (day === 'Saturday') price = groupOfPeople * 9.80
            else if (day === 'Sunday') price = groupOfPeople * 10.46

            // If the group is equal or bigger than 30 - 15% discount
            if (groupOfPeople >= 30) price *= 0.85

            break;
        case "Business":
            if (day === 'Friday') price = groupOfPeople * 10.90
            else if (day === 'Saturday') price = groupOfPeople * 15.60
            else if (day === 'Sunday') price = groupOfPeople * 16.00

            // If the group is equal or bigger than 100 - 10 of them can stay for free
            if (groupOfPeople >= 100) {
                if (day === 'Friday') price -= 10 * 10.90
                else if (day === 'Saturday') price -= 10 * 15.60
                else if (day === 'Sunday') price -= 10 * 16.00
            }

            break;
        case "Regular":
            if (day === 'Friday') price = groupOfPeople * 15.00
            else if (day === 'Saturday') price = groupOfPeople * 20.00
            else if (day === 'Sunday') price = groupOfPeople * 22.50

            // If the group is bigger than or equal to 10 and less than or equal to 20 - 5% discount
            if (groupOfPeople >= 10 && groupOfPeople <= 20) price *= 0.95

            break
    }
    console.log(`Total price: ${price.toFixed(2)}`)
}
