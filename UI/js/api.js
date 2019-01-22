// event Listeners
if (location.href.match(/login/)){
  if (localStorage.getItem('token') != null){
    window.location.href = 'orders.html';
  } else {
    document.getElementById('signin').addEventListener('click', login);
  }
} else if(location.href.match(/signup/)){
  if (localStorage.getItem('token') != null){
    window.location.href = 'orders.html';
  }
  else {document.getElementById('create').addEventListener('click', signup);}
}


//login
function login(e){
  e.preventDefault();

  let username = document.getElementById('username').value;
  let password = document.getElementById('password').value;

  fetch('http://127.0.0.1:5000/api/v2/auth/login', {
      method: 'POST',
      headers:{
        'Content-type': 'application/json'
      },
      body: JSON.stringify({
          username: username,
          password: password
        })
      })
      .then((res) => {
        status = res.status;
        return res.json();
      })
      .then((data) =>{
        if (status >= 400){
          alert(`${data.Message}`)
        }
        else if (status >= 200){
          alert(`${data.Message}`);
          window.localStorage.setItem('token', data.token);
          window.location.href = 'orders.html';
        }
      })
      .catch((err)=>console.log(err))
}

//sign up
function signup(e){
  e.preventDefault();

  let firstname = document.getElementById('firstname').value;
  let surname = document.getElementById('surname').value;
  let username = document.getElementById('username').value;
  let email = document.getElementById('email').value;
  let password = document.getElementById('password').value;

  fetch('http://127.0.0.1:5000/api/v2/auth/signup', {
    method: 'POST',
    headers:{
      'Content-type': 'application/json'
    },
    body: JSON.stringify({
        firstname:firstname,
        surname:surname,
        username: username,
        email:email,
        password: password
      })
    })
    .then((res)=>{
      status = res.status;
      return res.json();
    })
    .then((data)=>{
      if(status >= 400){
        alert(`${data.message}`)
      }
      else if(status >= 200){
        alert(`${data.message}`)
      }
    })
    .catch((err)=>console.log(err))
}
