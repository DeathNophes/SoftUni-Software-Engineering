function employeesList (array) {
    let employees = {};

    for (const name of array) {
        employees[name] = name.length
    }

    for (let key in employees) {
        console.log(`Name: ${key} -- Personal Number: ${employees[key]}`)
    }
}
