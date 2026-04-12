import time
from api.data_fetcher import DataFetcher
from database.db_manager import DatabaseManager

def main():
    fetcher = DataFetcher()
    db = DatabaseManager()
    
    print("--- Starting Financial Risk Analyzer ---")
    
    try:
        # Fetch data using our API module
        prices_df = fetcher.get_crypto_prices()
        
        if prices_df is not None:
            print("Data fetched successfully. Saving to database...")
            
            # Iterate through the DataFrame and save to SQL
            for asset, row in prices_df.iterrows():
                price = row['Price (EUR)']
                db.save_price(asset, price)
                print(f"Saved: {asset} at {price} EUR")
                
            print("--- Task Completed Successfully ---")
        else:
            print("Failed to fetch data.")
            
    except Exception as e:
        print(f"An error occurred in main execution: {e}")

if __name__ == "__main__":
    main()