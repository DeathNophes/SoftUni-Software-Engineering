function sortAddressBook (input) {
    let addressBook = {};

    for (const line of input) {
        const [name, address] = line.split(':');
        addressBook[name] = address
    }

    let sorted = Object.entries(addressBook)
    sorted.sort((a, b) => a[0].toLowerCase().localeCompare(b[0].toLowerCase()))

    for (const [name, address] of sorted) {
        console.log(name + ' -> ' + address);
    }
}
