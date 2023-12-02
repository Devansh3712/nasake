async function searchTherapists() {
	const div = document.getElementById('search-result');
	div.innerHTML = ``;
	const mode = document.getElementById('mode');
	const modeValue = mode.options[mode.selectedIndex].value;

	const table = document.createElement('table');
	table.innerHTML = `
	<tr>
		<th>Name</th>
    	<th>Location</th>
    	<th>Fees</th>
    	<th>Mode</th>
    	<th>Contact</th>
    	<th>Email</th>
	</tr>
	`;

	const response = await fetch(
		'http://localhost:8000/search/therapist?mode=' + modeValue,
		{
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
			},
		},
	);
	const therapists = await response.json();

	Object.keys(therapists).forEach((key) => {
		const therapist = therapists[key];
		const tr = document.createElement('tr');
		for (let value in therapist) {
			const td = document.createElement('td');
			switch (value) {
				case 'contact':
					td.textContent =
						therapist[value][0] === undefined
							? 'None'
							: therapist[value][0].contact;
					break;
				case 'email':
					td.textContent =
						therapist[value][0] === undefined
							? 'None'
							: therapist[value][0].email;
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
