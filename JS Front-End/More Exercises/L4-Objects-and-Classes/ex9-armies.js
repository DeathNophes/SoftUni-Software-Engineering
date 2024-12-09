function solve(input) {
    const leaders = {};

    const addLeader = (name) => {
        if (!leaders[name]) {
            leaders[name] = { totalArmy: 0, armies: {} };
        }
    };

    const removeLeader = (name) => {
        if (leaders[name]) {
            delete leaders[name];
        }
    };

    const addArmy = (leader, army, count) => {
        if (leaders[leader]) {
            if (!leaders[leader].armies[army]) {
                leaders[leader].armies[army] = 0;
            }
            leaders[leader].armies[army] += count;
            leaders[leader].totalArmy += count;
        }
    };

    const increaseArmyCount = (army, count) => {
        for (const leader of Object.keys(leaders)) {
            if (leaders[leader].armies[army]) {
                leaders[leader].armies[army] += count;
                leaders[leader].totalArmy += count;
            }
        }
    };

    input.forEach((action) => {
        if (action.endsWith('arrives')) {
            addLeader(action.replace(' arrives', ''));
        } else if (action.endsWith('defeated')) {
            removeLeader(action.replace(' defeated', ''));
        } else if (action.includes(':')) {
            const [leader, armyInfo] = action.split(': ');
            const [army, count] = armyInfo.split(', ');
            addArmy(leader, army, Number(count));
        } else if (action.includes('+')) {
            const [army, count] = action.split(' + ');
            increaseArmyCount(army, Number(count));
        }
    });

    // Sorting leaders by totalArmy count
    Object.entries(leaders)
        .sort((a, b) => b[1].totalArmy - a[1].totalArmy)
        .forEach(([leader, { totalArmy, armies }]) => {
            console.log(`${leader}: ${totalArmy}`);
            Object.entries(armies)
                .sort((a, b) => b[1] - a[1])
                .forEach(([army, count]) => console.log(`>>> ${army} - ${count}`));
        });
}