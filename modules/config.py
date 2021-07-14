import json

def load_config_data(config_file_path: str):
    with open(config_file_path, 'r') as config_file:
        return json.load(config_file_path)
