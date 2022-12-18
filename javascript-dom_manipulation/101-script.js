window.onload = function () {
  const btn = document.querySelector('#btn_translate');
  const sayHello = document.querySelector('#hello');
  
  btn.addEventListener('click', () => {
    const lanCode = document.querySelector('#language_code');
    if (lanCode.value !== "") {
      const url = 'https://stefanbohacek.com/hellosalut/?lang=' + lanCode.value;
      fetch(url, { method: 'GET'})
        .then(response => response.json())
        .then(data => {
          sayHello.textContent = data.hello;
        })
    } else {
      sayHello.textContent = "Please select a language"
    }
  })
};