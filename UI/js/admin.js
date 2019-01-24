
document.querySelector('.alltheorders').addEventListener('click', getAllParcels);

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
