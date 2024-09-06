from flask import Flask, request, jsonify
from web3 import Web3

app = Flask(__name__)

# 设置你的以太坊节点的HTTP地址
web3 = Web3(Web3.HTTPProvider('https://mainnet.infura.io/v3/YOUR_INFURA_PROJECT_ID'))

# 合约地址和ABI
contract_address = 'YOUR_CONTRACT_ADDRESS'
contract_abi = [...]  # 你的ERC20合约ABI
contract = web3.eth.contract(address=contract_address, abi=contract_abi)

@app.route('/transfer', methods=['POST'])
def transfer_tokens():
    sender_address = request.json['sender']
    private_key = request.json['private_key']
    recipient_address = request.json['recipient']
    amount = request.json['amount']

    nonce = web3.eth.getTransactionCount(sender_address)
    tx = contract.functions.transfer(recipient_address, web3.toWei(amount, 'ether')).buildTransaction({
        'chainId': 1,
        'gas': 2000000,
        'gasPrice': web3.toWei('50', 'gwei'),
        'nonce': nonce,
    })

    signed_tx = web3.eth.account.signTransaction(tx, private_key)
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return jsonify({'tx_hash': tx_hash.hex()})

if __name__ == '__main__':
    app.run(debug=True)
