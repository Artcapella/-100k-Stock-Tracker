import yfinance as yf
import pandas as pd
from datetime import datetime

# Define the tickers
tickers = ["TCEHY", "HAS", "BBWI", "NWL", "NFLX", "^GSPC"]  # ^GSPC represents the S&P 500

# Loop through each ticker
for ticker in tickers:
    # Initialize the ticker
    stock = yf.Ticker(ticker)
    
    # Retrieve historical data for the last 1 month
    history = stock.history(period='1mo')
    
    # Filter the DataFrame to only include Fridays
    fridays_df = history[history.index.weekday == 4]
    
    # Keep only the last 5 Fridays
    fridays_df = fridays_df.tail(5)
    
    # Print the DataFrame to verify
    print(f"Data for {ticker} (Last 5 Fridays):")
    print(fridays_df)
    
    # Save the filtered DataFrame to a CSV file
    fridays_df.to_csv(f"{ticker}_fridays.csv", index=True)
