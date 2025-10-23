document.addEventListener("DOMContentLoaded", function () {
  const socket = io();

  const roomId = document.getElementById("room-id").value;
  const messagesDiv = document.querySelector(".chat-messages");

  socket.on("connect", function () {
    socket.emit("my event", { data: "I'm connected!" });
    socket.emit("join", { room_id: roomId });
  });

  socket.on("new_message", function (data) {
    const messageContainer = document.createElement("div");
    messageContainer.classList.add("message");

    messageContainer.innerHTML = `
      <div class="message-info">
        <span class="username">${data.username}</span>
        <span class="timestamp">${data.time_sent}</span>
      </div>
      <p class="message-content">${data.content}</p>
    `;

    messagesDiv.appendChild(messageContainer);

    messagesDiv.scrollTop = messagesDiv.scrollHeight;
  });

  messagesDiv.scrollTop = messagesDiv.scrollHeight;
});
