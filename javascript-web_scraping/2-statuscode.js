#!/usr/bin/node
const request = require('request');
const args = process.argv;

const options = {
  url: args[2],
  method: 'GET'
};

/*
  Es importante que cuando se haga una request,
  y se utilize la respuesta, se establesca
  un atributo llamado headers en options
  ej:  headers: {'Content-Type: 'application/json'}
  esto para indicar el tipo de contenido de la
  respuesta
*/

request(options, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
