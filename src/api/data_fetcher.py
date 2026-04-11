import requests
import pandas as pd

class DataFetcher:
    """Class to fetch financial data from public APIs."""
    
    def __init__(self):
        self.base_url = "https://api.coingecko.com/api/v3"

    def get_crypto_prices(self, coin_ids=["bitcoin", "ethereum", "ripple"]):
        """Fetches current prices for a list of cryptocurrencies in EUR."""
        params = {
            'ids': ','.join(coin_ids),
            'vs_currencies': 'eur'
        }
        try:
            response = requests.get(f"{self.base_url}/simple/price", params=params)
            response.raise_for_status()
            data = response.json()
            
            # Convert JSON response to a structured DataFrame
            df = pd.DataFrame(data).T
            df.columns = ['Price (EUR)']
            df.index.name = 'Asset'
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

if __name__ == "__main__":
    fetcher = DataFetcher()
    prices = fetcher.get_crypto_prices()
    if prices is not None:
        print("--- Current Market Prices ---")
        print(prices)