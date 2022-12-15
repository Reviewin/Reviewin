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
		this.state = {}
	}

	componentDidMount() {
        window.addEventListener("beforeinstallprompt", (e) => {
            e.preventDefault();
            console.log("beforeinstallprompt called")
            this.setState({
				deferredPrompt: e,
				installable: true
			})
        })
    }

	render() {
		return (
			<AppContext.Provider value={this.state}>
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
