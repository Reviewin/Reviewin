import { Component, Fragment, h } from 'preact';

import { Button, Flex, Heading, Icon, Link, Menu, MenuButton, MenuDivider, MenuItem, MenuList, Text, HStack, VStack } from '@chakra-ui/react';
import { BiChevronDown } from 'react-icons/bi';
import { route } from 'preact-router';


class MainNav extends Component {
    constructor() {
        super();
    }

    handleLogOut() {
        //window.localStorage.removeItem("role")
        window.rvwnClient.logOut()
        .then(() => {
            route("/", true)
        })
    }

    componentDidMount() {
    }

    render(props) {
        return (
        <Flex as="nav" w="100%" h="3em" zIndex="1" position="fixed" align="center" px="4" bg="yellow.100">
            <HStack mr="auto">
                <Heading as="h1" size="md">Reviewin</Heading>
                { props.session.user && props.session.user.role == "partner"  &&  (
                    <>
                        <Link href="/products/">Products</Link>
                        <Link href="/gifts/">Gifts</Link>
                    </>
                )}
            </HStack>
            <Flex ml="auto">
                { props.session.user ? (
                    <Menu>
                        <MenuButton as={Button} variant="ghost" rightIcon={<Icon as={BiChevronDown} />}>
                            {props.session.user.displayName}
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
        )
    }
}

export default MainNav;