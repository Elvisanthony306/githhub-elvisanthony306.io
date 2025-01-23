const addbtn = document.getElementById('add-post-btn');
const postForm = document.getElementById('add-post');
const items = document.getElementById('items')
const ham = document.getElementById('ham-burger')

document.addEventListener('DOMContentLoaded', ()=> {
    addbtn.disabled = true
    addbtn.classList.add('active')
})
postForm.addEventListener('keyup', ()=> {
    if (document.querySelector('#add-post').value.length > 0 ) {
        addbtn.disabled = false
        addbtn.classList.remove('active')
    } else {
        addbtn.disabled = true
        addbtn.classList.add('active')
    }
    
})

addbtn.addEventListener('click', function() {
    postForm.classList.add('active')
    console.log('bam')
    
});


ham.addEventListener('click', ()=> {
    items.classList.toggle('active')
})

