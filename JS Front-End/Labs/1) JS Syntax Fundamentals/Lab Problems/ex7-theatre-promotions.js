function solve (day, age) {
    let result;

    // Check if age is within the valid range
    if (age < 0 || age > 122) {
        console.log("Error!")
        return;
    }

    // Determine the price based on day and age
    switch (day) {
        case 'Weekday':
            if (age >= 0 && age <= 18) {result = 12}
            else if (age > 18 && age <= 64) {result = 18}
            else if (age > 64 && age <= 122) {result = 12}
            break;
        case 'Weekend':
            if (age >= 0 && age <= 18) {result = 15}
            else if (age > 18 && age <= 64) {result = 20}
            else if (age > 64 && age <= 122) {result = 15}
            break;
        case 'Holiday':
            if (age >= 0 && age <= 18) {result = 5}
            else if (age > 18 && age <= 64) {result = 12}
            else if (age > 64 && age <= 122) {result = 10}
            break;
    }

    // Output the result
    console.log(result + "$")
}
