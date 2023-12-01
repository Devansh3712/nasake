async function searchTherapists() {
	const div = document.getElementById('search-result');
	div.innerHTML = ``;
	const mode = document.getElementById('mode');
	const modeValue = mode.options[mode.selectedIndex].value;

	const response = await fetch(
		'http://localhost:8000/search/therapist?mode=' + modeValue,
		{
			method: 'GET',
		},
	);
	const table = document.createElement('table');
	const tr = document.createElement('tr');
	tr.innerHTML = `<th>Name</th>
    <th>Location</th>
    <th>Fees</th>
    <th>Mode</th>
    <th>Contact</th>
    <th>Email</th>`;
	table.appendChild(tr);
	const therapists = await response.json();
	Object.keys(therapists).forEach((key) => {
		const therapist = therapists[key];
		const tr = document.createElement('tr');
		for (let value in therapist) {
			const td = document.createElement('td');
			switch (value) {
				case 'contact':
					if (therapist[value][0] !== undefined) {
						td.textContent = therapist[value][0].contact;
					} else td.textContent = 'None';
					break;
				case 'email':
					if (therapist[value][0] !== undefined) {
						td.textContent = therapist[value][0].email;
					} else td.textContent = 'None';
					break;
				case 'id':
					continue;
				default:
					td.textContent = therapist[value];
			}
			tr.appendChild(td);
		}
		table.appendChild(tr);
	});
	div.appendChild(table);
}

document.getElementById('submit').addEventListener('click', searchTherapists);
