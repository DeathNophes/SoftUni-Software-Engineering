function organizeShelves(input) {
    const shelves = {}; // To store shelves and their books

    input.forEach(line => {
        if (line.includes("->")) {
            // Create a shelf if id is not taken
            const [id, genre] = line.split(" -> ");
            if (!shelves.hasOwnProperty(id)) {
                shelves[id] = { genre, books: [] };
            }
        } else if (line.includes(":")) {
            // Add a book to the appropriate shelf
            const [bookInfo, genre] = line.split(", ");
            const [title, author] = bookInfo.split(": ");
            for (const id in shelves) {
                if (shelves[id].genre === genre) {
                    shelves[id].books.push({ title, author });
                    break;
                }
            }
        }
    });

    // Sort shelves by book count in descending order
    const sortedShelves = Object.entries(shelves)
        .sort((a, b) => b[1].books.length - a[1].books.length);

    // Print the output
    sortedShelves.forEach(([id, shelf]) => {
        console.log(`${id} ${shelf.genre}: ${shelf.books.length}`);
        shelf.books
            .sort((a, b) => a.title.localeCompare(b.title))
            .forEach(book => console.log(`--> ${book.title}: ${book.author}`));
    });
}