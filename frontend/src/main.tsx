import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'

const contentElement = document.getElementById('root') ?? new HTMLElement()

ReactDOM.createRoot(contentElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)
