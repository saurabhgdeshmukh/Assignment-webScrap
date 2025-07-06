import { createApp } from 'vue'
import App from './App.vue'

// Global CSS reset
const globalStyles = `
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  html, body {
    margin: 0;
    padding: 0;
    width: 100%;
    height: 100%;
    font-family: 'Gotham', sans-serif;
  }
  
  #app {
    margin: 0;
    padding: 0;
    width: 100%;
    min-height: 100vh;
  }
`;

// Create and inject global styles
const styleSheet = document.createElement("style");
styleSheet.textContent = globalStyles;
document.head.appendChild(styleSheet);

createApp(App).mount('#app')