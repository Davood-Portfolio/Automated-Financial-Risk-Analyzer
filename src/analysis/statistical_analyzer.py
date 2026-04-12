import sqlite3
import pandas as pd

class StatisticalAnalyzer:
    def __init__(self, db_path="data/financial_data.db"):
        self.db_path = db_path

    def load_data(self):
        """Load historical prices from database into a Pandas DataFrame."""
        query = "SELECT asset_name, price_eur, timestamp FROM asset_prices"
        with sqlite3.connect(self.db_path) as conn:
            df = pd.read_sql_query(query, conn)
        return df

    def calculate_summary(self):
        """Calculate basic statistics for each asset."""
        df = self.load_data()
        if df.empty:
            return "No data available."
        
        # Group by asset and calculate mean and count
        summary = df.groupby('asset_name')['price_eur'].agg(['mean', 'count', 'std'])
        summary.columns = ['Average Price', 'Record Count', 'Volatility (Std)']
        return summary

if __name__ == "__main__":
    analyzer = StatisticalAnalyzer()
    print("--- Financial Statistics Summary ---")
    print(analyzer.calculate_summary())