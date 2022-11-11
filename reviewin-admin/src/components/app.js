import { h } from 'preact';
import { Router } from 'preact-router';

import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
	
})

// Code-splitting is automated for `routes` directory
import Entrance from "../routes/entrance";
import LoggedInWrapper from "../routes/logged-in-wrapper";
import Login from "../routes/login";

const App = () => (
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
)

export default App;
