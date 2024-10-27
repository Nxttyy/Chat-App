
 //window.onload = function() {
document.addEventListener("DOMContentLoaded", function () {
    var socket = io();
    socket.on('connect', function() {
        socket.emit('my event', { data: "I'm connected!" });

        const roomId = document.getElementById('room-id').value;
        console.log(roomId)
        socket.emit('join', { room_id: roomId });

    });
  // Listen for incoming messages and append to chat
    socket.on('new_message', function(data) {
        console.log("there")
      const messageContainer = document.createElement("div");
        messageContainer.classList.add("message", "m-2", "w-75");
        

        messageContainer.innerHTML = `
            <p>${data.content}</p>
            <p>${data.time_sent}</p>
            <p>username</p>
        `;

        document.querySelector(".scrollable-div").appendChild(messageContainer);
        console.log("recieved")
    });
});
 //}


  
