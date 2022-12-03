import { Component, Fragment, h } from 'preact';

import ProductNav from "../../components/product-nav";

import { Flex, Heading, Icon, Tabs, TabList, Tab, TabPanels, TabPanel } from "@chakra-ui/react";
import { BiCog, BiCommentDetail, BiEdit, BiGroup, BiMale } from "react-icons/bi";

class SingleProductPage extends Component {
    constructor() {
        super();
        this.state = {product: []}
    }

    componentDidMount() {
        document.title = "Reviewin";
        if (this.props.id) {
            window.rvwnClient.getProductById(this.props.id)
            .then((product) => {
                this.setState({product: product})
                document.title = product.name + " : Manage product - Reviewin"
            })
            .catch((err) => {
                if (err) { alert(err) }
            })
        }
    }

    render() {
        return (
        <Flex direction="column" w="100%">
            <Tabs isManual isLazy colorScheme="yellow">
                <TabList as={Flex} w="100%" px="4" bg="gray.100" align="center">
                    <Heading as="h1" size="md">{this.state.product.name}</Heading>
                    <Tab><Icon as={BiMale} />Demographics</Tab>
                    <Tab><Icon as={BiCommentDetail} />Reviews</Tab>
                    <Tab ml="auto"><Icon as={BiEdit} />Edit product</Tab>
                    <Tab><Icon as={BiCog} aria-label="Manage product"/></Tab>
                </TabList>
                <TabPanels>
                    <TabPanel>Tab 1</TabPanel>
                    <TabPanel>Tab 2</TabPanel>
                    <TabPanel>Tab 3</TabPanel>
                    <TabPanel>Tab 4</TabPanel>
                </TabPanels>
            </Tabs>
            <Flex w="100%" px="4">
                <h1>{this.state.product.name}</h1>
            </Flex>
        </Flex>
        )
    }
}

export default SingleProductPage;
