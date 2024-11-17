function addReservation() {
    const name = document.getElementById('name').value;
    const phone = document.getElementById('phone').value;
    fetch('/add_reservation', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ name, phone })
    })
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function searchReservation() {
    const name = document.getElementById('search-name').value;
    fetch(`/search_reservation?name=${name}`)
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function searchByPhone() {
    const phone = document.getElementById('search-phone').value;
    fetch(`/search_by_phone?phone=${phone}`)
    .then(response => response.json())
    .then(data => alert(data.message))
    .catch(error => console.error('Error:', error));
}

function listReservations() {
    fetch('/list_reservations')
    .then(response => response.json())
    .then(data => {
        const tbody = document.getElementById('reservation-display');
        tbody.innerHTML = '';
        data.forEach(reservation => {
            const row = document.createElement('tr');
            const phoneCell = document.createElement('td');
            const nameCell = document.createElement('td');
            phoneCell.textContent = reservation.phone_number;
            nameCell.textContent = reservation.name;
            row.appendChild(phoneCell);
            row.appendChild(nameCell);
            tbody.appendChild(row);
        });
    })
    .catch(error => console.error('Error:', error));
}
