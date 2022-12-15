import { Button, ScaleFade } from '@chakra-ui/react';
import { Component, Fragment, h } from 'preact';

class InstallButton extends Component {
    constructor() {
        super();
        this.state = { shown: false }
    }

    render() {
        return (
            <div>
                <ScaleFade in={this.state.shown} initialScale="0.5">
                    {this.props.installable && (
                        <Button colorScheme="yellow" onClick={this.props.install}>
                            Installer
                        </Button>
                    )}
                </ScaleFade>
            </div>
        )
    }
};

export default InstallButton;
