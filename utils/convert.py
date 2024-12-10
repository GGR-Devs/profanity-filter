import csv
import os


def from_source_to_csv(input_path: str, output_path: str):
    filename = os.path.splitext(os.path.basename(input_path).upper())[0]
    language = filename

    with open(input_path, 'r', encoding='utf-8') as input_file:
        lines = input_file.read().splitlines()

        stripped = [line.strip() for line in lines if line.strip()]

        rows = [(index, language, word) for index, word in enumerate(stripped)]

        file_exists = os.path.exists(output_path)
        with open(output_path, 'a', newline='', encoding='utf-8') as out_file:
            writer = csv.writer(out_file)
            if not file_exists:
                writer.writerow(('index', 'language', 'word'))
            writer.writerows(rows)
