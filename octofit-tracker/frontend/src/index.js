import 'bootstrap/dist/css/bootstrap.min.css';

// Set REACT_APP_CODESPACE_NAME from window.location if running in Codespaces
if (!process.env.REACT_APP_CODESPACE_NAME && window.location.hostname.endsWith('.app.github.dev')) {
  const codespace = window.location.hostname.split('-8000')[0];
  process.env.REACT_APP_CODESPACE_NAME = codespace;
  console.log('Detected Codespace:', codespace);
}
import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
