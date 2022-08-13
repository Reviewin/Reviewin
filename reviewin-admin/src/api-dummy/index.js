class ReviewinClient {
	constructor() {
		this.token = window.localStorage.getItem("rvwntoken") || ""
		this.sessionCache = {}

		this.sessionDummy = JSON.parse(window.localStorage.getItem("sessionDummy")) || {}
	}

	authenticate(username, password) {return new Promise((resolve, reject) => {
		const users = [
			{
				username: "poositight",
				password: "poosiclean",
				role: "partner"
			},
			{
				username: "kanar",
				password: "texte du bas",
				role: "consumer"
			}
		]

		const filtered = users.filter(user => user.username == username)
		if (filtered[0]) {
			const user = filtered[0]
			if (user.password == password) {
				this.token = "dummy"
				window.localStorage.setItem("rvwntoken", this.token)

				// the server would handle storing the session
				this.sessionDummy.user = user
				window.localStorage.setItem("sessionDummy", JSON.stringify(this.sessionDummy))

				this.sessionCache = this.sessionDummy

				resolve(this.token)
			}
			else {
				reject("Invalid password")
			}
		}
		else {
			reject("Unknown user")
		}
	})}

	getSession() {return new Promise((resolve, reject) => {
		console.log("called getSession")
		if (this.token) {
			// the token would be checked by the server which would return the session
			if (this.token == "dummy") {
				resolve(this.sessionDummy)
			}
			else {
				reject("Invalid or expired session, please re-authenticate")
			}
		}
		else {
			reject("Please authenticate first")
		}
	})}

	getUserProducts() {return new Promise((resolve, reject) => {
		console.log("called getUserProducts")
		const products = [
			{
				id: 1287288,
				name: "Lorem ipsum dolor sit amet"
			},
			{
				id: 3850275,
				name: "Consectetur adispicing eit"
			}
		]
		this.getSession().then((session) => {
			// role check would be done both client and server-side (the latter being the most important)
			if (session.user.role == "partner") {
				resolve(products)
			}
			else {
				reject("This account cannot manage products")
			}
		})
		.catch((err) => reject(err))
	})}

	logOut() {return new Promise((resolve, reject) => {
		this.token = ""
		window.localStorage.removeItem("rvwntoken")

		this.sessionCache = {}

		this.sessionDummy = {}
		window.localStorage.removeItem("sessionDummy")

		resolve()
	})}
}

export default ReviewinClient;