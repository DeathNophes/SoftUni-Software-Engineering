function solve (lostFights, helmetPrice, swordPrice, shieldPrice, armorPrice) {

    let brokenHelmets = 0;
    let brokenSwords = 0;
    let brokenShields = 0;
    let brokenArmors = 0;

    for (let i = 1; i <= lostFights; i++) {
        if (i % 2 === 0 && i % 3 === 0) {
            brokenShields += 1;
            if (brokenShields % 2 === 0) {
                brokenArmors += 1;
            }
        }
        if (i % 2 === 0) brokenHelmets += 1;
        if (i % 3 === 0) brokenSwords += 1;
    }

    let result = (brokenHelmets * helmetPrice) + (brokenSwords * swordPrice) +
        (brokenShields * shieldPrice) + (brokenArmors * armorPrice)

    console.log(`Gladiator expenses: ${result.toFixed(2)} aureus`)
}
