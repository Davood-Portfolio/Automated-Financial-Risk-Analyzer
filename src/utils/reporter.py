import pandas as pd
from datetime import datetime
import os

class Reporter:
    def __init__(self, output_path="data/reports/"):
        self.output_path = output_path
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

    def generate_csv_report(self, stats_df, forecasts):
        """Combines stats and forecasts into a single CSV report."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{self.output_path}market_report_{timestamp}.csv"
        
        report_data = stats_df.copy()
        # Mapping forecasts to the dataframe
        report_data['Forecast_Next_Price'] = [
            forecasts.get(asset, 0) for asset in report_data.index
        ]
        
        report_data.to_csv(filename)
        return filename