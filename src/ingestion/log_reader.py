import json

def read_logs(file_path: str):
    with open(file_path, 'r') as file:
        logs = json.load(file)
    return logs