import json
import os.path


class JsonStorage:
    def __init__(self, file: str, initial_value=None):
        if initial_value is None:
            initial_value = []

        file_path = f'storage/{file}.json'

        self.file = file_path
        file_exist = os.path.isfile(file_path)
        if not file_exist:
            with open(self.file, 'w') as f:
                json.dump(initial_value, f)

    def read(self):
        try:
            with open(self.file) as f:
                data = json.load(f)
            return data
        except FileNotFoundError:
            print(f"'{self.file}' file Not found")

    def write(self, content):
        with open(self.file, 'w') as f:
            json.dump(content, f)
