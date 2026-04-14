import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

class PriceForecaster:
    def __init__(self):
        self.model = LinearRegression()

    def predict_next_price(self, prices):
        """Predicts the next price point using Linear Regression."""
        if len(prices) < 5:
            return None
        
        # Prepare data (Time steps as X, Prices as y)
        X = np.array(range(len(prices))).reshape(-1, 1)
        y = np.array(prices)
        
        # Train the model
        self.model.fit(X, y)
        
        # Predict the next point in the series
        next_index = np.array([[len(prices)]])
        prediction = self.model.predict(next_index)
        
        return prediction[0]