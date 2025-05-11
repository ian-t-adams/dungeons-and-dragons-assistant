import React from 'react';
import './App.css';
import AgentChat from './components/AgentChat';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>D&D Assistant</h1>
        <AgentChat />
      </header>
    </div>
  );
}

export default App;
