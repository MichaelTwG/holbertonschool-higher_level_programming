window.onload = function () {
  const listUl = document.querySelector('.my_list');
  const addItem = document.querySelector('#add_item');
  const removeItem = document.querySelector('#remove_item');
  const clearList = document.querySelector('#clear_list');

  addItem.addEventListener('click', () => {
    const li = document.createElement('li');
    li.textContent = 'Item';
    listUl.appendChild(li);
  });

  removeItem.addEventListener('click', () => {
    const lastChild = listUl.lastElementChild;
    lastChild.remove();
  });

  clearList.addEventListener('click', () => {
    listUl.innerHTML = '';
  });
};