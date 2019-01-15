// login
eventListeners();
// Functions

function eventListeners() {
  document.getElementById('signin').addEventListener('click', login);
}

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
}
