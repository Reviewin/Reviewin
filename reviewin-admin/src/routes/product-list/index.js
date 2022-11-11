import { Component, Fragment, h } from 'preact';

import { Button, Flex, Heading, Link, Spacer } from "@chakra-ui/react";

class ProductList extends Component {
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
            <li key={product.id}>{product.name}</li>
        ))

        return (
            <Flex direction="column" w="100%">
                <Flex w="100%" align="center" p="4">
                    <Heading as="h2" size="md">Manage your products</Heading>
                    <Link href="/products/new" ml="auto">
                    	{/* tabindex="-1" allows only the Link to be reached by keyboard navigation */}
                        <Button colorScheme="gray" tabindex="-1">Submit new product</Button>
                    </Link>
                </Flex>
                <br />
                <ol>
                    {list}
                </ol>
            </Flex>
        )
    }
}

export default ProductList;