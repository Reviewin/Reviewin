import { h } from 'preact';
import { useEffect, useState } from 'preact/hooks';

import { Heading } from "@chakra-ui/react";

const ProductList = () => {
    const [ products, setProducts ] = useState([])

    useEffect(() => {
        document.title = "Products - Reviewin"
    })

    useEffect(() => {
        window.rvwnClient.getUserProducts()
        .then((products) => {
            setProducts(products)
        })
        .catch((err) => {
            if (err) { alert(err) }
        })
    })


    const list = products.map((product) => (
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

export default ProductList;