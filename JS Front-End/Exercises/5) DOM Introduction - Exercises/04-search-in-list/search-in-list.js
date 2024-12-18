function solve() {
    // We get towns as a Node List
    const towns = document.querySelectorAll('#towns li');
    // We get the string from the search bar turned to lowercase
    const searchStr = document.querySelector('#searchText').value.toLowerCase();
    // We get the result element
    const resultEl = document.querySelector('#result');

    // If there is nothing on the search bar we stop the program
    if (searchStr === '') return NaN;

    // We create a variable to store our matches
    let matches = 0;

    // We iterate through every item see if there is a match
    towns.forEach(town => {
        // Before the if statements we make sure to set everything
        // to be with the default values and in that way we are not running another cycle
        town.style.fontWeight = 'normal';
        town.style.textDecoration = 'none';

        // We see if there is a match
        if (town.textContent.toLowerCase().includes(searchStr)) {
            town.style.fontWeight = 'bold';
            town.style.textDecoration = 'underline';
            matches += 1;
        }
    })

    // We show the matches
    resultEl.textContent = `${matches} matches found`
}
