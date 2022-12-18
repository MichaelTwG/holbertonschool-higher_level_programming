const header = document.querySelector('header');
const div = document.querySelector('#red_header');

div.addEventListener('click', () => {
  header.classList.add('red');
});