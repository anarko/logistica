
const btnLogout = document.getElementById('btn-logout');
const btnMenu1 = document.getElementById('btn-menu1');

btnLogout.addEventListener('click', () => {    
  window.location='/recupero/logout/';
});


btnMenu1.addEventListener('click', () => {    
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