import React from 'react';
import ChatBot from './components/Chatbot/ChatBot';

function App() {
    return (
        <div style={{
            height: '100vh',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            background: '#f0f2f5'
        }}>
            <ChatBot />
        </div>
    );
}

export default App;
