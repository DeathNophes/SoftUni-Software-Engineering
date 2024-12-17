function solve() {
    
    const input = document.querySelector('#inputs textarea').value;

    const outputBestRestEl = document.querySelector('#outputs #bestRestaurant p');
    const outputWorkersEl = document.querySelector('#outputs #workers p');

    if ( ! input ) return;

    const restaurant = JSON.parse(input)
        .reduce((acc, entry) => {
           
            const [ name, workersData ] = entry.split(' - ');
            
            const workers = workersData.split(', ')
                .map(workerData => {

                    const [ name, salary ] = workerData.split(' ');

                    return { name, salary: Number(salary) }
                });

            if ( ! acc.hasOwnProperty(name) ) {
                acc[name] = {
                    workers: []
                }
            }
            acc[name].workers.push(...workers);

            return acc;
            
        }, {})

    function getAvgSalary(restaurantData) {
        const allSalaries = restaurantData.workers.reduce((allSalaries, w) => allSalaries + w.salary, 0);
        return allSalaries / restaurantData.workers.length;
    }

    const bestRestaurantKey = Object.keys(restaurant)
        .sort((a, b) => getAvgSalary(restaurant[b]) - getAvgSalary(restaurant[a]))[0];

    const bestWorkers = restaurant[bestRestaurantKey].workers
        .toSorted((a, b) => b.salary - a.salary);

    outputBestRestEl.textContent = `Name: ${bestRestaurantKey} `;
    outputBestRestEl.textContent += `Average Salary: ${getAvgSalary(restaurant[bestRestaurantKey]).toFixed(2)} `
    outputBestRestEl.textContent += `Best Salary: ${bestWorkers[0].salary.toFixed(2)}`;

    outputWorkersEl.textContent = bestWorkers.map(w => `Name: ${w.name} With Salary: ${w.salary}`).join(' ');

}