// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract VideoHashStorage {
    mapping(string => string) public videoHashes;

    function storeHash(string memory videoId, string memory hashValue) public {
        videoHashes[videoId] = hashValue;
    }

    function getHash(string memory videoId) public view returns (string memory) {
        return videoHashes[videoId];
    }
}