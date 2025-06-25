import os
import json
from web3 import Web3
from dotenv import load_dotenv
from pathlib import Path
from django.conf import settings

# Load environment variables
env_path = Path(__file__).resolve().parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

# Load from .env
ganache_url = os.environ["GANACHE_URL"]
account = os.environ["GANACHE_ACCOUNT"]
private_key = os.environ["GANACHE_PRIVATE_KEY"]
contract_address = Web3.to_checksum_address(os.environ["SPRINT_CONTRACT_ADDRESS"])

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider(ganache_url))
assert w3.is_connected(), "Web3 connection to Ganache failed"

# Load ABI
abi_path = os.path.join(settings.BASE_DIR, 'contracts', 'SprintContract.json')
with open(abi_path) as f:
    abi = json.load(f)

# Load the deployed contract
contract = w3.eth.contract(address=contract_address, abi=abi)

# Function to send Sprint data
def push_sprint_to_chain(sprint):
    tx = contract.functions.createSprint(
        sprint.project_id,
        sprint.customer_id,
        sprint.project_manager_id,
        int(sprint.sprint_start.timestamp()),
        int(sprint.sprint_end.timestamp()),
        sprint.sprint_description,
        sprint.estimated_hours,
        sprint.total_items,
        sprint.total_completed,
        int(sprint.created_on.timestamp()),
        int(sprint.updated_at.timestamp())
    ).build_transaction({
        'from': account,
        'nonce': w3.eth.get_transaction_count(account),
        'gas': 300000,
        'gasPrice': w3.to_wei('1', 'gwei')
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)

    return w3.to_hex(tx_hash)
