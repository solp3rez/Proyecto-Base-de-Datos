import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Ingles from './components/Ingles.jsx';


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <App />
    <Ingles />
  </StrictMode>,
)
