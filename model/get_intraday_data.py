import yfinance as yf
import datetime

# Download 1-minute intraday data for TSLA for the specified date
data = yf.download("TSLA", start='2023-09-01', end='2023-09-02', interval="1m")

# Save the data to a CSV file
data.to_csv("tsla_intraday_data.csv")
