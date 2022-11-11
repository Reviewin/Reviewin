import { Component, Fragment, h } from 'preact';

import MainNav from "../../components/main-nav"
import ProductList from "../product-list";
import GiftList from "../gift-list";
import UserSettings from "../user-settings";

import { Flex } from '@chakra-ui/react';
import { Router, route } from 'preact-router';
//import { Link as MatchLink } from 'preact-router/match';

class Main extends Component {
    constructor() {
        super();
        this.state = { session: {} }
    }

    handleLogOut() {
        //window.localStorage.removeItem("role")
        window.rvwnClient.logOut()
        .then(() => {
            route("/", true)
        })
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
            <MainNav session={this.state.session} />
            <Flex as="main" marginTop="3em" w="100%">
                <Router>
                    <ProductList path="/products/" />
                    <GiftList path="/gifts/" />
                    <UserSettings path="/settings/" />
                </Router>
            </Flex>
        </Flex>
        )
    }
}

export default Main;