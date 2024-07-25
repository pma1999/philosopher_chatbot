import React from 'react';
import { useAppContext } from '../contexts/AppContext';

const ConfigOptions: React.FC = () => {
  const { resetChat, changePhilosopher, changeLanguage, changeApiKey } = useAppContext();

  const handleCloseProgram = () => {
    window.close();
  };

  return (
    <div className="flex flex-col space-y-2">
      <button onClick={resetChat} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Reset Chat
      </button>
      <button onClick={changePhilosopher} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Change Philosopher
      </button>
      <button onClick={changeLanguage} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Change Language
      </button>
      <button onClick={changeApiKey} className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Change API Key
      </button>
      <button onClick={handleCloseProgram} className="px-4 py-2 bg-red-500 text-white rounded hover:bg-red-600">
        Close Program
      </button>
    </div>
  );
};

export default ConfigOptions;