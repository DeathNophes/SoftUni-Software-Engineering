document.addEventListener('DOMContentLoaded', () => {
    const baseUrl = 'https://api.restful-api.dev/objects';
    const listEl = document.querySelector('#list');

    document.querySelector('#load').addEventListener('click', () => {

        // const responsePromise = fetch(baseUrl);

        // responsePromise
        //     .then(response => {
        //         response.json()
        //             .then(result => {
        //                 console.log(result);
        //             })
        //     })
        //     .catch(error => {
        //         console.log(error);
        //     })

        fetch(baseUrl)
            .then(response => response.json())
            .then(result => {
                // console.log(result);

                result.forEach(item => {
                    console.log(item.name);

                    listEl.append(
                    Object.assign( document.createElement('li'), { textContent: item.name } )
                    )

                })
            })
            .catch(error => console.error(error));
    });

    document.querySelector('#post').addEventListener('click', () => {

        const data = {
           "name": "Apple MacBook Pro 16",
           "data": {
              "year": 2019,
              "price": 1849.99,
              "CPU model": "Intel Core i9",
              "Hard disk size": "1 TB"
           }
        }

        fetch(baseUrl, {
            method: 'POST',
            headers: { "content-type": "application/json" },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            })
            .catch(error => console.error(error));

        const id = "ff808181932badb601938dbd65fb0286";

        fetch(baseUrl + `/${id}`, {
            method: 'PUT',
            headers: { "content-type": "application/json" },
            body: JSON.stringify(data)
        })
            .then(response => response.json())
            .then(result => {
                console.log(result);
            })
            .catch(error => console.error(error));

    });

    document.querySelector('#getdata').addEventListener('click', getDataHandler);

    async function getDataHandler() {
        try {

            const response = await fetch(baseUrl);
            const result = await response.json();

            console.log(result);

        } catch (error) {
            console.error(error);
        }
    }

});