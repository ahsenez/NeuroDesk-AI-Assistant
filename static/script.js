async function sendCommand() {

    const input = document.getElementById("command-input");
    const chatBox = document.getElementById("chat-box");

    const command = input.value;

    if(command.trim() === "") return;
