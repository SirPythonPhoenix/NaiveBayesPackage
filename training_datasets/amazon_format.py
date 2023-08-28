import json

FILENAME = "Amazon_Digital_Music.json"

counter = 0
with open(f"f_{FILENAME}", "w") as foverwrite:
    pass

with open(FILENAME, "r") as fsource, open(f"f_{FILENAME}", "a") as fdest:
    line = fsource.readline()
    while len(line) != 0:
        line_loaded = json.loads(line)
        try:
            line_loaded = {
                "text": line_loaded['reviewText'],
                "label": str(int(line_loaded["overall"]))
            }
            fdest.write(json.dumps(line_loaded) + "\n")
            counter += 1
            print(f"\rLoading & dumping lines: {counter}", end="")
        except KeyError:
            pass
        finally:
            line = fsource.readline()
print("\nFinished writing file.")

