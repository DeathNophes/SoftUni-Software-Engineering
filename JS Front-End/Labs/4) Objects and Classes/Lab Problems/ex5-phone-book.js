function phoneBook (input) {
    let assocArr = {};

    for (const pair of input) {
        const [name, phone] = pair.split(' ');
        assocArr[name] = phone
    }

    for (let key in assocArr) {
        console.log(key + ' -> ' + assocArr[key])
    }
}
