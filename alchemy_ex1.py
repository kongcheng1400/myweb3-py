# Setup
from web3 import Web3

alchemy_url = "https://eth-goerli.g.alchemy.com/v2/KAPI7KZcfx_Xv1Q9rXrvP1pwFY3WI0VJ"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(w3.is_connected())
# Get the latest block number
latest_block = w3.eth.block_number
print(latest_block)

latest_block = w3.eth.get_block('latest')
print(latest_block)

# Get the balance of an account
balance = w3.eth.get_balance('0x742d35Cc6634C0532925a3b844Bc454e4438f44e')
print(balance)

# Get the information of a transaction
tx = w3.eth.get_transaction('0x65afa993c3f2f650cedea38cfafad82110c4d90f0bbb8f21401d0701ec413696')
print(tx)