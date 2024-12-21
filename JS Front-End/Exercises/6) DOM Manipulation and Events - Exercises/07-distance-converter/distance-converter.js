document.addEventListener('DOMContentLoaded', solve);

function solve() {
    // Conversion rates to meters
    const conversionRates = {
        km: 1000,
        m: 1,
        cm: 0.01,
        mm: 0.001,
        mi: 1609.34,
        yrd: 0.9144,
        ft: 0.3048,
        in: 0.0254
    };

    const convertButton = document.getElementById('convert');

    convertButton.addEventListener('click', () => {
        // Get input values
        const inputDistance = Number(document.getElementById('inputDistance').value);
        const inputUnit = document.getElementById('inputUnits').value;
        const outputUnit = document.getElementById('outputUnits').value;

        if (isNaN(inputDistance)) return false;

        // Convert input distance to meters
        const distanceInMeters = inputDistance * conversionRates[inputUnit];

        // Convert distance from meters to the desired unit
        const convertedDistance = distanceInMeters / conversionRates[outputUnit];

        // Display the result
        document.getElementById('outputDistance').value = convertedDistance.toFixed(4);
    });
}