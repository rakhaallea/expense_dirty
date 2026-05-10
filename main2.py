import csv

def read_csv(file_path):
    rows = []

    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)

        for row in reader:
            rows.append(row)

    return rows
