let socket = null;
let isSocketReady = false;

document.addEventListener("DOMContentLoaded", () => {
  const fab = document.getElementById("chat-fab");
  const chatBox = document.getElementById("chat-box");
  const closeBtn = document.getElementById("chat-close");
  const sendBtn = document.getElementById("chat-send");
  const input = document.getElementById("chat-input");
  const messages = document.getElementById("chat-messages");

  function connectSocket() {
    // ❌ DO NOT reconnect if already open
    if (socket && socket.readyState === WebSocket.OPEN) return;

    socket = new WebSocket(
      (location.protocol === "https:" ? "wss://" : "ws://") +
        location.host +
        "/ws/support-chat/"
    );

    socket.onopen = () => {
      console.log("✅ WebSocket connected");
      isSocketReady = true;
      sendBtn.disabled = false;
    };

    socket.onclose = () => {
      console.warn("⚠️ WebSocket closed");
      isSocketReady = false;
      sendBtn.disabled = true;
    };

    socket.onerror = (e) => {
      console.error("❌ WebSocket error", e);
      isSocketReady = false;
      sendBtn.disabled = true;
    };

    socket.onmessage = (e) => {
      const data = JSON.parse(e.data);

      const isMe = data.sender === CURRENT_USERNAME;

      messages.innerHTML += `
        <div class="msg ${isMe ? "user" : "admin"}">
          <b>${data.sender}:</b> ${data.message}
        </div>
      `;

      messages.scrollTop = messages.scrollHeight;
    };
  }

  /* =====================
     OPEN CHAT
     ===================== */
  fab.onclick = () => {
    chatBox.classList.remove("hidden");
    connectSocket();
  };

  /* =====================
     CLOSE CHAT
     ===================== */
  closeBtn.onclick = () => {
    chatBox.classList.add("hidden");
  };

  /* =====================
     SEND MESSAGE (BUTTON)
     ===================== */
  function sendMessage() {
    const msg = input.value.trim();
    if (!msg) return;

    if (!isSocketReady || !socket || socket.readyState !== WebSocket.OPEN) {
      console.warn("❌ WebSocket not ready");
      return;
    }

    socket.send(JSON.stringify({ message: msg }));
    input.value = "";
  }

  sendBtn.onclick = sendMessage;

  /* =====================
     SEND MESSAGE (ENTER KEY)
     ✅ ADDITIVE FEATURE
     ===================== */
  input.addEventListener("keydown", (e) => {
    if (e.key === "Enter") {
      e.preventDefault();
      sendMessage();
    }
  });

  /* =====================
     INITIAL STATE
     ===================== */
  sendBtn.disabled = true;
});
