function solve (input) {
    // We get the heroes count
    const heroesCount = input.shift();

    // We only include the heroes here
    const heroesInput = input.splice(0, heroesCount);

    // We get the heroes team
    const heroes = heroesInput.reduce((heroes, hero) => {
        // Split every string with the right element and create the object
        let [name, powers, energy] = hero.split('-');
        powers = powers.split(',');
        heroes[name] = { powers, energy: Number(energy)}
        return heroes;
    }, {})

    // We iterate through all entries
    input.forEach(entry => {

        if (entry === 'Evil Defeated!') {
            Object
                .entries(heroes)
                .forEach(el => {
                    const name = el[0];
                    const powers = el[1].powers.join(', ');
                    const energy = el[1].energy;

                    console.log(`Superhero: ${el[0]}`)
                    console.log(`- Superpowers: ${powers}`)
                    console.log(`- Energy: ${energy}`)
                })
            return;
        }

        const line = entry.split(' * ');
        const command = line.shift();
        const name = line.shift();

        switch (command) {
            case ('Use Power'):
                const [ superpower, energyRequired ] = line;

                if (heroes[name].powers.includes(superpower) && heroes[name].energy >= energyRequired) {
                    heroes[name].energy -= energyRequired
                    console.log(`${name} has used ${superpower} and now has ${heroes[name].energy} energy!`)
                } else {
                    console.log(`${name} is unable to use ${superpower} or lacks energy!`)
                }

                break;

            case ('Train'):
                const trainingEnergy = line.pop();
                let energyAfterTraining = heroes[name].energy + Number(trainingEnergy)

                if (heroes[name].energy === 100) {
                    console.log(`${name} is already at full energy!`)
                } else if (energyAfterTraining <= 100) {
                    heroes[name].energy = energyAfterTraining;
                    console.log(`${name} has trained and gained ${trainingEnergy} energy!`)
                } else if (energyAfterTraining > 100) {
                    const difference = 100 - heroes[name].energy;
                    heroes[name].energy = 100;
                    console.log(`${name} has trained and gained ${difference} energy!`)
                }

                break;

            case ('Learn'):
                const newSuperpower = line.pop();

                if (heroes[name].powers.includes(newSuperpower)) {
                    console.log(`${name} already knows ${newSuperpower}.`)
                } else {
                    heroes[name].powers.push(newSuperpower);
                    console.log(`${name} has learned ${newSuperpower}!`)
                }

                break;

        }

    })

}
