import React from 'react';

const ChatMessage = ({ text, type }) => {
    return (
        <div className={`message-wrapper ${type}`}>
            <div className={`message ${type}`}>
                {type === 'bot' && (
                    <div className="avatar">
                        <img src="/bot-avatar.png" alt="Bot" />
                    </div>
                )}
                <div className="message-content">
                    {text}
                </div>
            </div>
        </div>
    );
};

export default ChatMessage;
