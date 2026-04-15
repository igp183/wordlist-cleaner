import argparse
import json
import sqlite3

INPUT_FILE = "words_dictionary.json"
OUTPUT_FILE = "words.db"


def main():
    parser = argparse.ArgumentParser(description="Convert a JSON wordlist to SQLite.")
    parser.add_argument("--input", default=INPUT_FILE, help="Path to the input JSON file")
    parser.add_argument("--output", default=OUTPUT_FILE, help="Path to the output SQLite file")
    args = parser.parse_args()

    print(f"Loading words from: {args.input}")
    with open(args.input, "r") as f:
        words = json.load(f)

    con = sqlite3.connect(args.output)
    con.execute("CREATE TABLE IF NOT EXISTS words (word TEXT PRIMARY KEY)")
    con.executemany("INSERT OR IGNORE INTO words VALUES (?)", [(w,) for w in words])
    con.commit()
    con.close()

    print(f"Inserted {len(words)} words into: {args.output}")


main()
