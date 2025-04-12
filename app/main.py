import requests
import time
import json

API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def get_btc_price(url):
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Request failed. status: {response.status_code}")
    
    data = response.json()
    return data['bitcoin']['usd']



def main():
    while True:
        print(f'BTC: {get_btc_price(API_URL)}')
        time.sleep(12)
        

if __name__ == '__main__':
    main()