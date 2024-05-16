const chatHistory = document.getElementById('chat-history');
const chatForm = document.getElementById('chat-form');

// Fetch initial data on page load (empty message list for now)
fetch('/chatbot', { method: 'GET' })
  .then(response => response.json())
  .then(data => {
    // Update the chat history with any initial data (e.g., welcome message)
  });

// Handle form submission
chatForm.addEventListener('submit', (event) => {
  event.preventDefault();

  const description = document.getElementById('description').value;

  // Send a POST request to the backend with the user's description
  fetch('/chatbot', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ description })
  })
  .then(response => response.json())
  .then(data => {
    // Append the chatbot's response to the chat history
    const botMessage = document.createElement('div');
    botMessage.classList.add('bot-message');
    botMessage.innerHTML = `<p class="message-text">${data.response}</p>`;
    chatHistory.appendChild(botMessage);

    // Clear the input field
    document.getElementById('description').value = '';

    // Scroll to the bottom of the chat history
    chatHistory.scrollTop = chatHistory.scrollHeight;
  });
});
