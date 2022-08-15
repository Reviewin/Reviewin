import { h } from 'preact';
import { useEffect, useState } from 'preact/hooks';

import { Button, Center, Flex, FormControl, FormErrorMessage, FormHelperText, FormLabel, Heading, Icon, IconButton, Input, VStack } from '@chakra-ui/react';
import { BiHelpCircle } from "react-icons/bi";
import { route } from 'preact-router';

const Login = (mode) => {
    useEffect(() => {
        document.title = "Log in to Reviewin"
    })

    const [username, setUsername] = useState("")
    const [usernameError, setUsernameError] = useState("")
    const [password, setPassword] = useState("")
    const [passwordError, setPasswordError] = useState("")

    const handleUsernameChange = (e) => setUsername(e.target.value)
    const handlePasswordChange = (e) => setPassword(e.target.value)
    const handleSubmit = (e) => {
        e.preventDefault()
        window.rvwnClient.authenticate(username, password)
        .then((token) => {
            window.rvwnClient.getSession()
            .then((session) => {
                console.log(session)
                route("/", true)
            })
            .catch((err) => {
                if (err) { console.log(err); }
                else { alert("Failed to get session after successful authentication. Please try again later.")}
            })
        })
        .catch((err) => {
            if (err) { alert(err); }
            else { alert("Please check the provided information and try again.") }
        })
    }

    return (
        <Flex as="main" h="100%" justify="center" align="center" bg="yellow.100">
            <VStack>
                <Heading as="h1" size="md" textAlign="center">Log in to Reviewin</Heading>
                <form onSubmit={handleSubmit}>
                    <FormControl isRequired isInvalid={usernameError}>
                        <FormLabel htmlFor="email">E-mail address</FormLabel>
                        <Input id="email" name="email" type="email" onChange={handleUsernameChange}></Input>
                        <FormErrorMessage>{usernameError}</FormErrorMessage>
                    </FormControl>
                    <FormControl isRequired isInvalid={passwordError}>
                        <FormLabel htmlFor="password">Password</FormLabel>
                        <Input id="password" name="password" type="password" onChange={handlePasswordChange}></Input>
                        <FormHelperText>{password}</FormHelperText>
                        <FormErrorMessage>{passwordError}</FormErrorMessage>
                    </FormControl>
                    <Flex justify="space-between">
                        <Button type="submit" colorScheme="yellow">Log in</Button>
                        <IconButton icon={<Icon as={BiHelpCircle} />} />
                    </Flex>
                </form>
            </VStack>
        </Flex>
    )
}

export default Login;