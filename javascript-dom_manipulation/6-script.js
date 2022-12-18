const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

fetch(url, { method: 'GET' }) // fech devuelve una promesa
  .then(response => response.json()) //convertir la respuesta a json
  .then(data => {
    //manejar la respuesta
    const character = document.querySelector('#character');
    character.textContent = data.name;
  })
  .catch(err => { // capturar el error
    console.log(err);
  })
