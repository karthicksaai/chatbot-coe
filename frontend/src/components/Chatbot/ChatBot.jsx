import React, { useState, useRef, useEffect } from 'react';
import ChatMessage from './ChatMessage';
import Loading from '../common/Loading';
import './ChatBot.css';

const ChatBot = () => {
    const [messages, setMessages] = useState([
        {
            text: "Hello! I'm your COE Assistant. How can I help you today?",
            type: 'bot'
        }
    ]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSend = async () => {
        if (!input.trim()) return;

        const userMessage = {
            text: input,
            type: 'user'
        };

        setMessages(prev => [...prev, userMessage]);
        setInput('');
        setIsLoading(true);

        try {
            const response = await fetch('http://localhost:8000/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: input }),
            });

            const data = await response.json();
            
            setMessages(prev => [...prev, {
                text: data.response,
                type: 'bot'
            }]);
        } catch (error) {
            setMessages(prev => [...prev, {
                text: "Sorry, I'm having trouble connecting. Please try again.",
                type: 'bot'
            }]);
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="chatbot-container">
            <div className="chatbot-header">
                <h2>COE Assistant</h2>
                <p>Controller of Examinations</p>
            </div>

            <div className="messages-container">
                {messages.map((message, index) => (
                    <ChatMessage 
                        key={index}
                        text={message.text}
                        type={message.type}
                    />
                ))}
                {isLoading && <Loading />}
                <div ref={messagesEndRef} />
            </div>

            <div className="input-container">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    placeholder="Type your question here..."
                    onKeyPress={(e) => e.key === 'Enter' && handleSend()}
                />
                <button 
                    onClick={handleSend}
                    className="send-button"
                    disabled={!input.trim()}
                >
                    Send
                </button>
            </div>
        </div>
    );
};

export default ChatBot;
