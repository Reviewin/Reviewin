class ReviewinClient {
	constructor() {
		this.token = window.localStorage.getItem("rvwntoken") || ""
		this.sessionCache = {}

		this.sessionDummy = JSON.parse(window.localStorage.getItem("sessionDummy")) || {}
	}

	authenticate(email, password) {return new Promise((resolve, reject) => {
		const users = [
			{
				displayName: "Poosi Tight SARL",
				email: "contact@poositight.tld",
				password: "poosiclean",
				role: "partner"
			},
			{
				displayName: "Kanar Kanar",
				email: "kanar@superboitemail.tld",
				password: "texte du bas",
				role: "consumer"
			}
		]

		const filtered = users.filter(user => user.email == email)
		if (filtered[0]) {
			const user = filtered[0]
			if (user.password == password) {
				this.token = "dummy"

				// the server would handle storing the session
				this.sessionDummy.user = user
				window.localStorage.setItem("sessionDummy", JSON.stringify(this.sessionDummy))

				this.sessionCache = this.sessionDummy

				window.localStorage.setItem("rvwntoken", this.token)
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
				name: "racism ender",
				images: [
					{"url": "https://picsum.photos/id/22/367/267"}
				]
			},
			{
				id: 3850275,
				name: "gromit mug",
				images: [
					{"url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fimages-na.ssl-images-amazon.com%2Fimages%2FI%2F71fS2SBKk4L._AC_SL1500_.jpg&f=1&nofb=1&ipt=99dff3fd7fcf8fc7dde39489a6e7e461660376cad6a0e8a8915e65c7d564a9f8&ipo=images"}
				]
			},
			{
				id: 4637284,
				name: "plateauschuhe aquarium",
				images: [
					{"url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.GuDZndfp01q2APCRyfoz4QHaHa%26pid%3DApi&f=1&ipt=caa3ed582c934561f225b096dfc40cf19581c80935688f0ff367e7815ba87515&ipo=images"}
				]
			},
			{
				id: 7465923,
				name: "plateauschuhe aquarium",
				images: [
					{"url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.GuDZndfp01q2APCRyfoz4QHaHa%26pid%3DApi&f=1&ipt=caa3ed582c934561f225b096dfc40cf19581c80935688f0ff367e7815ba87515&ipo=images"}
				]
			},
			{
				id: 1284572,
				name: "plateauschuhe aquarium",
				images: [
					{"url": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.GuDZndfp01q2APCRyfoz4QHaHa%26pid%3DApi&f=1&ipt=caa3ed582c934561f225b096dfc40cf19581c80935688f0ff367e7815ba87515&ipo=images"}
				]
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