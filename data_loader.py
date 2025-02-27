import yfinance as yf
import pandas as pd

def fetch_stock_data(ticker, start="2000-01-01", end="2024-12-31", interval="1d"):
    """
    Fetch historical stock data from Yahoo Finance.

    Args:
        ticker (str): Stock ticker symbol (e.g., "AAPL").
        start (str): Start date in "YYYY-MM-DD" format.
        end (str): End date in "YYYY-MM-DD" format.
        interval (str): Data interval ("1d", "1wk", "1mo").

    Returns:
        pd.DataFrame: Cleaned stock data.
    """
    try:
        stock = yf.download(ticker, start=start, end=end, interval=interval)
        stock.dropna(inplace=True)  # Remove missing values
        stock.reset_index(inplace=True)  # Ensure 'Date' is a column
        return stock
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return None

if __name__ == "__main__":
    df = fetch_stock_data("AMZN", start = "2025-2-1", end="2025-2-27")
    print(df.tail())  # Preview data