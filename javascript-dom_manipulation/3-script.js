const header = document.querySelector('header');
const div = document.querySelector('#toggle_header');

div.addEventListener('click', () => {
  header.classList.toggle('green');
  header.classList.toggle('red');
});