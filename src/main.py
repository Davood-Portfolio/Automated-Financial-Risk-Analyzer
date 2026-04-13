import time
from api.data_fetcher import DataFetcher
from database.db_manager import DatabaseManager
from analysis.statistical_analyzer import StatisticalAnalyzer
from utils.risk_manager import RiskManager

def main():
    fetcher = DataFetcher()
    db = DatabaseManager()
    analyzer = StatisticalAnalyzer()
    risk_mgr = RiskManager(volatility_threshold=2.0) # Set threshold

    print("--- 🚀 Financial Risk Analyzer Pro ---")
    
    # 1. Fetch & Save
    prices_df = fetcher.get_crypto_prices()
    if prices_df is not None:
        for asset, row in prices_df.iterrows():
            db.save_price(asset, row['Price (EUR)'])
    
    # 2. Analyze & Risk Assessment
    print("\n[Risk Assessment Report]")
    stats = analyzer.calculate_summary()
    
    for asset, row in stats.iterrows():
        volatility = row['Volatility (Std)']
        # Check if volatility is NaN (first few records)
        safe_vol = 0 if str(volatility) == 'nan' else volatility
        status = risk_mgr.evaluate_risk(asset, safe_vol)
        print(f"Asset: {asset:10} | Volatility: {safe_vol:.2f} | Status: {status}")

    # 3. Correlation
    print("\n[Market Correlation]")
    corr = analyzer.calculate_correlation()
    print(corr)

if __name__ == "__main__":
    main()