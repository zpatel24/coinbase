import requests

# Base RPC URL
rpc_url = 'https://api.developer.coinbase.com/rpc/v1/base/4Fjo6n_rByO6HxBvIbwoaGveKrd5yoci'
# For production, endpoint url and wallet address should be in a secret management tool or environmentalized
def get_eth_balance():
    # set up payload for request
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "cdp_listBalances",
        "params": [
            {
                "address": "0x5ff137d4b0fdcd49dca30c7cf57e578a026d2789",  # Base wallet address to check
                "pageToken": "",  # No pagination
                "pageSize": 1  # Limit to 1 result
            }
        ]
    }

    # Headers for the request
    headers = {
        "Content-Type": "application/json"
    }

    try:
        # Make the POST request to the endpoint
        response = requests.post(rpc_url, json=payload, headers=headers, timeout=10)
        
        # Check if the request was successful
        if response.status_code == 200:
            
            data = response.json()
            
            # Get reponse
            result = data.get("result", {})
            balances = result.get("balances", [])
            
            if balances:
                # Get the balance information from the first result
                balance_info = balances[0]
                
                # Convert the balance from wei to float
                balance_wei = float(balance_info["value"])
                decimals = balance_info["decimals"]  
                
                # Convert the balance to ETH using the decimals
                balance_eth = balance_wei / (10 ** decimals)
                
               
                return balance_eth
            else:
                
                raise Exception("Unexpected response structure: 'balances' missing or empty")
        else:
            # Raise an error if the request failed
            raise Exception(f"Failed to fetch balance: {response.status_code} - {response.text}")
    
    except requests.exceptions.Timeout:
        # Handle timeout
        raise Exception("Request timed out while trying to fetch balance")

    except Exception as e:
        # Catch any other exceptions and raise them
        raise Exception(f"An error occurred: {e}")
