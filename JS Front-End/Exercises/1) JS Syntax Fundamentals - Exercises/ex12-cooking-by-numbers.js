function solve (num, op1, op2, op3, op4, op5) {

    let number = Number(num);
    const listOfOperations = [op1, op2, op3, op4, op5]

    for (let i = 0; i < listOfOperations.length; i++) {
        let currentAction = listOfOperations[i]

        switch (currentAction) {
            case "chop": number /= 2; break;
            case "dice": number = Math.sqrt(number); break;
            case "spice": number += 1; break;
            case "bake": number *= 3; break;
            case "fillet": number *= 0.80; break;
        }

        console.log(number)
    }
}
