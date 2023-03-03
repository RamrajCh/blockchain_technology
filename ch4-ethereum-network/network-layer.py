#
# Practice for Network Layer
#
# Prerequisite Note - Get ganach http service URL
#                     Then, update such information below
#                     Next, run the script in your local environment
# Ethereum P2P Network
from web3 import Web3

provider_url = "http://127.0.0.1:8545"
#provider_url = "https://goerli.infura.io/v3/4795546af81740deaac63160553d1544"
# provider_url = "https://mainnet.infura.io/v3/b62d70f9852e41918a44f714dacb5629"
w3 = Web3(Web3.HTTPProvider(provider_url))

# Found Method admin_peers not supported in ganache
# Found available testnet also doesn't support the method.
#ValueError: {'code': -32601, 'message': 'The method admin_peers does not exist/is not available'}
#peers = w3.geth.admin.peers()
#print(peers)

# Network Discovery Protocol
from web3 import Web3
# Found Method admin_nodeInfo not supported in ganache
# Found available testnet also doesn't support the method.
#ValueError: {'code': -32601, 'message': 'The method admin_peers does not exist/is not available'}
#enode = w3.geth.admin.node_info()['enode']
#print(enode)

# Ethereum Database
from web3 import Web3
block_number = 1
block = w3.eth.get_block(block_number)
print(block)

# RLP (Recursive-length prefix) Encoding
# Used to encode a wide variety of data in Ethereum
from rlp import encode
data = [b'\x01', 2, b'hello']
encoded_data = encode(data)
print(encoded_data.hex())

# Sample Output with Ganache output- 
# AttributeDict({'number': 1, 'hash': HexBytes('0x5e3eef454d0680e31a0b7691ae8230c836cf622a4105f5684a06f43c73bfb072'), 'parentHash': HexBytes('0xfd5a659d03baa70c4e507fa4a5ec2941c78a5eecabb74e727aa39e966e35fb0e'), 'mixHash': HexBytes('0x0000000000000000000000000000000000000000000000000000000000000000'), 'nonce': HexBytes('0x0000000000000000'), 'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'), 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'transactionsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'), 'stateRoot': HexBytes('0x4ceb17d898c299216a60821376a751b76e132e51ba0e2c48038b3350a63d9ad4'), 'receiptsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'), 'miner': '0x0000000000000000000000000000000000000000', 'difficulty': 0, 'totalDifficulty': 0, 'extraData': HexBytes('0x'), 'size': 1000, 'gasLimit': 6721975, 'gasUsed': 0, 'timestamp': 1677770484, 'transactions': [], 'uncles': []})
# c801028568656c6c6f
#
# AttributeDict({'difficulty': 17171480576, 'extraData': HexBytes('0x476574682f76312e302e302f6c696e75782f676f312e342e32'), 'gasLimit': 5000, 'gasUsed': 0, 'hash': HexBytes('0x88e96d4537bea4d9c05d12549907b32561d3bf31f45aae734cdc119f13406cb6'), 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'miner': '0x05a56E2D52c817161883f50c441c3228CFe54d9f', 'mixHash': HexBytes('0x969b900de27b6ac6a67742365dd65f55a0526c41fd18e1b16f1a1215c2e66f59'), 'nonce': HexBytes('0x539bd4979fef1ec4'), 'number': 1, 'parentHash': HexBytes('0xd4e56740f876aef8c010b86a40d5f56745a118d0906a34e69aec8c0db1cb8fa3'), 'receiptsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'), 'sha3Uncles': HexBytes('0x1dcc4de8dec75d7aab85b567b6ccd41ad312451b948a7413f0a142fd40d49347'), 'size': 537, 'stateRoot': HexBytes('0xd67e4d450343046425ae4271474353857ab860dbc0a1dde64b41b5cd3a532bf3'), 'timestamp': 1438269988, 'totalDifficulty': 34351349760, 'transactions': [], 'transactionsRoot': HexBytes('0x56e81f171bcc55a6ff8345e692c0f86e5b48e01b996cadc001622fb5e363b421'), 'uncles': []})
# c801028568656c6c6f