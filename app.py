import pandas as pd
import plotly.graph_objs as go
from flask import Flask, render_template
from model.set_working_directory import set_working_directory

app = Flask(__name__)

# Function to load stock data from a CSV file into a Pandas DataFrame
def load_stock_data(csv_path):
    df = pd.read_csv(csv_path)
    return df

# Function to create a candlestick chart from stock data
def create_candlestick_chart(df):
    candlestick = go.Candlestick(
        x=df['Date'],
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
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
    return fig

@app.route('/')
def index():
    # Path to the CSV file
    csv_path = 'stock_data/META.csv'

    # Load stock data and create a candlestick chart
    df = load_stock_data(csv_path)
    chart = create_candlestick_chart(df)

    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    # Set the working directory
    set_working_directory('/workspaces/AutoTraderX')
    
    # Run the Flask application
    app.run(debug=True)
