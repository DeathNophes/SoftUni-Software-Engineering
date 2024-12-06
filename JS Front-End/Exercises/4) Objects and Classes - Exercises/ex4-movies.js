function solve(input) {

    const movies = {};

    input.forEach((line) => {

        if ( line.includes('addMovie') ) {

            const [_, name] = line.split('addMovie ');
            movies[name] = { name };

        } else if ( line.includes('directedBy') ) {

            const [name, director] = line.split(' directedBy ');
            movies[name] ??= {};
            movies[name].director = director;

        } else if ( line.includes('onDate') ) {

            const [name, date] = line.split(' onDate ');
            movies[name] ??= {};
            movies[name].date = date;

        }
    });

    for (const movie in movies) {
        if ( Object.keys(movies[movie]).length > 2 ) console.log(JSON.stringify(movies[movie]));
    }

}
