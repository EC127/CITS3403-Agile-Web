const chatHistory = document.querySelector('.chat-history');
const chatInput = document.querySelector('.chat-input input');
const chatButton = document.querySelector('.chat-input button');

let canSendMessage = true;

chatButton.addEventListener('click', sendMessage);

chatInput.addEventListener('keydown', (event) => {
  if (event.key === 'Enter') {
    sendMessage();
  }
});

function sendMessage() {
  const message = chatInput.value.trim();
  if (message !== '') {
    appendMessage(message, true, true);
    chatInput.value = '';
    botResponse(message);
  }
}

function botResponse(message) {
  // Replace this with your own API call or bot logic
  $.ajax({
    url: '/chat',
    type: 'POST',
    contentType: 'application/json',
    data: JSON.stringify({ message: message }),
    dataType: 'json',
    success: function (data) {
      console.log(data); // gain response
      if (data.error === 'Spamming') {
        error_message = 'Your interact too frequently please try again in 20 sec.'
        appendMessage(error_message, false, false);
      }
      else{
        appendMessage(data.response, false, false);  // add the response to chat history
      }
    },
    error: function (error) {
      console.error(error);
    }
  });
}


function appendMessage(message, isUser, waitForBot) {
  const messageContainer = document.createElement('div');
  messageContainer.className = `message-${isUser ? 'user' : 'bot'}`;

  const messageText = document.createElement('p');
  messageText.textContent = message;

  messageContainer.appendChild(messageText);
  chatHistory.appendChild(messageContainer);
  chatHistory.scrollTop = chatHistory.scrollHeight;

  if (isUser) {
    messageText.style.backgroundColor = '#4caf50';
  }

  if (isUser) {
    messageText.style.backgroundColor = '#4caf50';
  }

  if (waitForBot) {
    chatInput.disabled = true;
  } else {
    chatInput.disabled = false;
  }
}

