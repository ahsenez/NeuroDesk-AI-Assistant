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
        body: JSON.stringify({
            command: command
        })
    });

    const data = await response.json();

    const aiMessage = document.createElement("div");
    aiMessage.className = "ai-message";
    aiMessage.innerText = data.response;

    chatBox.appendChild(aiMessage);

    input.value = "";

    chatBox.scrollTop = chatBox.scrollHeight;
}
