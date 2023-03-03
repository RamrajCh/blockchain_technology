#
# Data Layer Practice
#
# Prerequisite Note - Get ganache two addresses for sender and receiver address
#                     get private key for the sender, and ganach http service URL
#                     Then, update such information below
#                     Next, run the script in your local environment
#
#
# data layer refers to the layer of the Ethereum network responsible 
# for managing account generation, transactions, the creation of the genesis block, 
# uncle blocks, the Ethereum world state, gas fees, and ether units.
#
from web3 import Web3

# define the sender and receiver addresses
sender_address = '0x7Aa2660e0BcBd80D767f046904DabE92635d78CB'
receiver_address = '0x391B71369588D461DE46D4b22CbE127f8F8cadB4'

# connect to the Ethereum network
# Get
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))


# set the sender's private key
private_key = '722a5bd0354efe5e8189db400adb7462f684c56ac3fc37b4253ba909f56b9ec8'

# create the transaction object
transaction = {
    'to': receiver_address,
    'value': w3.toWei(20, 'ether'),
    'gas': 2000000,
    'gasPrice': w3.toWei('50', 'gwei'),
    'nonce': w3.eth.getTransactionCount(sender_address)
}

# sign the transaction
signed_transaction = w3.eth.account.signTransaction(transaction, private_key)

# send the transaction
tx_hash = w3.eth.sendRawTransaction(signed_transaction.rawTransaction)

# get the transaction receipt
tx_receipt = w3.eth.waitForTransactionReceipt(tx_hash)

# print the transaction receipt
print(tx_receipt)

#
# See blockID and also explore the transaction details from the ganache block explorer application
#
# Sample Results:
# AttributeDict({'transactionHash': HexBytes('0x56ae5b36673549746929d36d55d36f489f5907ef4a06481fa66d186973175f78'), 'transactionIndex': 0, 'blockHash': HexBytes('0x251b907aef1ed73b6d2f478a3e2604b53a43395c8cecfd15f51f4f4e8ebefc9c'), 'blockNumber': 129, 'from': '0xb0D5ADf8Fa9574aD490464b57F8C4Dc3516c1eeA', 'to': '0xc57B98a147ab0e38C82B5f0Ef972824ee0894f68', 'gasUsed': 21045, 'cumulativeGasUsed': 21045, 'contractAddress': None, 'logs': [], 'status': 0, 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000')})