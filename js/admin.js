
document.querySelector('.alltheorders').addEventListener('click', getAllParcels);
document.querySelector('.changests').addEventListener('click', changeStatus);
document.getElementById('change').addEventListener('click', deliverParcel);

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
          <td> <a href="#" class="btn edit delivr">Delivered</a></td>
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
