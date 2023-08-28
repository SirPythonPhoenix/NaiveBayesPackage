import csv
import json

FILENAME = "enron_spam_data.csv"
FORMATTED_FILENAME = "f_enron_spam_data.json"

with open(FORMATTED_FILENAME, "w") as foverwrite:
    foverwrite.write("")

with open(FILENAME) as f, open(FORMATTED_FILENAME, "a") as fdest:
    csv_reader = csv.reader(f, delimiter=',')
    line_count = 0
    index_errors = 0
    value_errors = 0
    print(f'Column names are {", ".join(next(csv_reader))}')
    while True:
        try:
            e = next(csv_reader)
            try:
                int(e[0])
                if len(e) != 5:
                    continue
                elements = int(e[0])
                e = {
                    "text": e[1] + " " + e[2],
                    "label": str(e[3])
                }
                fdest.write(json.dumps(e) + "\n")
            except ValueError:
                value_errors += 1
            except IndexError:
                index_errors += 1
            line_count += 1
        except csv.Error:
            pass
        except StopIteration:
            break
    print(f'Processed lines: {line_count}\nHighest index: {elements} \nValue Errors: {value_errors} \nIndex Errors: {index_errors}')
