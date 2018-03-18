pragma solidity ^0.4.0;

contract Product {

    // Define a basic structure of an item
    struct Item {
        string name;
        string title;
        string sku_number;
        string url;
    }

    mapping(address => Item) items;
    address[] products;

    // Setter of a brand new product
    function setProduct(
        string _name,
        string _title,
        string _sku_number,
        string _url
    ) public {
        address chief = msg.sender;

        items[chief].name = _name;
        items[chief].title = _title;
        items[chief].sku_number = _sku_number;
        items[chief].url = _url;
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
        items[_chief].title,
        items[_chief].sku_number,
        items[_chief].url
        );
    }
}
