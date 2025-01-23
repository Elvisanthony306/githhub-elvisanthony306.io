const post = document.getElementById('delete-form')
const items = document.getElementById('items')
const ham = document.getElementById('ham-burger')

post.addEventListener('submit', ()=> {
    alert('post has been deleted')
})

ham.addEventListener('click', ()=> {
    items.classList.toggle('active')
})