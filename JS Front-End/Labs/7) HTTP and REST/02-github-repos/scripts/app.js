function loadRepos() {

   const baseUrl = 'https://api.github.com/users/testnakov/repos'; // The API URL
   const resultEl = document.querySelector('#res');

   fetch(baseUrl) // Sending a GET request
       .then(response => response.text()) // Transform the response to text
       .then(res => resultEl.textContent = res)  // Replace the textContent
       .catch(error => console.log('Error')) // Handle potential errors
}