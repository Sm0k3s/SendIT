const form = document.getElementById('form');

document.getElementById('post_parcel').addEventListener('click', postParcel);

function postParcel(e){
  e.preventDefault();

  let title = document.getElementById('title').value;
  let description = document.getElementById('description').value;
  let location = document.getElementById('location').value;
  let destination = document.getElementById('destination').value;
  let weight = document.getElementById('weight').value;

  let status;
  if(title === '' || location === '' || destination === '' || weight === ''){
    displayErrors('some fields are empty');
  } else {
    fetch('http://127.0.0.1:5000/api/v2/parcels', {
      method: 'POST',
      headers:{
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + window.localStorage.getItem('token')
      },
      body: JSON.stringify({
          title:title,
          description:description,
          pickup_location: location,
          weight:weight,
          destination: destination
        })
      })
      .then((res)=>{
        status = res.status
        return res.json();
      })
      .then((data)=>{
        if(status >= 400){
          if(data.Message == 'expired token, login to get a new one.'){
            window.localStorage.removeItem('token');
            window.location.href = 'login.html';
          }else{
            displayErrors(`${data.message}`)
          }
        }
        else if(status >= 200){
          displaySuccess(`${data.message}`);
        }
      })
      .catch((err)=>console.log(err));

  }

}

function displayErrors (message) {
  let div = document.createElement('div');
  div.classList = 'error';

  div.innerHTML = `
    <p>${message}</p>
  `
  form.insertBefore(div, document.querySelector('.form-group'));

  setTimeout(function(){
    document.querySelector('.error').remove();
  }, 3000);
}

function displaySuccess (message) {
  let div = document.createElement('div');
  div.classList = 'message';

  div.innerHTML = `
    <p>${message}</p>
  `
  form.insertBefore(div, document.querySelector('.form-group'));

  setTimeout(function(){
    document.querySelector('.message').remove();
  }, 3000);
}
