pragma solidity ^0.4.0;

contract Product {

    // Define a basic structure of an item
    struct Item {
        string name;
        string category;
        string sku_number;
        string url;
    }

    mapping(address => Item) public items;

    // Setter of a brand new product
    function setProduct(
        string _name,
        string _category,
        string _sku_number,
        string _url
    ) constant public returns (address) {
        address _chief = msg.sender;

        items[_chief].name = _name;
        items[_chief].category = _category;
        items[_chief].sku_number = _sku_number;
        items[_chief].url = _url;

        return _chief;
    }

    // Getter of a product
    function getProduct(address _chief) public constant returns (
        string,
        string,
        string,
        string
    ) {
        return (
        items[_chief].name,
        items[_chief].category,
        items[_chief].sku_number,
        items[_chief].url
        );
    }
}
