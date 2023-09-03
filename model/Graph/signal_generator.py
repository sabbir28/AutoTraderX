import pandas as pd

def signal_generator(df):
    """
    Generate trading signals based on candlestick patterns.

    Args:
        df (pandas.DataFrame): A DataFrame containing OHLC (Open, High, Low, Close) price data.

    Returns:
        int: 1 for Bearish Pattern, 2 for Bullish Pattern, 0 for No Clear Pattern.
    """
    open_price = df.Open.iloc[-1]
    close_price = df.Close.iloc[-1]
    previous_open = df.Open.iloc[-2]
    previous_close = df.Close.iloc[-2]

    # Bearish Pattern
    if (
        open_price > close_price
        and previous_open < previous_close
        and close_price < previous_open
        and open_price >= previous_close
    ):
        return 1

    # Bullish Pattern
    elif (
        open_price < close_price
        and previous_open > previous_close
        and close_price > previous_open
        and open_price <= previous_close
    ):
        return 2

    # No clear pattern
    else:
        return 0