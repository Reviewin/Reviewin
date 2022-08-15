import { Component, Fragment, h } from 'preact';

import { Heading } from "@chakra-ui/react";

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
            <>
                <Heading as="h2">Manage your products</Heading>
                <ol>
                    {list}
                </ol>
            </>
        )
    }
}

export default ProductList;