import json

INPUT_FILE = "/home/ivan/Downloads/words_dictionary.json"
OUTPUT_FILE = "cleaned_words.json"

MIN_LENGTH = 3
MAX_LENGTH = 99

ALLOW_NUMBERS = False
ALLOW_SPACES = False
ALLOW_HYPHENS = False
ALLOW_CAPITALS = False


def is_valid(word):
    isTooShort = len(word) < MIN_LENGTH
    isTooLong = len(word) > MAX_LENGTH
    hasSpaces = not ALLOW_SPACES and " " in word
    hasNumbers = not ALLOW_NUMBERS and any(c.isdigit() for c in word)
    hasHyphens = not ALLOW_HYPHENS and "-" in word
    hasCapitals = not ALLOW_CAPITALS and any(c.isupper() for c in word)

    return not (
        isTooShort or isTooLong or hasSpaces or hasNumbers or hasHyphens or hasCapitals
    )


def main():
    print(f"Loading words from: {INPUT_FILE}")
    with open(INPUT_FILE, "r") as file:
        words = json.load(file)

    before = len(words)
    cleaned = {word: value for word, value in words.items() if is_valid(word)}
    after = len(cleaned)

    print(f"Words before: {before}")
    print(f"Words after:  {after}")
    print(f"Words removed: {before - after}")

    with open(OUTPUT_FILE, "w") as file:
        json.dump(cleaned, file, indent=2)

    print(f"Saved to: {OUTPUT_FILE}")


main()
