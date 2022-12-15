// https://developer.mozilla.org/fr/docs/Web/API/Service_Worker_API/Using_Service_Workers#r%C3%A9ponses_personnalis%C3%A9es_aux_requ%C3%AAtes

this.addEventListener('fetch', function(event) {
    event.respondWith(
      // la magie opère ici
    );
  });
  