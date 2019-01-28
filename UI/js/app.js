// letiables

//Event Listeners
eventListeners();
// Functions

function eventListeners() {
  document.querySelector('.weight').addEventListener('blur', calcPrice);
  document.getElementById('signout').addEventListener('click', signOut)
}

function signOut(e){
  e.preventDefault();

  window.localStorage.removeItem('token');
  setTimeout(()=>{window.location.href = 'login.html';}, 200);
}

function calcPrice(e){
  e.preventDefault();

  const place = document.querySelector('.place').value;
  const price = document.querySelector('.weight').value;
  let ne = parseInt(price) * 2
  console.log(place, ne);
  document.querySelector('.price').innerHTML = ne;
}

// Modal
let modal = document.getElementById('edit');

let btn = document.querySelector(".edit");


let span = document.getElementsByClassName("close")[0];

btn.onclick = function() {
    modal.style.display = "block";
}

span.onclick = function() {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}

//Tabs
function openCity(e, order) {
    let i, tabcontent, tablinks;
    tabcontent = document.querySelectorAll(".tabcontent");
    for (i = 0; i < tabcontent.length; i++) {
        tabcontent[i].style.display = "none";
    }
    tablinks = document.querySelectorAll(".tablinks");
    for (i = 0; i < tablinks.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" active", "");
    }
    document.getElementById(order).style.display = "block";
    e.currentTarget.className += " active";
}

// Get the element with id="defaultOpen" and click on it
document.getElementById("defaultOpen").click();
