import requests
import itertools

# Chaves de API da Alchemy
API_KEYS = [
    "ILu7oFU_6lE-oiyvIw03Dv4EmOyGfvuM",
    "1suVtuzYsk5fWli_SGwT3cIyTf8SpB5z",
    "UnIDZzpAi9RpxoiPi32ICsl0bvQECtxT"
]

# Cria um iterador cíclico para as chaves de API
api_key_iterator = itertools.cycle(API_KEYS)

def get_alchemy_url():
    api_key = next(api_key_iterator)
    return f"https://eth-mainnet.g.alchemy.com/v2/{api_key}"

def get_eth_balance(address: str) -> str:
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "params": [address, "latest"],
        "method": "eth_getBalance"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    
    response = requests.post(get_alchemy_url(), json=payload, headers=headers)
    if response.status_code == 200:
        balance_wei = int(response.json().get("result", "0"), 16)  # Convertendo de hexadecimal para decimal
        return balance_wei / 10**18  # Convertendo de Wei para ETH
    else:
        return 0.0

def get_token_balance(address: str, token_contract: str) -> float:
    payload = {
        "id": 1,
        "jsonrpc": "2.0",
        "params": [
            {
                "to": token_contract,
                "data": f"0x70a08231000000000000000000000000{address[2:]}"  # ERC20 balanceOf(address)
            },
            "latest"
        ],
        "method": "eth_call"
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json"
    }
    
    response = requests.post(get_alchemy_url(), json=payload, headers=headers)
    if response.status_code == 200:
        balance_wei = int(response.json().get("result", "0"), 16)  # Convertendo de hexadecimal para decimal
        return balance_wei / 10**18  # Convertendo de Wei para a unidade do token
    else:
        return 0.0

def get_balances(address: str) -> dict:
    eth_balance = get_eth_balance(address)
    usdt_contract = "0xdac17f958d2ee523a2206206994597c13d831ec7"  # Endereço do contrato USDT
    usdc_contract = "0xa0b86991c6218b36c1d19d4a2e9eb0ce3606eb48"  # Endereço do contrato USDC
    
    usdt_balance = get_token_balance(address, usdt_contract)
    usdc_balance = get_token_balance(address, usdc_contract)
    
    return {
        "ETH Balance": eth_balance,
        "USDT Balance": usdt_balance,
        "USDC Balance": usdc_balance
    }