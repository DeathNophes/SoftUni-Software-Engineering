function pass (grade) {
    return grade >= 3.00
}

function hLine() {
    console.log('--------------------');
}

function printHeader() {
    console.log('~~~-    {@}    -~~~');
    console.log('~- Certificate -~~~');
    console.log('~~~-   ~---~   -~~~');
}

function printName(nameArray) {
    console.log(`${nameArray[0]} ${nameArray[1]}`);
}

function formatGrade (grade) {
    const formattedGrade = grade.toFixed(2);
    if (grade < 3.50) console.log(`Poor (${formattedGrade})`);
    else if (grade < 4.50) console.log(`Good (${formattedGrade})`);
    else if (grade < 5.50) console.log(`Very good (${formattedGrade})`);
    else if (grade >= 5.50) console.log(`Excellent (${formattedGrade})`);
}

function printCertificate(grade, name) {
    if (pass(grade) !== true) {
        console.log('Student does not qualify');
    } else {
        hLine();
        printHeader();
        printName(name);
        formatGrade(grade);
    }
    
}

printCertificate(5.25, ['David', 'Core']);