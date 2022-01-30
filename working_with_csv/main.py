import os
import csv
import json

csv_file_path = f"{os.getcwd()}/working_with_csv/location.csv"
json_file_path = f"{os.getcwd()}/working_with_csv/location.json"


def convert_csv_to_json(csv_path: str, json_path: str):
    with open(csv_path, encoding="utf-8-sig") as csvFile:
        reader = csv.DictReader(csvFile)

        data = []
        for row in reader:
            data.append(row)

        with open(json_path, "w", encoding="utf-8") as jsonfile:
            jsonfile.write(json.dumps(data, indent=2))


convert_csv_to_json(csv_file_path, json_file_path)
