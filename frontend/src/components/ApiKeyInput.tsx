import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAppContext } from '../contexts/AppContext';
import { validateApiKey } from '../services/api';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faEye, faEyeSlash } from '@fortawesome/free-solid-svg-icons';

const ApiKeyInput: React.FC = () => {
  const { setApiKey, setCurrentStep, currentStep, apiKey } = useAppContext();
  const [inputKey, setInputKey] = useState(apiKey || '');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [isKeyVisible, setIsKeyVisible] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (currentStep !== 'apiKey') {
      const storedApiKey = localStorage.getItem('anthropic_api_key');
      if (storedApiKey) {
        setApiKey(storedApiKey);
        setCurrentStep('philosopher');
        navigate('/select-philosopher');
      }
    }
  }, [setApiKey, setCurrentStep, navigate, currentStep]);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);
    try {
      const isValid = await validateApiKey(inputKey);
      if (isValid) {
        localStorage.setItem('anthropic_api_key', inputKey);
        setApiKey(inputKey);
        setCurrentStep('philosopher');
        navigate('/select-philosopher');
      } else {
        setError('Invalid API Key');
      }
    } catch (error) {
      setError(error instanceof Error ? error.message : 'Error validating API Key');
    } finally {
      setIsLoading(false);
    }
  };

  const toggleKeyVisibility = () => {
    setIsKeyVisible(!isKeyVisible);
  };

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-2xl font-bold mb-4">Enter Anthropic API Key</h2>
      <form onSubmit={handleSubmit} className="w-full max-w-sm">
        <div className="flex items-center border-b border-b-2 border-blue-500 py-2">
          <input
            className="appearance-none bg-transparent border-none w-full text-gray-700 mr-3 py-1 px-2 leading-tight focus:outline-none"
            type={isKeyVisible ? 'text' : 'password'}
            placeholder="API Key"
            value={inputKey}
            onChange={(e) => setInputKey(e.target.value)}
            disabled={isLoading}
          />
          <button
            type="button"
            onClick={toggleKeyVisibility}
            className="flex-shrink-0 bg-gray-500 hover:bg-gray-700 text-sm border-4 text-white py-1 px-2 rounded"
          >
            <FontAwesomeIcon icon={isKeyVisible ? faEyeSlash : faEye} />
          </button>
          <button
            className={`flex-shrink-0 bg-blue-500 hover:bg-blue-700 border-blue-500 hover:border-blue-700 text-sm border-4 text-white py-1 px-2 rounded ml-2 ${
              isLoading ? 'opacity-50 cursor-not-allowed' : ''
            }`}
            type="submit"
            disabled={isLoading}
          >
            {isLoading ? 'Validating...' : 'Submit'}
          </button>
        </div>
      </form>
      {error && <p className="text-red-500 mt-2">{error}</p>}
    </div>
  );
};

export default ApiKeyInput;
