function attachEvents() {
    // Get the elements
    const btnLoadPostsEl = document.querySelector('#btnLoadPosts')
    const btnViewPostEl = document.querySelector('#btnViewPost')

    btnLoadPostsEl.addEventListener('click', loadHandler);
    btnViewPostEl.addEventListener('click', viewHandler);

    const selectPosts = document.querySelector('#posts');
    const postTitleEl = document.querySelector("#post-title");
    const postBodyEl = document.querySelector("#post-body");
    const postCommentsEl = document.querySelector("#post-comments");

    const baseUrl = "http://localhost:3030/jsonstore/blog"

    function loadHandler () {
        selectPosts.innerHTML = '';

        fetch(baseUrl + '/posts')
            .then(response => response.json())
            .then(posts => {

                Object
                    .values(posts)
                    .forEach(post => {
                        const optionEl = document.createElement('option');

                        optionEl.dataset.id = post.id;
                        optionEl.dataset.title = post.title;
                        optionEl.dataset.body = post.body;

                        optionEl.textContent = post.title;
                        selectPosts.appendChild(optionEl);
                    })

            })
            .catch(error => console.error(error))
    }

    function viewHandler () {

        postCommentsEl.innerHTML = '';

        fetch(baseUrl + '/comments')
            .then(response => response.json())
            .then(comments => {

                const optionEl = selectPosts.querySelector('option:checked');

                postTitleEl.textContent = optionEl.dataset.title;
                postBodyEl.textContent = optionEl.dataset.body;

                Object
                    .values(comments)
                    .forEach(comment => {
                        if (comment['postId'] === optionEl.dataset.id) {
                            const commentEl = document.createElement('li');
                            commentEl.textContent = comment.text;
                            postCommentsEl.appendChild(commentEl);
                        }
                    })

            })
            .catch(error => console.error(error))

    }

}

attachEvents();