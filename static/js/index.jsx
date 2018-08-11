import bugsnag from 'bugsnag-js'
// # Bugsnag is an error monitoring tool. This will track all client-side errors.
const bugsnagClient = bugsnag('cf8dfcc6a740905747ae226e6d67380d');

import ReactDOM from 'react-dom'
import React from 'react'
import createPlugin from 'bugsnag-react'
import App from './App.jsx';



var ErrorBoundary = bugsnagClient.use(createPlugin(React))
ReactDOM.render(
  <ErrorBoundary>
    <App />
  </ErrorBoundary>,
  document.getElementById('app-root')
);


console.log("js loaded")
