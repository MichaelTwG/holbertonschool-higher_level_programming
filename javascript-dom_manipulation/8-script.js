window.onload = function () {
  const hello = document.querySelector('#hello');
  fetch('https://stefanbohacek.com/hellosalut/?lang=fr', {mode: 'cors'})
    .then(response => response.json())
    .then(data => {
      hello.textContent = data.hello;
    })
    .catch(err => {
      console.log(err);
    });
};