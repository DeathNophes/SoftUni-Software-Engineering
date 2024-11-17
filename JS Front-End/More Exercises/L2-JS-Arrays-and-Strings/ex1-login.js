function solve (array) {
    const username = array[0]
    const password = username.split('').reverse().join('') // We reverse the username
    let counter = 0

    for (let i = 1; i < array.length; i++) {
        if (array[i] === password) {
            console.log(`User ${username} logged in.`)
            break;
        } else  {
            counter += 1
            if (counter === 4) {
                console.log(`User ${username} blocked!`)
                break;
            } else {
                console.log("Incorrect password. Try again.")
            }
        }
    }
}
