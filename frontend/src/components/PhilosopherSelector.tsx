import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../contexts/AppContext';
import { getPhilosophers } from '../services/api';

interface Philosopher {
  id: string;
  name: string;
  period: string;
}

const PhilosopherSelector: React.FC = () => {
  const { language, apiKey, setPhilosopherId, setCurrentStep } = useAppContext();
  const [philosophers, setPhilosophers] = useState<Philosopher[]>([]);
  const [error, setError] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchPhilosophers = async () => {
      if (!language || !apiKey) {
        setError('Language or API key is missing');
        setIsLoading(false);
        return;
      }
      try {
        const data = await getPhilosophers(language, apiKey);
        setPhilosophers(data);
        setError(null);
      } catch (error) {
        console.error('Error fetching philosophers:', error);
        setError(error instanceof Error ? error.message : 'Error fetching philosophers. Please try again later.');
      } finally {
        setIsLoading(false);
      }
    };
    fetchPhilosophers();
  }, [language, apiKey]);

  const handlePhilosopherSelect = (id: string) => {
    setPhilosopherId(id);
    setCurrentStep('chat');
    navigate('/chat');
  };

  if (isLoading) {
    return <div>Loading philosophers...</div>;
  }

  if (error) {
    return (
      <div className="flex flex-col items-center">
        <h2 className="text-2xl font-bold mb-4">Select a Philosopher</h2>
        <p className="text-red-500">{error}</p>
        <button 
          onClick={() => setCurrentStep('language')}
          className="mt-4 px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
        >
          Restart
        </button>
      </div>
    );
  }

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-2xl font-bold mb-4">Select a Philosopher</h2>
      <div className="grid grid-cols-2 gap-4">
        {philosophers.map((philosopher) => (
          <button
            key={philosopher.id}
            onClick={() => handlePhilosopherSelect(philosopher.id)}
            className="bg-white hover:bg-gray-100 text-gray-800 font-semibold py-2 px-4 border border-gray-400 rounded shadow"
          >
            {philosopher.name}
            <span className="block text-sm text-gray-500">{philosopher.period}</span>
          </button>
        ))}
      </div>
    </div>
  );
};

export default PhilosopherSelector;