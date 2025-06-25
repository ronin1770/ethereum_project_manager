import json
import os
from web3 import Web3
from django.conf import settings

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Use environment variables
ganache_url = os.environ["GANACHE_URL"]
account = os.environ["GANACHE_ACCOUNT"]
private_key = os.environ["GANACHE_PRIVATE_KEY"]
project_contract_address = os.environ["PROJECT_CONTRACT_ADDRESS"]

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider(ganache_url))


# Connect to local Ganache
w3 = Web3(Web3.HTTPProvider(ganache_url))

# Load ABI
abi_path = os.path.join(settings.BASE_DIR,'contracts', 'ProjectContract.json')
with open(abi_path) as f:
    abi = json.load(f)

# Deployed contract address from Remix (Ganache network)
contract_address = Web3.to_checksum_address(project_contract_address)
contract = w3.eth.contract(address=contract_address, abi=abi)

# Main function to push data
def push_project_to_chain(project):
    tx = contract.functions.createProject(
        project.project_name,
        project.customer_id,
        project.project_description,
        int(project.project_start.timestamp()),
        int(project.project_end.timestamp()),
        int(project.project_actual_start.timestamp()),
        int(project.project_actual_end.timestamp()),
        project.completed,
        project.project_manager_id,
        int(project.created_on.timestamp()),
        int(project.updated_at.timestamp())
    ).build_transaction({
        'from': account,
        'nonce': w3.eth.get_transaction_count(account),
        'gas': 300000,
        'gasPrice': w3.to_wei('1', 'gwei')
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)

    print(signed_tx)

    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)



    return w3.to_hex(tx_hash)