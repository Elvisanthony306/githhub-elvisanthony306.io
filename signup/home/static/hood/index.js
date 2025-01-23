
const firstName = document.getElementById("first-name");
const email = document.getElementById("email");
const city = document.getElementById("city");
const age = document.getElementById("age");
const editBtn = document.getElementById('edit-btn');
const subBtn = document.getElementById('submit');
const form = document.getElementById('form');





editBtn.addEventListener('click', function() {
    firstName.disabled = false
    email.disabled = false
    city.disabled = false
    age.disabled = false
    editBtn.style.display = "none"
    subBtn.style.display = 'block'
})

form.addEventListener('submit', function() {
    firstName.disabled = true
    email.disabled = true
    city.disabled = true
    age.disabled = true
    editBtn.style.display = "block"
    subBtn.style.display = 'none'
})