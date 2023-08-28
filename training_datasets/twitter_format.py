import csv
import json

FILENAME = "twitter_training.csv"
FORMATTED_FILENAME = "f_twitter_training.json"

with open(FORMATTED_FILENAME, "w") as foverwrite:
    foverwrite.write("")

with open(FILENAME) as f, open(FORMATTED_FILENAME, "a") as fdest:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    index_errors = 0
    value_errors = 0
    while True:
        try:
            e = next(csv_reader)
            e = {
                "text": e[3],
                "label": str(e[2])
            }
            fdest.write(json.dumps(e) + "\n")
            line_count += 1
        except StopIteration:
            break
            line_count += 1
    print(f'Processed lines: {line_count}')
