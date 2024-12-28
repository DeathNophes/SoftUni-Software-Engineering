function loadCommits() {
    // Get all the required elements
    const username = document.querySelector('#username').value;
    const repoName = document.querySelector('#repo').value;
    const commitsListEl = document.querySelector('#commits');

    const baseUrl = `https://api.github.com/repos/${username}/${repoName}/commits`;

    // Clear the list before appending new items
    commitsListEl.innerHTML = '';

    fetch(baseUrl)
        .then(response => {
            if (! response.ok) {
                throw new Error(`Error: ${response.status} (Not found)`)
            }
            return response.json();
        })
        .then(commits => {
            commits.forEach(commit => {
                const newLiEl = document.createElement('li');
                newLiEl.textContent = `${commit.commit.author.name}: ${commit.commit.message}`;
                commitsListEl.append(newLiEl)
            })
        })
        .catch(error => {
            const errorLi = document.createElement('li');
			errorLi.textContent = error.message;
			commitsListEl.append(errorLi);
        })
}