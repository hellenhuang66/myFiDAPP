
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract control{

    uint a=1;
    function assign_a(uint num) public{
        a = num;
    }

  
    function get() public view returns (string memory){
        if (a==1)
            return ("a is 1");
        else 
            return ("a is not 1");
    }

}