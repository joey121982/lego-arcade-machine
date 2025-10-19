import json
import os
import time
from typing import Tuple, List, Dict, Any

HIGHSCORE_PATH = "./assets/highscores.json"
TOP_SIZE = 3

def load_highscores(path: str = HIGHSCORE_PATH):
    if not os.path.exists(path):
        return {}
    try:
        with open(path, "r") as f:
            data = json.load(f)
            # normalize format
            for key, value in list(data.items()):
                if not isinstance(value, list):
                    data[key] = []
            return data
    except Exception:
        return {}

def save_highscores(data, path: str = HIGHSCORE_PATH):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as file:
        json.dump(data, file, indent=2)

def get_highscores(game_name, path: str = HIGHSCORE_PATH):
    data = load_highscores(path)
    return data.get(game_name, [])

def update_highscore(game_name, score, name: str | None = None, path: str = HIGHSCORE_PATH):

    try:
        score = int(score)
    except Exception:
        return False, False

    data = load_highscores(path)
    entries = data.get(game_name, [])

    # ensure all entries are dicts with 'score' and 'name'
    entries = [e for e in entries if isinstance(e, dict) and "score" in e]
    entries = sorted(entries, key=lambda e: int(e["score"]), reverse=True)

    qualifies = len(entries) < TOP_SIZE or score > int(entries[-1]["score"])

    if not qualifies:
        return False, False

    if name is None:
        return False, True

    new_entry = {"score": int(score), "name": name, "ts": int(time.time())}
    entries.append(new_entry)
    entries = sorted(entries, key=lambda e: int(e["score"]), reverse=True)[:TOP_SIZE]
    data[game_name] = entries
    save_highscores(data, path)
    return True, False