
const btnLogout = document.getElementById('btn-logout');
const subirArchivos = document.getElementById('subir-archivos');
const llamadas = document.getElementById('btn-llamadas');


btnLogout.addEventListener('click', () => {    
  window.location='/recupero/logout/';
});


subirArchivos.addEventListener('click', () => {    
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;  
  
  const request = new Request(
      '/recupero/upload_files_form/',
      {headers: {'X-CSRFToken': csrftoken}}
  );

  fetch(request, {
      method: 'POST',
      mode: 'same-origin'  // Do not send CSRF token to another domain.
  })
    .then(response => response.json())
    .then( function ( data )  {
      document.getElementById('container').innerHTML = data.form;
    } );

});


llamadas.addEventListener('click', () => {    
  const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;  
  
  const request = new Request(
      '/recupero/get_clientes/',
      {headers: {'X-CSRFToken': csrftoken}}
  );

  fetch(request, {
      method: 'POST',
      mode: 'same-origin'  // Do not send CSRF token to another domain.
  })
    .then(response => response.json())
    .then( function ( data )  {
      document.getElementById('container').innerHTML = data.html;
    } );

});