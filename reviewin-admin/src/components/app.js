import { Component, h } from 'preact';
import { Router } from 'preact-router';

import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
	
})

// Code-splitting is automated for `routes` directory
import Entrance from "../routes/entrance";
import LoggedInWrapper from "../routes/logged-in-wrapper";
import Login from "../routes/login";
import { useState } from 'preact/hooks';

class App extends Component {
	constructor() {
		super();
		this.state = {installable: false}
	}

	deferredPrompt;

	componentDidMount() {
        window.addEventListener("beforeinstallprompt", (e) => {
            console.log("beforeinstallprompt")
            e.preventDefault();
            this.deferredPrompt = e;
            console.log(this.deferredPrompt)
            this.setState({installable: true})
        })
    }

    installApp() {
        this.deferredPrompt.prompt()
    }

	render() {
		return (
			<ChakraProvider theme={theme}>
				<div id="app">
					{/*<Header />*/}
					<Router>
						<Entrance path="/" />
						<LoggedInWrapper path="/:r*" installable={this.installable} install={this.installApp}></LoggedInWrapper>
						<Login path="/login/" />
					</Router>
				</div>
			</ChakraProvider>
		)
	}
}

export default App;
