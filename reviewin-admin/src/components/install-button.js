import { Button, ScaleFade } from '@chakra-ui/react';
import { Component, Fragment, h } from 'preact';
import { useContext } from 'preact/hooks';

import AppContext from "./app-context";

class InstallButton extends Component {
    constructor() {
        super();
        this.state = { shown: false }
    }
	
	installApp(appcontext) {
		//const context = useContext(AppContext);
		appcontext.deferredPrompt.prompt();
	}
	
    render() {
        return (
            <AppContext.Consumer>
            	{appcontext => (
					<ScaleFade in={appcontext.installable} initialScale={0.1}>
	                    {appcontext.installable && (
	                        <Button colorScheme="yellow" onClick={() => this.installApp(appcontext)}>
	                            Installer
	                        </Button>
	                    )}
	                </ScaleFade>
				)}
            </AppContext.Consumer>
        )
    }
};

export default InstallButton;
