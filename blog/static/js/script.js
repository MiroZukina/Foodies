const toggleButton = document.getElementById('menu-toggle');
const navbar = document.getElementById('main-navbar');

toggleButton.addEventListener('click', () => {
    navbar.classList.toggle('active');
});
