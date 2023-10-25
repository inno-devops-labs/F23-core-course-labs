// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721Enumerable.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract MarketingToken is ERC721Enumerable, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIdCounter;

    struct Item {
        string title;
        string image;
        bool isForSale;
        uint256 price;
    }

    mapping(uint256 => Item) public items;

    constructor() ERC721("MarketingToken", "MKT") Ownable(msg.sender) {}

    function mintItem(string calldata title, string calldata image) external payable {
        require(msg.value == 0.001 ether, "Price is 0.001 ether");
        require(_tokenIdCounter.current() < 1000, "Only 1000 items can be minted");

        _tokenIdCounter.increment();
        uint256 newItemId = _tokenIdCounter.current();

        items[newItemId] = Item({
            title: title,
            image: image,
            isForSale: false,
            price: 0
        });

        _safeMint(msg.sender, newItemId);
    }

    function modifyItem(uint256 tokenId, string calldata title, string calldata image) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can modify");

        items[tokenId].title = title;
        items[tokenId].image = image;
    }

    function listItemForSale(uint256 tokenId, uint256 price) external {
        require(ownerOf(tokenId) == msg.sender, "Only the owner can list for sale");

        items[tokenId].isForSale = true;
        items[tokenId].price = price;
    }

    function buyItem(uint256 tokenId) external payable {
        require(items[tokenId].isForSale, "Item is not for sale");
        require(msg.value == items[tokenId].price, "Incorrect Ether sent");

        address currentOwner = ownerOf(tokenId);
        
        items[tokenId].isForSale = false;  // Set this first to reduce the risk of re-entrancy attacks
        payable(currentOwner).transfer(msg.value);

        _transfer(currentOwner, msg.sender, tokenId);
    }
}