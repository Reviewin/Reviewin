import { Button, ScaleFade } from '@chakra-ui/react';
import { Component, Fragment, h } from 'preact';

class InstallButton extends Component {
    constructor() {
        super();
        this.state = { shown: {} }
    }

    deferredPrompt;

    componentDidMount() {
        window.addEventListener("beforeinstallprompt", (e) => {
            e.preventDefault();
            this.deferredPrompt = e;
            console.log(this.deferredPrompt)
            this.setState({shown: true})
        })
    }

    installApp() {
        this.deferredPrompt.prompt()
    }

    render() {
        return (
            <div>
                <ScaleFade in={this.state.shown} initialScale="0.5">
                    {this.state.shown && (
                        <Button colorScheme="yellow" onClick={this.installApp}>
                            Installer
                        </Button>
                    )}
                </ScaleFade>
            </div>
        )
    }
};

export default InstallButton;
