import json
from datetime import datetime

FILE = "data/history.json"

def save_result(filename, count):
    try:
        with open(FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "date": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "file": filename,
        "tv_count": count
    })

    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)
