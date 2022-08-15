import { Component, Fragment, h } from 'preact';

import Entrance from "../entrance";
import ProductList from "../product-list";
import GiftList from "../gift-list";
import UserSettings from "../user-settings";

import { Button, Flex, Heading, Icon, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Text, HStack, VStack } from '@chakra-ui/react';
import { BiChevronDown } from 'react-icons/bi';
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
            <Flex as="nav" w="100%" h="3em" position="fixed" lign="center" px="4" bg="yellow.100">
                <HStack mr="auto">
                    <Heading as="h1" size="md">Reviewin</Heading>
                    { this.state.session.user && this.state.session.user.role == "partner"  &&  (
                        <>
                            <Link href="/products/">Products</Link>
                            <Link href="/gifts/">Gifts</Link>
                        </>
                    )}
                </HStack>
                <Flex ml="auto">
                    { this.state.session.user ? (
                        <Menu>
                            <MenuButton as={Button} variant="ghost" rightIcon={<Icon as={BiChevronDown} />}>
                                {this.state.session.user.displayName}
                            </MenuButton>
                            <MenuList>
                                <MenuItem as={Link} href="/settings">Settings</MenuItem>
                                <MenuDivider />
                                <MenuItem onClick={this.handleLogOut}>Log out</MenuItem>
                            </MenuList>
                        </Menu>
                    ) : (
                        <Text>Reviewin User</Text>
                    )}
                </Flex>
            </Flex>
            <Flex as="main" marginTop="3em">
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