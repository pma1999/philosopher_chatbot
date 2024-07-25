import React, { createContext, useState, useContext, ReactNode, useEffect } from 'react';

interface AppContextType {
  language: string;
  setLanguage: (lang: string) => void;
  apiKey: string;
  setApiKey: (key: string) => void;
  philosopherId: string;
  setPhilosopherId: (id: string) => void;
  sessionId: string;
  setSessionId: (id: string) => void;
  resetChat: () => void;
  changePhilosopher: () => void;
  changeLanguage: () => void;
  changeApiKey: () => void;
  currentStep: 'language' | 'apiKey' | 'philosopher' | 'chat';
  setCurrentStep: (step: 'language' | 'apiKey' | 'philosopher' | 'chat') => void;
}

const AppContext = createContext<AppContextType | undefined>(undefined);

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [language, setLanguageState] = useState<string>('');
  const [apiKey, setApiKeyState] = useState<string>('');
  const [philosopherId, setPhilosopherId] = useState<string>('');
  const [sessionId, setSessionId] = useState<string>('');
  const [currentStep, setCurrentStep] = useState<'language' | 'apiKey' | 'philosopher' | 'chat'>('language');

  const setLanguage = (lang: string) => {
    setLanguageState(lang.toLowerCase());
    setCurrentStep('apiKey');
  };

  const setApiKey = (key: string) => {
    localStorage.setItem('anthropic_api_key', key);
    setApiKeyState(key);
  };

  useEffect(() => {
    const storedApiKey = localStorage.getItem('anthropic_api_key');
    if (storedApiKey && currentStep !== 'apiKey') {
      setApiKeyState(storedApiKey);
    }
  }, [currentStep]);

  const resetChat = () => {
    setCurrentStep('philosopher');
  };

  const changePhilosopher = () => {
    setPhilosopherId('');
    setCurrentStep('philosopher');
  };

  const changeLanguage = () => {
    setLanguageState('');
    setCurrentStep('language');
  };

  const changeApiKey = () => {
    setCurrentStep('apiKey');
  };

  return (
    <AppContext.Provider value={{ 
      language, setLanguage,
      apiKey, setApiKey, 
      philosopherId, setPhilosopherId,
      sessionId, setSessionId,
      resetChat,
      changePhilosopher,
      changeLanguage,
      changeApiKey,
      currentStep,
      setCurrentStep
    }}>
      {children}
    </AppContext.Provider>
  );
};

export const useAppContext = () => {
  const context = useContext(AppContext);
  if (context === undefined) {
    throw new Error('useAppContext must be used within an AppProvider');
  }
  return context;
};
