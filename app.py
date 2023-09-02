import plotly.graph_objs as go
from flask import Flask, render_template

app = Flask(__name__)

# Sample data for visualization
x_values = [1, 2, 3, 4, 5]
y_values = [10, 15, 13, 17, 8]

# Function to create the line chart
def create_line_chart():
    trace = go.Scatter(x=x_values, y=y_values, mode='lines+markers')
    data = [trace]
    layout = go.Layout(title='Sample Line Chart', xaxis=dict(title='X-axis'), yaxis=dict(title='Y-axis'))
    fig = go.Figure(data=data, layout=layout)
    return fig.to_html(full_html=False)

@app.route('/')
def index():
    # Generate the line chart and pass it to the HTML template
    chart = create_line_chart()
    return render_template('index.html', chart=chart)

if __name__ == '__main__':
    app.run(debug=True)
