function solve (browser, array) {

    array.forEach(action => {
        if (action.startsWith('Open')) {
            // Extract the tab and add it to the Open Tabs
            const tab = action.split(' ')[1];
            browser['Open Tabs'].push(tab);
            browser['Browser Logs'].push(action)

        } else if (action.startsWith('Close')) {
            // Extract the tab name and process closure
            const tab = action.split(' ')[1];
            const index = browser['Open Tabs'].indexOf(tab)

            if (index !== -1) {
                // Valid site => remove from Open Tabs
                browser['Open Tabs'].splice(index, 1);
                browser['Recently Closed'].push(tab);
                browser['Browser Logs'].push(action);
            }

        } else if (action === 'Clear History and Cache') {
            browser['Browser Logs'] = [];
            browser['Open Tabs'] = [];
            browser['Recently Closed'] = [];
        }
    })

    console.log(browser['Browser Name'])
    console.log(`Open Tabs: ${browser['Open Tabs'].join(', ')}`)
    console.log(`Recently Closed: ${browser['Recently Closed'].join(', ')}`)
    console.log(`Browser Logs: ${browser['Browser Logs'].join(', ')}`)
}
