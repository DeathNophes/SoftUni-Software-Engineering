function schoolRegister(input) {
    const school = {};

    // Process each student record
    input.forEach((line) => {
        const [namePart, gradePart, scorePart] = line.split(', ');
        const name = namePart.split(': ')[1];
        const grade = Number(gradePart.split(': ')[1]) + 1; // Next grade
        const score = Number(scorePart.split(': ')[1]);

        // Only promote students with an annual score of 3 or higher
        if (score >= 3) {
            if (!school[grade]) {
                school[grade] = { students: [], scores: [] };
            }
            school[grade].students.push(name);
            school[grade].scores.push(score);
        }
    });

    // Sort grades and format output
    const sortedGrades = Object.keys(school).sort((a, b) => a - b);

    sortedGrades.forEach((grade) => {
        const students = school[grade].students.join(', ');
        const averageScore =
            (school[grade].scores.reduce((a, b) => a + b, 0) /
            school[grade].scores.length).toFixed(2);

        console.log(`${grade} Grade`);
        console.log(`List of students: ${students}`);
        console.log(`Average annual score from last year: ${averageScore}`);
        console.log('');
    });
}