function convertToJSON (name, lastName, hairColor) {
    const inputAsObject = {
        name: name,
        lastName: lastName,
        hairColor: hairColor,
    }

    const inputAsJSON = JSON.stringify(inputAsObject);

    console.log(inputAsJSON);
}
