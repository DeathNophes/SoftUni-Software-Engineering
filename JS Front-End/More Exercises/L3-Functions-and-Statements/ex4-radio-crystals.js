function processCrystals(input) {
    const targetThickness = input[0];
    const chunks = input.slice(1); // This gets all the chunks on the first index and forward

    const operations = {
        cut: (thickness) => thickness / 4,
        lap: (thickness) => thickness * 0.8,
        grind: (thickness) => thickness - 20,
        etch: (thickness) => thickness - 2,
        xRay: (thickness) => thickness + 1,
        transportAndWash: (thickness) => Math.floor(thickness)
    };

    for (let chunk of chunks) {
        console.log(`Processing chunk ${chunk} microns`);
        let currentThickness = chunk;

        const executeOperation = (operation, name) => {
            let count = 0; // counting the number of actions
            while (operation(currentThickness) >= targetThickness ||
                   (name === "etch" && operation(currentThickness) + 1 >= targetThickness)) {
                currentThickness = operation(currentThickness);
                count++;
            }
            if (count > 0) {
                console.log(`${name} x${count}`);
                currentThickness = operations.transportAndWash(currentThickness);
                console.log("Transporting and washing");
            }
        };

        // Cut
        executeOperation(operations.cut, "Cut");

        // Lap
        executeOperation(operations.lap, "Lap");

        // Grind
        executeOperation(operations.grind, "Grind");

        // Etch
        executeOperation(operations.etch, "Etch");

        // X-ray (only if needed)
        if (currentThickness + 1 === targetThickness) {
            currentThickness = operations.xRay(currentThickness);
            console.log("X-ray x1");
        }

        console.log(`Finished crystal ${currentThickness} microns`);
    }
}
