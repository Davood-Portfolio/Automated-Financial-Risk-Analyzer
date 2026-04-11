import sqlite3
import os

class DatabaseManager:
    def __init__(self, db_path="data/financial_data.db"):
        self.db_path = db_path
        self._create_table()

    def _create_table(self):
        """Creates the prices table if it doesn't exist."""
        query = """
        CREATE TABLE IF NOT EXISTS asset_prices (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT NOT NULL,
            price_eur REAL NOT NULL,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        );
        """
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(query)

    def save_price(self, asset_name, price):
        """Inserts a new price record into the database."""
        query = "INSERT INTO asset_prices (asset_name, price_eur) VALUES (?, ?)"
        with sqlite3.connect(self.db_path) as conn:
            conn.execute(query, (asset_name, price))

if __name__ == "__main__":
    db = DatabaseManager()
    print(f"Database initialized at {db.db_path}")