// src/main.jsx

import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App.jsx';

// 1. IMPORTACIÓN DE BOOTSTRAP (PRIMERO)
import 'bootstrap/dist/css/bootstrap.min.css'; 

// 2. IMPORTACIÓN DE TUS ESTILOS PERSONALIZADOS (SEGUNDO)
import './App.css'; // <--- ¡Asegúrate de añadir esta línea!

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
);