import requests
import os
from requests.auth import HTTPBasicAuth

BITCOIN_RPC_URL = os.getenv("BITCOIN_RPC_URL", "http://127.0.0.1:18332")
BITCOIN_RPC_USER = os.getenv("BITCOIN_RPC_USER", "bitcoinrpc")
BITCOIN_RPC_PASSWORD = os.getenv("BITCOIN_RPC_PASSWORD", "LemetrodomeMakepe1988")

def get_bitcoin_blockchain_info():
    headers = {'content-type': 'application/json'}
    payload = {
        "method": "getblockchaininfo",
        "params": [],
        "jsonrpc": "2.0",
        "id": 0,
    }
    response = requests.post(
        BITCOIN_RPC_URL,
        json=payload,
        headers=headers,
        auth=HTTPBasicAuth(BITCOIN_RPC_USER, BITCOIN_RPC_PASSWORD),
    )
    response.raise_for_status()
    return response.json()['result']
