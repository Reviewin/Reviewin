import { h } from 'preact';
import { Router } from 'preact-router';

import { ChakraProvider, extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
	
})

import Header from './header';
// Code-splitting is automated for `routes` directory
import Entrance from "../routes/entrance";
import Main from "../routes/main";
import Login from "../routes/login";

const App = () => (
	<ChakraProvider theme={theme}>
		<div id="app">
			{/*<Header />*/}
			<Router>
				<Entrance path="/" />
				<Main path="/:r*"></Main>
				<Login path="/login/" />
			</Router>
		</div>
	</ChakraProvider>
)

export default App;
