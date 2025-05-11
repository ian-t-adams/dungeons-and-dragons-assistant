import React, { useState } from 'react';
import { agentAct } from '../api';

function AgentChat() {
  const [input, setInput] = useState('');
  const [response, setResponse] = useState('');

  const handleSend = async () => {
    const result = await agentAct(input);
    setResponse(result.result);
  };

  return (
    <div>
      <h2>Agent Chat</h2>
      <input value={input} onChange={e => setInput(e.target.value)} placeholder="Say something..." />
      <button onClick={handleSend}>Send</button>
      <div>Response: {response}</div>
    </div>
  );
}

export default AgentChat;
