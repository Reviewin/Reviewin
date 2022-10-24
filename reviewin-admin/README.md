# reviewin-admin

Interface web destinée aux partenaires pour le service Reviewin, incluant une implémentation factice de l'API Reviewin.

Ce code renferme de nombreuses erreurs de programmation, je déconseille donc de l'utiliser tel quel en l'état.

## note about Chakra UI
Chakra 2.x requires support for [useId in react 18](https://github.com/preactjs/preact/issues/3373),
which is currently not implemented in Preact.
Currently [using Chakra 1.x](https://github.com/redwoodjs/redwood/issues/5601#issuecomment-1133584714), should update Preact and Chakra when possible.

## Commandes de développement

``` bash
# installer les dépendances
npm install

# démarre un serveur de développement à l'adresse indiquée
# recompile automatiquement lors des modifications
node build.js serve

# compiler l'application pour la production dans /dist
npm run build

```
