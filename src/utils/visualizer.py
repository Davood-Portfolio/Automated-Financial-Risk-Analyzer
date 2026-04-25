import matplotlib.pyplot as plt
import os

class Visualizer:
    def __init__(self, output_path="data/plots/"):
        self.output_path = output_path
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def plot_price_forecast(self, asset_name, historical_prices, forecast_value):
        """Creates a chart showing historical prices and the AI forecast."""
        plt.figure(figsize=(10, 6))
        
        # Plot historical data
        plt.plot(historical_prices, label='Historical Price', color='blue', marker='o')
        
        # Plot forecast point
        next_index = len(historical_prices)
        plt.scatter(next_index, forecast_value, color='red', label='AI Forecast', zorder=5)
        
        # Draw a line connecting the last price to the forecast
        plt.plot([next_index - 1, next_index], [historical_prices[-1], forecast_value], 
                 color='red', linestyle='--')

        plt.title(f"Price Analysis & Forecast: {asset_name.upper()}")
        plt.xlabel("Time Points")
        plt.ylabel("Price (EUR)")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)
        
        # Save the plot
        file_path = f"{self.output_path}{asset_name}_forecast.png"
        plt.savefig(file_path)
        plt.close()
        return file_path