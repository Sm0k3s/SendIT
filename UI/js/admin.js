
document.querySelector('.alltheorders').addEventListener('click', getAllParcels);
document.querySelector('.changests').addEventListener('click', changeStatus);
document.getElementById('change').addEventListener('click', deliverParcel);
document.querySelector('.changelocale').addEventListener('click', changeLocation);
document.querySelector('#changeloc').addEventListener('click', updateLocation);


function getAllParcels(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/parcels`,{
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
      document.getElementById('alltheorders').innerHTML = output;
    })
    }
  })
  .catch(err => console.log(err))
}

// Change delivery status

function changeStatus(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/parcels`,{
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
          <td> <a href="#" class="btn edit delivr">Deliver</a></td>
        </tr>
        `;
        document.getElementById('change').innerHTML = output;
      }

    })
    }
  })
  .catch(err => console.log(err))
}


// change statuss to delivered

function deliverParcel(e){
  e.preventDefault();
  let status;

  if(e.target.classList.contains('delivr')){
    let id = e.target.parentElement.parentElement.firstElementChild.innerHTML;

    fetch(`http://127.0.0.1:5000/api/v2/parcels/${id}/status`,{
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

// Change current location

function changeLocation(e){
  e.preventDefault();

  let status;

  fetch(`http://127.0.0.1:5000/api/v2/parcels`,{
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
          <td>${parcel['current_location']}</td>
          <td>${parcel['destination']}</td>
          <td>${parcel['weight']}</td>
          <td>${parcel['price']}</td>
          <td> <input type="text" class="c_location" id="" placeholder="current location"> </td>
          <td><a href="#" class="btn edit locale">Submit</a></td>
        </tr>
        `;
        document.getElementById('changeloc').innerHTML = output;
      }

    })
    }
  })
  .catch(err => console.log(err))
}

//function to update current location

function updateLocation(e){
  e.preventDefault();
  let status;
  if(e.target.classList.contains('locale')){
    let id = e.target.parentElement.parentElement.firstElementChild.innerHTML;
    let new_location = e.target.parentElement.parentElement.children[6].children[0].value;
    let new_ = e.target.parentElement.parentElement.children[2].innerText;

    console.log(new_)
    console.log(id);
    console.log(new_location);
    fetch(`http://127.0.0.1:5000/api/v2/parcels/${id}/presentLocation`, {
      method: 'PUT',
      headers:{
        'Content-type': 'application/json',
        'Authorization': 'Bearer ' + window.localStorage.getItem('token'),
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Request-Method': '*'
      },
      body: JSON.stringify({
          location: new_location
        })
    })
    .then((res) => {
      status = res.status;
      return res.json();
    })
    .then((data) => {
      if(status == 400){
        // alert(`${data.message}`);
        console.log(data);
        document.querySelector('.c_location').reset();
        // new_ = `${new_location}`;
      } else if(status == 200) {
        // alert(`${data.message}`);
        // document.querySelector('.c_location').reset();
        console.log(data);
      }
    })
    .catch(err => console.log(err));
  }

}
