import yfinance as yf
import pandas as pd

# Define the tickers
tickers = ["TCEHY", "HAS", "BBWI", "NWL", "NFLX", "^GSPC"]  # ^GSPC represents the S&P 500

# Loop through each ticker
for ticker in tickers:
    # Download historical data for the ticker
    history = yf.download(ticker, start='2000-01-01', end='2025-02-18')  # Adjust dates as needed
    
    # Ensure the index is a DatetimeIndex
    if not isinstance(history.index, pd.DatetimeIndex):
        history.index = pd.to_datetime(history.index)
    
    # Filter the DataFrame to include only Fridays
    fridays_df = history[history.index.dayofweek == 4]  # 4 corresponds to Friday
    
    # Select only the 'Close' column
    fridays_close = fridays_df[['Close']]
    
    # Print the DataFrame to verify
    print(f"Friday closing prices for {ticker}:")
    print(fridays_close)
    
    # Save the filtered DataFrame to a CSV file
    fridays_close.to_csv(f"{ticker}_closings.csv", index=True)
