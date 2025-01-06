function createProfileElement (profile, index) {
    const profileEl = document.createElement('div');
    profileEl.classList.add('profile');
    profileEl.innerHTML = `
        <img src="./iconProfile2.png" class="userIcon" alt="image"/>
        <label>Lock</label>
        <input type="radio" name="user${index + 1}Locked" value="lock" checked>
        <label>Unlock</label>
        <input type="radio" name="user${index + 1}Locked" value="unlock"><br>
        <hr>
        <label>Username</label>
        <input type="text" name="user${index + 1}Username" value="${profile.username}" disabled readonly />
        <div class="hidden-info" style="display: none;">
            <hr>
            <label>Email:</label>
            <input type="email" name="user${index + 1}Email" value="${profile.email}" disabled readonly />
            <label>Age:</label>
            <input type="number" name="user${index + 1}Age" value="${profile.age}" disabled readonly />
        </div>
        <button>Show more</button>
    `;

    const button = profileEl.querySelector('button');
    const hiddenInfoEl = profileEl.querySelector('.hidden-info');
    const lockEl = profileEl.querySelector(`input[name="user${index + 1}Locked"][value="lock"]`);
    const unlockEl = profileEl.querySelector(`input[name="user${index + 1}Locked"][value="unlock"]`);

    // Add event listener for the button
    button.addEventListener('click', () => {
        if (lockEl.checked) return;

        if (unlockEl.checked) {
            if (hiddenInfoEl.style.display === 'none') {
                hiddenInfoEl.style.display = 'block';
                button.textContent = 'Hide it';
            } else {
                hiddenInfoEl.style.display = 'none';
                button.textContent = 'Show more';
            }
        }
    });

    return profileEl;
}

function lockedProfile() {
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/profiles';
    const mainEl = document.querySelector('#main');

    fetch(baseUrl)
        .then(response => response.json())
        .then(data => {
            mainEl.innerHTML = ''; // Clear any existing content

            Object.values(data).forEach((profile, index) => {
                const profileElement = createProfileElement(profile, index);
                mainEl.appendChild(profileElement);
            })
        })
}