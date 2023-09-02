import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template
from model.set_working_directory import set_working_directory

app = Flask(__name__)

def load_stock_data(csv_path):
    """
    Load stock data from a CSV file into a Pandas DataFrame.

    :param csv_path: The path to the CSV file.
    :return: A Pandas DataFrame containing the stock data.
    """
    # Load your CSV data into a Pandas DataFrame
    df = pd.read_csv(csv_path)
    return df

def create_candlestick_chart(df):
    """
    Create a candlestick chart from stock data.

    :param df: A Pandas DataFrame containing stock data.
    :return: A Plotly candlestick chart.
    """
    # Extract relevant columns
    date_column = 'Date'
    open_column = 'Open'
    high_column = 'High'
    low_column = 'Low'
    close_column = 'Close'

    # Create a Candlestick chart with green for up days and red for down days
    candlestick = go.Candlestick(
        x=df[date_column],
        open=df[open_column],
        high=df[high_column],
        low=df[low_column],
        close=df[close_column],
        increasing_line=dict(color='green'),
        decreasing_line=dict(color='red'),
    )

    data = [candlestick]
    layout = go.Layout(
        title='Candlestick Chart for Stock Prices',
        xaxis=dict(title='Date'),
        yaxis=dict(title='Price'),
    )

    fig = go.Figure(data=data, layout=layout)
    chart = fig.to_html(full_html=False)
    return chart  # Return the chart HTML

@app.route('/')
def index():
    csv_path = 'stock_data/META.csv'
    df = load_stock_data(csv_path)
    chart = create_candlestick_chart(df)
    print(chart)
    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    set_working_directory('/workspaces/AutoTraderX')
    app.run(debug=True)
