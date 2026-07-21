async function sendCommand() {

    const input = document.getElementById("command-input");
    const chatBox = document.getElementById("chat-box");

    const command = input.value;

    if(command.trim() === "") return;

    const userMessage = document.createElement("div");
    userMessage.className = "user-message";
    userMessage.innerText = command;

    chatBox.appendChild(userMessage);

    const response = await fetch("/command", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
