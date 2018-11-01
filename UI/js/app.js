// Variables

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
