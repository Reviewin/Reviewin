import { Component, Fragment, h } from 'preact';

import MainNav from "../../components/main-nav"
import ProductListPage from "../product-list-page";
import SingleProductPage from "../single-product-page";
import GiftList from "../gift-list";
import UserSettings from "../user-settings";

import { Flex } from '@chakra-ui/react';
import { Router, route } from 'preact-router';
//import { Link as MatchLink } from 'preact-router/match';

class LoggedInWrapper extends Component {
    constructor() {
        super();
        this.state = { session: {} }
    }

    componentDidMount() {
        window.rvwnClient.getSession()
        .then((s) => {this.setState({session: s})})
        .catch((err) => {
            if (err) { alert(err) }
            route("/login", true)
        })
    }

    render() {
        return (
        <Flex direction="vertical">
            <MainNav session={this.state.session} installable={this.props.installable} install={this.props.install}/>
            <Flex as="main" marginTop="3em" w="100%">
                <Router>
                    <ProductListPage path="/products/" />
                    <SingleProductPage path="/products/id/:id" />
                    <GiftList path="/gifts/" />
                    <UserSettings path="/settings/" />
                </Router>
            </Flex>
        </Flex>
        )
    }
}

export default LoggedInWrapper;
