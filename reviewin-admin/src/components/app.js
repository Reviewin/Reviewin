import { Component, createContext, h } from 'preact';
import { useState } from 'preact/hooks';
import { Router } from 'preact-router';

import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
	
})

import AppContext from "./app-context";
// Code-splitting is automated for `routes` directory
import Entrance from "../routes/entrance";
import LoggedInWrapper from "../routes/logged-in-wrapper";
import Login from "../routes/login";

class App extends Component {
	constructor() {
		super();
	}

	context;

	componentDidMount() {
        window.addEventListener("beforeinstallprompt", (e) => {
            console.log("beforeinstallprompt")
            e.preventDefault();
            this.context.deferredPrompt = e;
            console.log(this.context.deferredPrompt)
            this.context.installable = true
        })
    }

    installApp() {
        this.context.deferredPrompt.prompt()
    }

	render() {
		return (
			<AppContext.Provider value={this.context}>
				<ChakraProvider theme={theme}>
					<div id="app">
						{/*<Header />*/}
						<Router>
							<Entrance path="/" />
							<LoggedInWrapper path="/:r*"></LoggedInWrapper>
							<Login path="/login/" />
						</Router>
					</div>
				</ChakraProvider>
			</AppContext.Provider>
		)
	}
}

export default App;
