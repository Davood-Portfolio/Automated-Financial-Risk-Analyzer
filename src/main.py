import time
from api.data_fetcher import DataFetcher
from database.db_manager import DatabaseManager
from analysis.statistical_analyzer import StatisticalAnalyzer
from analysis.forecaster import PriceForecaster
from utils.risk_manager import RiskManager

def main():
    fetcher = DataFetcher()
    db = DatabaseManager()
    analyzer = StatisticalAnalyzer()
    forecaster = PriceForecaster()
    risk_mgr = RiskManager(volatility_threshold=2.0)

    print("--- Financial Risk Analyzer Pro (AI Mode) ---")
    
    # 1. Fetch & Save Data
    prices_df = fetcher.get_crypto_prices()
    if prices_df is not None:
        for asset, row in prices_df.iterrows():
            db.save_price(asset, row['Price (EUR)'])
    
    # 2. Statistical & Risk Analysis
    print("\n[Risk and Market Report]")
    stats = analyzer.calculate_summary()
    for asset, row in stats.iterrows():
        vol = 0 if str(row['Volatility (Std)']) == 'nan' else row['Volatility (Std)']
        status = risk_mgr.evaluate_risk(asset, vol)
        print(f"Asset: {asset:10} | Volatility: {vol:.2f} | Status: {status}")

    # 3. AI Price Forecasting
    print("\n[AI Price Forecast - Next Move]")
    df_history = analyzer.load_data()
    
    for asset in ['bitcoin', 'ethereum', 'ripple']:
        asset_prices = df_history[df_history['asset_name'] == asset]['price_eur'].tolist()
        prediction = forecaster.predict_next_price(asset_prices)
        
        if prediction:
            current_price = asset_prices[-1]
            trend = "UP" if prediction > current_price else "DOWN"
            change = ((prediction - current_price) / current_price) * 100
            print(f"Asset: {asset:10} | Forecast: {prediction:.2f} EUR | Trend: {trend} ({change:+.4f}%)")
        else:
            print(f"Asset: {asset:10} | Status: Insufficient data for forecast (minimum 5 points required)")

if __name__ == "__main__":
    main()