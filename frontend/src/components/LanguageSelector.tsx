import React from 'react';
import { useAppContext } from '../contexts/AppContext';

const LanguageSelector: React.FC = () => {
  const { setLanguage } = useAppContext();

  const handleLanguageSelect = (lang: string) => {
    setLanguage(lang);
  };

  return (
    <div className="flex flex-col items-center">
      <h2 className="text-2xl font-bold mb-4">Select Language</h2>
      <div className="flex space-x-4">
        {['ES', 'EN', 'CA'].map((lang) => (
          <button
            key={lang}
            onClick={() => handleLanguageSelect(lang)}
            className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
          >
            {lang}
          </button>
        ))}
      </div>
    </div>
  );
};

export default LanguageSelector;