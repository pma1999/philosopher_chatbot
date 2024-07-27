import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';
import axios from 'axios';

axios.defaults.withCredentials = true;

// Configurar interceptores globales para manejar errores de red
axios.interceptors.response.use(
  response => response,
  error => {
    if (error.response && error.response.status === 500) {
      console.error('Internal server error occurred');
      // Aquí podrías mostrar un mensaje de error al usuario o redirigir a una página de error
    }
    return Promise.reject(error);
  }
);

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

reportWebVitals();