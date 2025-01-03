document.addEventListener('DOMContentLoaded', solution)

function createArticleElement(baseUrl, article) {
    const articleEl = document.createElement('div');
    articleEl.classList.add('accordion')
    articleEl.innerHTML = `
        <div class="head">
            <span>${article.title}</span>
            <button class="button" id="${article._id}">More</button>
        </div>
        <div class="extra">
            <p></p>
        </div>
    `

    const btnEl = articleEl.querySelector('.button');
    const divExtraEl = articleEl.querySelector('.extra')
    const extraParagraphEl = articleEl.querySelector('.extra p');

    fetch(baseUrl + '/details/' + article._id )
        .then(response => response.json())
        .then(data => {
            extraParagraphEl.textContent = data.content;
        })
        .catch(error => console.error(error))

    btnEl.addEventListener('click', () => {
        if (btnEl.textContent === 'More') {
            divExtraEl.style.display = 'block'
            btnEl.textContent = 'Less'
        } else {
            divExtraEl.style.display = 'none'
            btnEl.textContent = 'More'
        }
    })

    return articleEl
}

function solution() {
    const mainSection = document.querySelector('#main');
    const baseUrl = 'http://localhost:3030/jsonstore/advanced/articles';

    fetch(baseUrl + '/list')
        .then(response => response.json())
        .then(data => {
            data.forEach(el => {
                const articleElement = createArticleElement(baseUrl, el);
                mainSection.appendChild(articleElement)
            })
        })
}