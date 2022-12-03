// https://esbuild.github.io/api/

const fs = require("fs-extra");
const path = require("path");
const http = require("http");

// https://github.com/evanw/esbuild/issues/266#issuecomment-787212174
const preactCompatPlugin = {
    name: "preact-compat",
    setup(build) {
        const path = require("path");
        const preact = path.join(process.cwd(), "node_modules", "preact", "compat", "dist", "compat.module.js");

        build.onResolve({filter: /^(react-dom|react)$/}, args => {
            return {path: preact};
        });
    }
}

const buildOptions = {
	entryPoints: ["src/index.js"],
	bundle: true,
	plugins: [preactCompatPlugin],
	loader: {".js": "jsx"},
	jsxFactory: "h",
	jsxFragment: "Fragment",
	target: ["es2016"],
	outdir: "dist/js"
}

let servePort = 8000;
let proxyPort = 3000;

fs.mkdirs(path.join(__dirname, "dist")).then(() => {
	//fs.copyFile(path.join(__dirname, "src", "index.html"), path.join(__dirname, "dist", "index.html"))
	fs.copy(path.join(__dirname, "src", "webroot"), path.join(__dirname, "dist"))
	.then(() => {
		fs.copy(path.join(__dirname, "dist", "assets", "favicon.ico"), path.join(__dirname, "dist", "favicon.ico"))
	})

	/* IMPORTANT : les serveurs mis ici en fonctionnement sont destinés au développement.
	En production, les fichiers statiques compilés de l'application doivent être envoyés
	sur un serveur web compétent. */

	if (process.argv[2] == "serve") {
		require("esbuild").serve({
			servedir: "dist",
			port: servePort
		}, buildOptions)
		.then(r => {
			const {host, port} = r;
			servePort = port;
			console.log("Serveur esbuild interne en écoute sur le port", servePort);

			// En grande partie repompé sur la doc d'esbuild : https://esbuild.github.io/api/#customizing-server-behavior
			/* Création d'un serveur proxy en facade du serveur intégré à esbuild :
			copie, modifie et envoie à esbuild les requêtes qu'il reçoit d'un client,
			renvoie au client la réponse qu'il a reçu d'esbuild

			Ici, l'intérêt est de rediriger toute requête pour un chemin iconnu pour pointer sur index.html,
			afin de tester le routage côté javascript

			Cela n'étant pas possible avec le serveur d'esbuild, on met notre propre proxy devant.
			*/

			http.createServer((req, res) => {
				console.log("\nRequested path:", req.url)

				// Répertoire dont les fichiers sont servis par esbuild (cf ligne 39)
				// et donc indirectement par le proxy
				const webroot = path.join(__dirname, "dist");

				// req.url contient le chemin de fichier/dossier demandé dans l'url de la requête
				// on obtient le fichier/dossier correspondant sur la machine en ajoutant ce chemin à la webroot
				req_file = path.join(webroot, req.url);
				console.log("Matching local path:", req_file);

				// obtention d'informations sur le chemin :
				// s'il existe, la promesse résout (.then), sinon elle échoue (.catch)
				fs.stat(req_file)
				// si le chemin existe
				.then((s) => {
					//console.log(s);
					console.log("Local path exists.");
					
					// on utilise un timeout instantané pour que la fonction soit appelée
					// en dehors des handlers (.then et .catch) de la promesse renvoyée par fs.stat
					setTimeout(doProxyRequest, 0)
				})
				// si le chemin n'existe pas
				.catch((e) => {
					//console.log(e);
					console.log("Local path does not exist. Using fallback.");
					// utiliser le fichier index.html à la racine (de la webroot)
					// le javascript de cette page gère ensuite le routage
					req.url = "/index.html";
					console.log("Internally redirecting request to", req.url);

					// on utilise un timeout instantané pour que la fonction soit appelée
					// en dehors des handlers (.then et .catch) de la promesse renvoyée par fs.stat
					setTimeout(doProxyRequest, 0)
					// ref https://javascript.info/promise-error-handling
					// ref https://stackoverflow.com/a/38059322
				})

				function doProxyRequest() {
					// définition de la requête à esbuild
					// host et port sont ceux de esbuild (cf ligne 48)
					const options = {
						hostname: host,
						port: port,
						path: req.url,
						method: req.method,
						headers: req.headers
					}

					console.log("Sending upstream request with path:", options.path);
					// démarre une requête http au serveur esbuild
					// la fonction callback (2e paramètre) est appelée quand une réponse est reçue
					const upstreamReq = http.request(options, upstreamRes => {
						// res est la réponse qui sera envoyée au client (cf ligne 55)
						// upstreamRes est la réponse obtenue de esbuild
						res.writeHead(upstreamRes.statusCode, upstreamRes.headers);
						upstreamRes.pipe(res, {end: true})
					})

					// ceci est donc effectué avant le callback
					req.pipe(upstreamReq, { end: true })
				}
			}).listen(proxyPort, () => {
				console.log("Serveur de développement en écoute.");
				console.log("Application disponible à l'adresse http://localhost:" + proxyPort);
			})
		})
	}
	else {
		require("esbuild").build(buildOptions)
		.then((result) => {
			console.log("Succès")
		})
		.catch(() => process.exit(1))
	}
})

/* CODE INUTILISÉ */

// on catch toute éventuelle erreur ici pour pas qu'elle ne soit catch
// au bloc d'après
/*.catch((e) => {
	console.log(e)
	console.log("Error in upstream request.");
})*/

/* un peu useless puisque esbuild sait rediriger un chemin de dossier vers index.html

fs.opendir(req_file)
// si le chemin est un dossier
.then((d) => {
	console.log("Local path is a folder.");
	// utiliser le fichier index.html de ce dossier
	req.url = path.join(req.url, "index.html");
	console.log("Internally redirecting request to", req.url);
})

*/
