class RiskManager:
    def __init__(self, volatility_threshold=1.0):
        # If volatility is above this, it's high risk
        self.threshold = volatility_threshold

    def evaluate_risk(self, asset_name, volatility):
        """Classify risk level based on volatility."""
        if volatility > self.threshold:
            return "🔴 HIGH RISK"
        elif volatility > 0.1:
            return "🟡 MODERATE RISK"
        else:
            return "🟢 LOW RISK"