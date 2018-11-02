// letiables

//Event Listeners
eventListeners();
// Functions

function eventListeners() {
  document.querySelector('#quote').addEventListener('click', calcPrice)
}

function calcPrice(e){
  e.preventDefault();

  const place = document.querySelector('.place').value;
  const price = document.querySelector('.weight').value;
  let ne = parseInt(price) * 2
  console.log(place, ne);
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
