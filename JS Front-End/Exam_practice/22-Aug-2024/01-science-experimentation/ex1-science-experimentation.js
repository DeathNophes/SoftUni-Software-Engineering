function solve(input) {

    const chemicalsCount = input.shift();

    const chemicals = input.splice(0, chemicalsCount).reduce((chemicalsObj, entry) => {
        const [ chemical, amount ] = entry.split(' # ');

        chemicalsObj[chemical] = { quantity: Number(amount) }

        return chemicalsObj;
    }, {});

    input.forEach(entry => {

        const line = entry.split(' # ');
        const command = line.shift();

        let name = '';

        switch (command) {
            case 'Mix':
                const [ chemical1, chemical2, amount ] = line;

                if ( chemicals[chemical1].quantity >= amount && chemicals[chemical2].quantity >= amount ) {
                    chemicals[chemical1].quantity -= amount;
                    chemicals[chemical2].quantity -= amount;

                    console.log(`${chemical1} and ${chemical2} have been mixed. ${amount} units of each were used.`);

                } else {
                    console.log(`Insufficient quantity of ${chemical1}/${chemical2} to mix.`);
                }

                break;
            case 'Replenish':

                name = line.shift();
                const [ addedAmount ] = line;

                if ( ! chemicals.hasOwnProperty(name) ) {
                    console.log(`The Chemical ${name} is not available in the lab.`);
                } else {

                    if ( ( chemicals[name].quantity + Number(addedAmount) ) > 500 ) {
                        console.log(`${name} quantity increased by ${500 - chemicals[name].quantity} units, reaching maximum capacity of 500 units!`);
                        chemicals[name].quantity = 500;
                    } else {
                        chemicals[name].quantity += Number(addedAmount);
                        console.log(`${name} quantity increased by ${addedAmount} units!`);
                    }
                }

                break;
            case 'Add Formula':

                name = line.shift();
                const [ formula ] = line;

                if ( ! chemicals.hasOwnProperty(name) ) {
                    console.log(`The Chemical ${name} is not available in the lab.`);
                } else {
                    chemicals[name].formula = formula;
                    console.log(`${name} has been assigned the formula ${formula}.`);
                }

                break;
        }

    });

    Object.keys(chemicals).forEach(name => {

        let output = '';

        output += `Chemical: ${name}, Quantity: ${chemicals[name].quantity}`;

        if ( chemicals[name].hasOwnProperty('formula') ) {
            output += `, `;
            output += `Formula: ${chemicals[name].formula}`;
        }

        console.log(output);

    });

}
