function solve (input) {
    const users = [];
    const articles = [];
    const comments = {};

    const addUser = (username) => {
        if (! users.includes(username)) {
            users.push(username)
        }
    }

    const addArticle = (articleName) => {
        if (! articles.includes(articleName)) {
            articles.push(articleName)
        }
    }

    const addComment = (username, articleName, title, content) => {
        if (users.includes(username) && articles.includes(articleName)) {
            // If the array does not exist we create it
            comments[articleName] = comments[articleName] || [];

            const comment = {'user': username, 'title': title, 'content': content}
            comments[articleName].push(comment)
        }
    }

    input.forEach(action => {
        if (action.startsWith('user')) {
            const username = action.split(' ')[1];
            addUser(username);
        } else if (action.startsWith('article')) {
            const articleName = action.split(' ')[1];
            addArticle(articleName);
        } else if (action.includes('posts')) {
            const [userAndArticleInfo, commentInfo] = action.split(': ');
            const [username, articleName] = userAndArticleInfo.split(' posts on ');
            const [commentTitle, commentContent] = commentInfo.split(', ')
            addComment(username,articleName, commentTitle, commentContent)
        }
    })

    Object
        .entries(comments)
        .sort((a, b) => b[1].length- a[1].length)
        .forEach(([articleName, comments]) => {
            console.log(`Comments on ${articleName}`)
            comments.sort((a, b) => a.user.localeCompare(b.user))
            comments.forEach(({user, title, content}) => {
                console.log(`--- From user ${user}: ${title} - ${content}`)
            })
        })
}
