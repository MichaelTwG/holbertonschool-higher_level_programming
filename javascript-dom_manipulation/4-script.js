const listUl = document.querySelector('.my_list');
const addItem = document.querySelector('#add_item');

addItem.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  listUl.appendChild(li);
});