/*
const btnLogin = document.getElementById('btn-login');

btnLogin.addEventListener('click', () => {
  var url = '/recupero/login/';
  var data = {'user': 'anarko','pass':'anarko'};

  fetch(url, {
    method: 'POST', // or 'PUT'
    body: JSON.stringify(data), // data can be `string` or {object}!
    headers:{
      'Content-Type': 'application/json'
    }
  }).then(res => res.json())
  .catch(error => console.error('Error:', error))
  .then(response => console.log('Success:', response));
  });
*/