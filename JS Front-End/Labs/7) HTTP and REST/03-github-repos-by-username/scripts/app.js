function loadRepos() {

	const username = document.querySelector('#username').value;
	const listEl = document.querySelector('#repos');

	const baseUrl = `https://api.github.com/users/${username}/repos`;

	// Clear the list before appending new items
	listEl.innerHTML = '';

	fetch(baseUrl)
		.then(response => {
			if (! response.ok) {
				// If the response is not OK (e.g., 404)
				throw new Error(`Error: ${response.status} (${response.statusText})`);
			}
			return response.json();
		})
		.then(repo => repo.forEach(el => {
			const newLiEl = document.createElement('li');
			const newAEl = document.createElement('a');
			newAEl.setAttribute('href', `${el['html_url']}`);
			newAEl.textContent = `${el['full_name']}`;
			newLiEl.append(newAEl);
			listEl.append(newLiEl);
		}))
		.catch(error => {
			// If an error occurs, display it in a new list item
			const errorLi = document.createElement('li');
			errorLi.textContent = error.message;
			listEl.append(errorLi);
		})
}
