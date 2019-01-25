

eventListeners();

function eventListeners (){
  document.getElementById('allorders').addEventListener('click', getParcels);
  document.getElementById('intransit').addEventListener('click', parcelsInTransit);
  document.getElementById('_delivered').addEventListener('click', parcelsDelivered);
  document.getElementById('in_transit').addEventListener('click', cancelParcel);
}

// function to decode token
function parseJwt (token) {
            let base64Url = token.split('.')[1];
            let base64 = base64Url.replace(/-/g, '+').replace(/_/g, '/');
            return JSON.parse(window.atob(base64));
        };
// console.log(parseJwt(window.localStorage.getItem('token')));
// user identity
const identity = parseJwt(window.localStorage.getItem('token')).identity;

// Gets all parcels

function getParcels(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/users/${identity}/parcels`,{
    method:'GET',
    headers:{
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + window.localStorage.getItem('token')
    }
  })
  .then((res) => {
    status = res.status;
    return res.json();
  })
  .then((data) => {
    if (status == 200){
      let output = '';
    // console.log(data);
    data['all parcels'].forEach(parcel => {
      output += `
      <tr>

        <td>${parcel['id']}</td>
        <td>${parcel['title']}</td>
        <td>${parcel['description']}</td>
        <td>${parcel['pickup_location']}</td>
        <td>${parcel['destination']}</td>
        <td>${parcel['weight']}</td>
        <td>${parcel['price']}</td>
        <td>${parcel['status']}</td>
      </tr>
      `;
      document.getElementById('all_orders').innerHTML = output;
    })
    }
  })
  .catch(err => console.log(err))
}

// Get all parcels in transit

function parcelsInTransit(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/users/${identity}/parcels`,{
    method:'GET',
    headers:{
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + window.localStorage.getItem('token')
    }
  })
  .then((res) => {
    status = res.status;
    return res.json();
  })
  .then((data) => {
    if (status == 200){
      let output = '';
    data['all parcels'].forEach(parcel => {
      if(parcel['status'] == 'in transit'){

        output += `
        <tr>

          <td>${parcel['id']}</td>
          <td>${parcel['title']}</td>
          <td>${parcel['description']}</td>
          <td>${parcel['current_location']}</td>
          <td>${parcel['destination']}</td>
          <td>${parcel['weight']}</td>
          <td>${parcel['price']}</td>
          <td>${parcel['status']}</td>
          <td> <a href="#" class="btn edit">Change destination</a></td>
          <td> <a href="#" class="btn cancel">Cancel</a></td>
        </tr>
        `;
        document.getElementById('in_transit').innerHTML = output;
      }

    })
    }
  })
  .catch(err => console.log(err))
}

// Gets all delivered parcels

function parcelsDelivered(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/users/${identity}/parcels`,{
    method:'GET',
    headers:{
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + window.localStorage.getItem('token')
    }
  })
  .then((res) => {
    status = res.status;
    return res.json();
  })
  .then((data) => {
    if (status == 200){
      let output = '';
    data['all parcels'].forEach(parcel => {
      if(parcel['status'] == 'delivered'){

        output += `
        <tr>

          <td>${parcel['id']}</td>
          <td>${parcel['title']}</td>
          <td>${parcel['description']}</td>
          <td>${parcel['pickup_location']}</td>
          <td>${parcel['destination']}</td>
          <td>${parcel['weight']}</td>
          <td>${parcel['price']}</td>
          <td>${parcel['status']}</td>
        </tr>
        `;
        document.getElementById('deliv').innerHTML = output;
      }

    })
    }
  })
  .catch(err => console.log(err))
}


function cancelParcel(e){
  e.preventDefault();
  let status;

  if(e.target.classList.contains('cancel')){
    let id = e.target.parentElement.parentElement.firstElementChild.innerHTML;

    fetch(`http://127.0.0.1:5000/api/v2/parcels/${id}/cancel`,{
      method:'PUT',
      headers:{
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + window.localStorage.getItem('token')
      }
    })
    .then((res)=>{
      status = res.status;
      return res.json();
    })
    .then((data)=>{
      if(status >= 200){
        // alert(`${data.message}`)
        e.target.parentElement.parentElement.remove();
      }else if (status >= 400) {
        alert(`${data.message}`)
      }

    })
  }
}
