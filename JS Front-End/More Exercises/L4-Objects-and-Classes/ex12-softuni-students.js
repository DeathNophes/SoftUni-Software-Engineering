function manageCourses(input) {
    const courses = {};

    input.forEach(entry => {
        if (entry.includes(':')) {
            // Parse course name and capacity
            const [courseName, capacity] = entry.split(': ');
            if (!courses[courseName]) {
                courses[courseName] = {
                    capacity: Number(capacity),
                    students: []
                };
            } else {
                courses[courseName].capacity += Number(capacity);
            }
        } else if (entry.includes('joins')) {
            // Parse student info and course name
            const [studentInfo, courseName] = entry.split(' joins ');
            const [username, credits] = studentInfo.match(/(\w+)\[(\d+)\]/).slice(1);
            const email = studentInfo.match(/with email (.+)/)[1];

            // Add student if the course exists and has capacity
            if (courses[courseName] && courses[courseName].students.length < courses[courseName].capacity) {
                courses[courseName].students.push({
                    username,
                    email,
                    credits: Number(credits)
                });
            }
        }
    });

    // Sort courses by student count descending
    const sortedCourses = Object.entries(courses)
        .sort(([, a], [, b]) => b.students.length - a.students.length);

    // Output the courses and their students
    sortedCourses.forEach(([courseName, courseData]) => {
        const { capacity, students } = courseData;
        console.log(`${courseName}: ${capacity - students.length} places left`);
        students
            .sort((a, b) => b.credits - a.credits)
            .forEach(({ username, email, credits }) =>
                console.log(`--- ${credits}: ${username}, ${email}`)
            );
    });
}