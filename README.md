Automated Financial Risk Analyzer (AFRA)
Overview
The Automated Financial Risk Analyzer is a modular Python-based system designed to track, analyze, and forecast financial asset data. It integrates real-time data acquisition from cryptocurrency markets with statistical analysis and machine learning to provide actionable insights into market volatility and future price trends.

Core Capabilities
1. Real-Time Data Acquisition
The system utilizes a dedicated API module to fetch live price data for major assets (Bitcoin, Ethereum, and Ripple) in EUR. This ensures the analysis is always based on the most recent market conditions.

2. Historical Data Management
Leveraging an SQLite database, the application maintains a persistent record of all fetched prices. This historical depth allows for more accurate statistical calculations and serves as the training set for the predictive model.

3. Statistical Risk Assessment
The analyzer computes market volatility using Standard Deviation and Mean Price metrics. Based on predefined thresholds, it categorizes each asset's risk level as either "Low Risk" or "High Risk," enabling informed decision-making.

4. AI-Driven Forecasting
The project incorporates a Machine Learning layer using Scikit-learn. By applying a Linear Regression model to historical price sequences, the system predicts the next likely price point and identifies the expected market trend (UP/DOWN).

5. Automated Professional Reporting
CSV Reports: Generates comprehensive data sheets including statistical summaries and AI forecasts with timestamps.

Visual Analytics: Produces graphical charts (PNG) using Matplotlib, mapping historical price movements against the AI-predicted trajectory for visual verification.

Technical Architecture
The project follows a clean, modular directory structure:

src/api/: Handles external communications and data ingestion.

src/database/: Manages SQLite connections and CRUD operations.

src/analysis/: Contains the statistical logic and the Machine Learning forecaster.

src/utils/: Includes the reporting engine and the visualization module.

data/: Dedicated storage for the SQLite database, generated CSV reports, and visual plots.

Tech Stack
Language: Python 3.x

Libraries: Pandas, NumPy, Scikit-learn, Matplotlib

Database: SQLite3

Environment: Python Virtual Environment (venv)

Version Control: Git

How to Run
Ensure the virtual environment is activated.

Install dependencies: pip install -r requirements.txt.

Execute the main application: python src/main.py.

View results in the console and check the data/reports/ and data/plots/ directories for exported files.