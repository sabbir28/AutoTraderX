import yfinance as yf
import pandas as pd

dataF = yf.download("EURUSD=X", start="2022-10-7", end="2022-12-5", interval='15m')
dataF.iloc[:,:]
#dataF.Open.iloc