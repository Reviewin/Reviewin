// https://esbuild.github.io/api/

const fs = require("fs-extra");
const path = require("path");

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

fs.mkdirs(path.join(__dirname, "dist")).then(() => {
	fs.copyFile(path.join(__dirname, "src", "index.html"), path.join(__dirname, "dist", "index.html"))
	fs.copy(path.join(__dirname, "src", "assets"), path.join(__dirname, "dist", "assets"))
	.then(() => {
		fs.copy(path.join(__dirname, "dist", "assets", "favicon.ico"), path.join(__dirname, "dist", "favicon.ico"))
	})

	if (process.argv[2] == "serve") {
		require("esbuild").serve({
			servedir: "dist",
			port: 8000
		}, buildOptions)
	}
	else {
		require("esbuild").build(buildOptions)
		.then((result) => {})
		.catch(() => process.exit(1))
	}
})