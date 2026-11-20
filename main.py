import requests

URL = "https://api.coingecko.com/api/v3/simple/price"

PARAMS = {
    "ids": "bitcoin,ethereum,solana",
    "vs_currencies": "usd"
}

def get_crypto_prices():
    try:
        response = requests.get(URL, params=PARAMS, timeout=15)
        response.raise_for_status()
        data = response.json()

        print("\n===== DEXSNIPER PRICE MONITOR =====")

        print(f"BTC: ${data['bitcoin']['usd']}")
        print(f"ETH: ${data['ethereum']['usd']}")
        print(f"SOL: ${data['solana']['usd']}")

        print("==================================")

    except requests.RequestException as error:
        print("Error fetching prices:", error)

if __name__ == "__main__":
    get_crypto_prices()
