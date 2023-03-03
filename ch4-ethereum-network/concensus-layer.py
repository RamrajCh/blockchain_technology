# #
# # Practice for Consensus Layer - Forking and DAG File
# #
# from web3 import Web3, HTTPProvider

# # Connect to Ganache using HTTP provider
# # Found that ganache doesn't support debug_traceBlockByNumber
# # OPTION - 1 Ganache
# provider_url = "http://127.0.0.1:8545"

# # OPTION - 2 Goerli
# # Found that following infura also doesn't support debug_traceBlockByNumber
# # ValueError: {'code': -32601, 'message': 'The method debug_traceBlockByNumber does not exist/is not available'}
# #provider_url = "https://goerli.infura.io/v3/4795546af81740deaac63160553d1544"
# # provider_url = "https://mainnet.infura.io/v3/b62d70f9852e41918a44f714dacb5629"


# web3 = Web3(HTTPProvider(provider_url))

# # Check connection status
# if web3.isConnected():
#     print("Connected to Network")

# # Get the latest block number
# latest_block = web3.eth.getBlock('latest').number
# print(f"Latest block number: {latest_block}")

# # Create a fork of the blockchain at a specific block number
# fork_block_number = latest_block - 10
# #fork_block_number = 139
# forked_chain = web3.manager.request_blocking("debug_traceBlockByNumber", [fork_block_number, {"disableStorage": True}])

# # Get the DAG file for the forked chain
# dag_file = web3.manager.request_blocking(
#     "debug_dumpDAG", [fork_block_number, True]
# )

# # Print the DAG (Directed Acyclic Graph) file
# print(f"DAG file for block {fork_block_number}: {dag_file}")
