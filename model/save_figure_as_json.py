import json

def save_figure_as_json(figure_data, json_file_path):
    """
    Save a Plotly Figure object as a JSON file.

    :param figure_data: The Plotly Figure object to be saved.
    :param json_file_path: The path where the JSON file will be saved.
    """
    with open(json_file_path, 'w') as json_file:
        json.dump(figure_data, json_file)
        print(f'Plotly Figure data saved as JSON in {json_file_path}')
