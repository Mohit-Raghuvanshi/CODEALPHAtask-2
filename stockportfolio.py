import pandas as pd
import yfinance as yf

# Define the portfolio with stock symbols and quantities
portfolio = {
    'AAPL': 10,
    'MSFT': 5,
    'GOOGL': 3,
    'AMZN': 2
}

def fetch_stock_data(symbol):
    try:
        # Fetch historical stock data for the given symbol
        stock = yf.Ticker(symbol)
        stock_data = stock.history(period='1d', start='2020-01-01', end='2024-04-01')['Close']
        return stock_data
    except Exception as e:
        print(f"Error fetching data for {symbol}: {e}")
        return None

# Create an empty DataFrame to store portfolio data
portfolio_data = pd.DataFrame()

# Iterate through each symbol in the portfolio
for symbol, quantity in portfolio.items():
    # Fetch stock data for the symbol
    stock_data = fetch_stock_data(symbol)
    
    # Check if data was successfully fetched
    if stock_data is not None:
        # Calculate the total value of the stock holding and store in DataFrame
        portfolio_data[symbol] = stock_data * quantity

# Calculate total portfolio value, daily return, and print the DataFrame
if not portfolio_data.empty:
    portfolio_data['Total Value'] = portfolio_data.sum(axis=1)
    portfolio_data['Daily Return'] = portfolio_data['Total Value'].pct_change()
    print(portfolio_data)
else:
    print("No data fetched for the portfolio.")
