
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract show_loop{
    uint a = 5;
    uint b = 0;

    function assign_a(uint num) public{
        a = num;
    }
    
    function do_loop() public {
        while (a >= 1){
            a = a-1;
            b = b+a;
        }
    }

    function get_b() public view returns (uint){
        return (b);
    }

}
    