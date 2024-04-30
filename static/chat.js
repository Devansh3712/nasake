async function sendMessage() {
	const message = document.getElementById('message').value;
	if (message != '') {
		const chat = document.getElementById('chats');
		const element = document.createElement('div');
		element.classList.add('chat-user');
		element.textContent = 'You:\n\n' + message;
		chat.appendChild(element);
		document.getElementById('message').value = '';

		const loading = document.createElement('div');
		loading.innerHTML = `
		<div class="chat-bubble">
			<div class="typing">
				<div class="dot"></div>
				<div class="dot"></div>
				<div class="dot"></div>
			</div>
		</div>
		`;
		chat.appendChild(loading);
		const response = await fetch('http://localhost:8000/chat', {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ message: message }),
		});
		chat.removeChild(loading);
		const botMessage = await response.json();
		const bot = document.createElement('div');
		bot.classList.add('chat-bot');
		bot.textContent = 'Tsuki:\n\n' + String(botMessage);
		chat.appendChild(bot);
	}
}

document.getElementById('send').addEventListener('click', sendMessage);
document.getElementById('message').addEventListener('keydown', (event) => {
	if (event.key === 'Enter') {
		event.preventDefault();
		sendMessage();
	}
});

window.addEventListener('beforeunload', (event) => {
	event.preventDefault();
	event.returnValue = 'Reloading will clear the conversation, continue?';
});
