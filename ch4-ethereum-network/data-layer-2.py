#
# Data Layer Practice
#
# Prerequisite Note - Get ganach http service URL
#                     Then, update such information below
#                     Next, run the script in your local environment
#
#
# consensus layer is simulated here by creating a new block and adding it 
# to the blockchain using proof-of-work (PoW) algorithm. The PoW algorithm 
# requires that a miner solves a complex mathematical puzzle to add a new block 
# to the blockchain. The first miner to solve the puzzle is rewarded with a certain amount of Ether.
#
# Import required libraries
import time
from web3 import Web3

# Connect to the local blockchain
ganache_url = "http://127.0.0.1:8545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# Set default account to use for transactions
web3.eth.default_account = web3.eth.accounts[0]

# Get the current block number
block_number = web3.eth.blockNumber
print(f"Current block number: {block_number}")

# Get the balance of the default account
balance = web3.eth.getBalance(web3.eth.default_account)
print(f"Account balance: {balance}")

# Get the current gas price
gas_price = web3.eth.gasPrice
print(f"Current gas price: {gas_price}")

# Start mining
web3.geth.miner.start(1)

# Wait for 5 seconds
# Optional - Can increase the sleep time little longer (eg. 60) 
#             and initiate transaction (eg. Data Layer Practice code) by separate terminal
#             
time.sleep(3)

# Stop mining
web3.geth.miner.stop()

# Get the current block number after mining
block_number = web3.eth.blockNumber
print(f"Block number after mining: {block_number}")

# Get the balance of the default account after mining
balance = web3.eth.getBalance(web3.eth.default_account)
print(f"Account balance after mining: {balance}")

#
# Sample Results:
# Current block number: 325
# Account balance: 99971274000000000000
# Current gas price: 20000000000
# Block number after mining: 354
# Account balance after mining: 99970221750000000000