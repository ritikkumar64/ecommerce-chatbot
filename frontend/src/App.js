import React, { useState } from 'react';
import axios from 'axios';

function App() {
  const [message, setMessage] = useState('');
  const [reply, setReply] = useState('');

  const sendMessage = async () => {
    const res = await axios.post('http://localhost:5000/chat', { message });
    setReply(res.data.response);
  };

  return (
    <div style={{ padding: '20px' }}>
      <h1>🛍️ E-commerce Chatbot</h1>
      <input
        type="text"
        placeholder="Ask me anything..."
        value={message}
        onChange={e => setMessage(e.target.value)}
      />
      <button onClick={sendMessage}>Send</button>
      <p><strong>Bot:</strong> {reply}</p>
    </div>
  );
}

export default App;
