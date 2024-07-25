import React from 'react';
import { BrowserRouter as Router } from 'react-router-dom';
import { AppProvider, useAppContext } from './contexts/AppContext';
import LanguageSelector from './components/LanguageSelector';
import ApiKeyInput from './components/ApiKeyInput';
import PhilosopherSelector from './components/PhilosopherSelector';
import ChatInterface from './components/ChatInterface';
import ConfigOptions from './components/ConfigOptions';

const AppContent: React.FC = () => {
  const { currentStep } = useAppContext();

  const renderCurrentStep = () => {
    switch (currentStep) {
      case 'language':
        return <LanguageSelector />;
      case 'apiKey':
        return <ApiKeyInput />;
      case 'philosopher':
        return <PhilosopherSelector />;
      case 'chat':
        return <ChatInterface />;
      default:
        return <LanguageSelector />;
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <h1 className="text-3xl font-bold text-gray-900">Philosopher Chatbot</h1>
        </div>
      </header>
      <main className="flex-grow">
        <div className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
          {renderCurrentStep()}
        </div>
      </main>
      <footer className="bg-white shadow mt-auto">
        <div className="max-w-7xl mx-auto py-6 px-4 sm:px-6 lg:px-8">
          <ConfigOptions />
        </div>
      </footer>
    </div>
  );
};

const App: React.FC = () => {
  return (
    <AppProvider>
      <Router>
        <AppContent />
      </Router>
    </AppProvider>
  );
};

export default App;