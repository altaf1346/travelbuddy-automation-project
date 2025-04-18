import json
import csv

class DataReader:
    @staticmethod
    def read_json(file_path):
        """Reads data from a JSON file."""
        with open(file_path, 'r') as file:
            return json.load(file)

    @staticmethod
    def read_csv(file_path):
        """Reads data from a CSV file."""
        data = []
        with open(file_path, 'r') as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                data.append(row)
        return data
