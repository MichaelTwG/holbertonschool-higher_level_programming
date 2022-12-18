const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

fetch(url, { method: 'GET'})
  .then(response => response.json())
  .then(data => {
    const list = document.querySelector('#list_movies');
    for (const title of data.results) {
      const newLi = document.createElement('li');
      newLi.textContent = title.title;
      list.appendChild(newLi);
    }
  })
  .catch(err => {
    console.log(err);
  })