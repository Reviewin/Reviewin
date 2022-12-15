import './style';
import { h, render } from "preact";
import App from './components/app';

import ReviewinClient from "./api-dummy"
window.rvwnClient = new ReviewinClient();


render(<App />, document.body)

// L'enregistrement d'un service worker est nécessaire pour rendre le site installable
// https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API/Using_Service_Workers#enregistrer_un_worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register('/sw.js', { scope: '/' }).then(function(reg) {
      // registration worked
      console.log('Registration succeeded. Scope is ' + reg.scope);
    }).catch(function(error) {
      // registration failed
      console.log('Registration failed with ' + error);
    });
  };
  