function createDictionary(input) {
    const dictionary = {};

    // Loop through the input array to process each JSON string
    input.forEach(jsonString => {
        const parsedObject = JSON.parse(jsonString); // Convert JSON string to object
        const [term, definition] = Object.entries(parsedObject)[0]; // Extract term and definition
        dictionary[term] = definition; // Add or update the term in the dictionary
    });

    // Get sorted terms (keys of the dictionary)
    const sortedTerms = Object.keys(dictionary).sort();

    // Print the sorted terms and their definitions
    sortedTerms.forEach(term => {
        console.log(`Term: ${term} => Definition: ${dictionary[term]}`);
    });
}
