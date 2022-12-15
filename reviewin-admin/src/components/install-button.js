import { Button, ScaleFade } from '@chakra-ui/react';
import { Component, Fragment, h } from 'preact';
import { useContext } from 'preact/hooks';

import AppContext from "./app-context";

class InstallButton extends Component {
    constructor() {
        super();
        this.state = { shown: false }
    }
	
	installApp() {
		const context = useContext(AppContext);
		context.deferredHook.prompt();
	}
	
    render() {
        return (
            <AppContext.Consumer>
            	{appcontext => (
					<ScaleFade in={appcontext.installable}>
	                    {appcontext.installable && (
	                        <Button colorScheme="yellow" onClick={this.installApp}>
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
