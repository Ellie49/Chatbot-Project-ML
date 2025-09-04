const chatBox = document.getElementById("chat-box");
const input = document.getElementById("user-input");
const sendBtn = document.getElementById("send-btn");

// Change this if your backend runs on a different host/port
const API_URL = "http://127.0.0.1:5000/chat";

function appendMessage(text, who = "bot") {
  const p = document.createElement("div");
  p.className = `msg ${who}`;
  p.textContent = text;
  chatBox.appendChild(p);
  chatBox.scrollTop = chatBox.scrollHeight;
}

function showTyping() {
  const p = document.createElement("div");
  p.className = "msg bot typing";
  p.textContent = "Bot is typing…";
  chatBox.appendChild(p);
  chatBox.scrollTop = chatBox.scrollHeight;
  return p;
}

async function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;
  appendMessage(msg, "user");
  input.value = "";

  const typingNode = showTyping();

  try {
    const res = await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: msg })
    });
    const data = await res.json();
    typingNode.remove();
    appendMessage(data.reply || "(No reply)", "bot");
  } catch (err) {
    typingNode.remove();
    appendMessage("Error: could not reach the server. Is the backend running?", "bot");
  }
}

sendBtn.addEventListener("click", sendMessage);
input.addEventListener("keydown", (e) => {
  if (e.key === "Enter") sendMessage();
});

// Greet on load
appendMessage("Hello! I'm your course project bot 🤖. Ask me anything from the knowledge base or just say hi!", "bot");