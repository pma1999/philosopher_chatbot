import React, { useState, useEffect } from 'react';
import { useAppContext } from '../contexts/AppContext';
import { startConversation, sendMessage } from '../services/api';

interface Message {
  role: 'user' | 'assistant';
  content: string;
}

const ChatInterface: React.FC = () => {
  const { language, apiKey, philosopherId, setSessionId, sessionId, setCurrentStep } = useAppContext();
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState('');
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);
  const [isConversationStarted, setIsConversationStarted] = useState(false);
  const [philosopherName, setPhilosopherName] = useState('');

  useEffect(() => {
    if (!language || !apiKey || !philosopherId) {
      setCurrentStep('language');
      return;
    }

    const initConversation = async () => {
      setIsLoading(true);
      try {
        const response = await startConversation(language, philosopherId, apiKey);
        setSessionId(response.session_id);
        setPhilosopherName(response.philosopher_name);
        setMessages([]);
        setError(null);
        setIsConversationStarted(true);
      } catch (error) {
        console.error('Error starting conversation:', error);
        setError('Error starting conversation. Please try again.');
        setIsConversationStarted(false);
      } finally {
        setIsLoading(false);
      }
    };
    initConversation();
  }, [language, apiKey, philosopherId, setCurrentStep, setSessionId]);

  const handleSendMessage = async () => {
    if (input.trim() && !isLoading && isConversationStarted) {
      setIsLoading(true);
      setMessages(prev => [...prev, { role: 'user', content: input }, { role: 'assistant', content: `${philosopherName} is typing...` }]);
      setInput('');
      try {
        const response = await sendMessage(sessionId, input, apiKey);
        setMessages(prev => prev.map(m => m.content === `${philosopherName} is typing...` ? { role: 'assistant', content: response } : m));
        setError(null);
      } catch (error) {
        console.error('Error sending message:', error);
        setError(error instanceof Error ? error.message : 'Error sending message. Please try again.');
        if (error instanceof Error && error.message.includes('Conversation not started')) {
          setIsConversationStarted(false);
        }
      } finally {
        setIsLoading(false);
      }
    }
  };

  const handleKeyPress = (e: React.KeyboardEvent<HTMLInputElement>) => {
    if (e.key === 'Enter') {
      e.preventDefault();
      handleSendMessage();
    }
  };

  const handleRestartConversation = async () => {
    setIsLoading(true);
    try {
      const response = await startConversation(language, philosopherId, apiKey);
      setSessionId(response.session_id);
      setPhilosopherName(response.philosopher_name);
      setMessages([]);
      setError(null);
      setIsConversationStarted(true);
    } catch (error) {
      console.error('Error restarting conversation:', error);
      setError('Error restarting conversation. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  if (error) {
    return (
      <div className="flex flex-col items-center">
        <h2 className="text-2xl font-bold mb-4">Chat</h2>
        <p className="text-red-500">{error}</p>
        <button 
          onClick={handleRestartConversation}
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Restart Conversation
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col h-full">
      <div className="flex-grow overflow-y-auto p-4 space-y-4">
        <h2 className="text-xl font-bold mb-4">{philosopherName}</h2>
        {messages.map((message, index) => (
          <div
            key={index}
            className={`p-2 rounded-lg ${
              message.role === 'user' ? 'bg-blue-100 ml-auto' : 'bg-gray-100'
            }`}
          >
            {message.content}
          </div>
        ))}
      </div>
      <div className="p-4 border-t">
        <div className="flex space-x-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyPress={handleKeyPress}
            className="flex-grow p-2 border rounded"
            placeholder="Type your message..."
            disabled={isLoading}
          />
          <button
            onClick={handleSendMessage}
            className={`px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600 ${
              isLoading ? 'opacity-50 cursor-not-allowed' : ''
            }`}
            disabled={isLoading}
          >
            {isLoading ? 'Sending...' : 'Send'}
          </button>
        </div>
      </div>
    </div>
  );
};

export default ChatInterface;
