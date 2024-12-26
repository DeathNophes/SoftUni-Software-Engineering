document.addEventListener('DOMContentLoaded', solve);

function solve() {
    const correctAnswers = ["onclick", "JSON.stringify()", "A programming API for HTML and XML documents"];
    const sections = document.querySelectorAll('.question');
    const resultDiv = document.getElementById('results');
    let currentQuestionIndex = 0;
    let rightAnswers = 0;

    // Event delegation for handling answer clicks
    document.body.addEventListener('click', (e) => {
        if (e.target.classList.contains('quiz-answer')) {
            // Check if the selected answer is correct
            if (e.target.textContent === correctAnswers[currentQuestionIndex]) {
                rightAnswers++;
            }

            // Hide the current question and show the next one (if any)
            sections[currentQuestionIndex].classList.add('hidden');
            currentQuestionIndex++;

            if (currentQuestionIndex < sections.length) {
                sections[currentQuestionIndex].classList.remove('hidden');
            } else {
                // Show results
                const resultMessage =
                    rightAnswers === correctAnswers.length
                        ? "You are recognized as top JavaScript fan!"
                        : `You have ${rightAnswers} right ${rightAnswers === 1 ? "answer" : "answers"}`;
                resultDiv.textContent = resultMessage;
                resultDiv.style.display = 'block';
            }
        }
    });
}