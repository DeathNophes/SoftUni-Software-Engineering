function appoint (input) {
    let meetings = {};

    for (const pair of input) {
        const [weekday, name] = pair.split(' ');

        if (meetings.hasOwnProperty(weekday)) {
            console.log(`Conflict on ${weekday}!`)
        } else {
            meetings[weekday] = name;
            console.log(`Scheduled for ${weekday}`)
        }
    }

    for (let key in meetings) {
        console.log(key + ' -> ' + meetings[key])
    }
}
