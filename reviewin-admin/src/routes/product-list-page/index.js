import { Component, Fragment, h } from 'preact';

import { BiPlusCircle } from "react-icons/bi";
import { Box, Button, Flex, Heading, Icon, Image, Link, List, ListItem, SimpleGrid, Spacer } from "@chakra-ui/react";

class ProductListPage extends Component {
    constructor() {
        super();
        this.state = {products: []}
    }

    componentDidMount() {
        document.title = "Products - Reviewin";
        window.rvwnClient.getUserProducts()
        .then((products) => {
            this.setState({products: products})
        })
        .catch((err) => {
            if (err) { alert(err) }
        })
    }

    render() {
        let list = this.state.products.map((product) => (
            <ListItem key={product.id}>
                <Link href={`/products/id/${product.id}`}>
                    <Box>
                        <Image w="100%" h="100%" fit="cover" src={product.images[0].url} />
                        {product.name}
                    </Box>
                </Link>
            </ListItem>
        ))

        return (
            <Flex direction="column" w="100%" px="4">
                <Flex w="100%" align="center" py="4">
                    <Heading as="h2" size="md">Manage your products</Heading>
                    <Link href="/products/new" ml="auto">
                    	{/* tabindex="-1" allows only the Link to be reached by keyboard navigation */}
                        <Button colorScheme="gray" tabindex="-1" leftIcon={<Icon as={BiPlusCircle} />}>
                        Submit new product
                        </Button>
                    </Link>
                </Flex>
                <SimpleGrid as={List} columns={[1, null, 2, 4]} spacing={6}>
                	{list}
                </SimpleGrid>
                <br />
                {/*	Note to self : don't put Chakra's ListItems with a regular <ol> or <ul>
                	else the app doesn't render with error :
                	useStyles: `styles` is undefined. Seems you forgot to wrap the components in a `<*List />`
                */}
            </Flex>
        )
    }
}

export default ProductListPage;
