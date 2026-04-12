import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def plot_prices():
    # 1. Load data
    conn = sqlite3.connect("data/financial_data.db")
    df = pd.read_sql_query("SELECT asset_name, price_eur, timestamp FROM asset_prices", conn)
    conn.close()

    if df.empty:
        print("No data to plot.")
        return

    # 2. Setup Plot
    plt.figure(figsize=(10, 6))
    
    # 3. Plot each asset
    for asset in df['asset_name'].unique():
        asset_data = df[df['asset_name'] == asset]
        plt.plot(asset_data['timestamp'], asset_data['price_eur'], marker='o', label=asset)

    plt.title("Financial Asset Price Trends")
    plt.xlabel("Time")
    plt.ylabel("Price (EUR)")
    plt.legend()
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # 4. Show the plot
    print("Displaying chart...")
    plt.show()

if __name__ == "__main__":
    plot_prices()