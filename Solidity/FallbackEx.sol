//SPDX-License-Identifier: MIT

pragma solidity 0.8.3;

contract FunctionsExample {
    mapping(address => uint) public balanceReceived;

    address payable public owner;

    constructor() {
        owner = payable(msg.sender);
    }

    function destroyContract() public {
        require(msg.sender == owner,"qqq");
        selfdestruct(owner);
    }

    function recieveMoney() public payable {
        assert(balanceReceived[msg.sender] + msg.value >= balanceReceived[msg.sender]);

        balanceReceived[msg.sender] += msg.value;
    }

    function withdrawMoney(address payable _to, uint _amount) public {
        require(_amount <= balanceReceived[msg.sender],"dd");
        assert(balanceReceived[msg.sender] >= balanceReceived[msg.sender] - _amount);

        balanceReceived[msg.sender] -= _amount;
        _to.transfer(_amount);
    }

    receive () external payable {
        recieveMoney();
    }
}