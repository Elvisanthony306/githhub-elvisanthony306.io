const edit = document.getElementById('edit-form')
const items = document.getElementById('items')
const ham = document.getElementById('ham-burger')

edit.addEventListener('submit', ()=> {
    alert('post has been edited')
})



ham.addEventListener('click', ()=> {
    items.classList.toggle('active')
})