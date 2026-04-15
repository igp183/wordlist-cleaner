import argparse
import json

INPUT_FILE = "words_dictionary.json"
OUTPUT_FILE = "cleaned_words.json"

MIN_LENGTH = 3
MAX_LENGTH = 99

ALLOW_NUMBERS = False
ALLOW_SPACES = False
ALLOW_HYPHENS = False
ALLOW_CAPITALS = False


def is_valid(
    word, min_len, max_len, allow_nums, allow_spaces, allow_hyphens, allow_capitals
):
    isTooShort = len(word) < min_len
    isTooLong = len(word) > max_len
    hasSpaces = not allow_spaces and " " in word
    hasNumbers = not allow_nums and any(c.isdigit() for c in word)
    hasHyphens = not allow_hyphens and "-" in word
    hasCapitals = not allow_capitals and any(c.isupper() for c in word)

    return not (
        isTooShort or isTooLong or hasSpaces or hasNumbers or hasHyphens or hasCapitals
    )


def main():
    parser = argparse.ArgumentParser(description="Clean a JSON wordlist.")
    parser.add_argument(
        "--input", default=INPUT_FILE, help="Path to the input JSON file"
    )
    parser.add_argument(
        "--output", default=OUTPUT_FILE, help="Path to the output JSON file"
    )
    parser.add_argument(
        "--min-length", type=int, default=MIN_LENGTH, help="Minimum word length"
    )
    parser.add_argument(
        "--max-length", type=int, default=MAX_LENGTH, help="Maximum word length"
    )
    parser.add_argument(
        "--allow-numbers",
        action="store_true",
        default=ALLOW_NUMBERS,
        help="Allow words with numbers",
    )
    parser.add_argument(
        "--allow-spaces",
        action="store_true",
        default=ALLOW_SPACES,
        help="Allow words with spaces",
    )
    parser.add_argument(
        "--allow-hyphens",
        action="store_true",
        default=ALLOW_HYPHENS,
        help="Allow words with hyphens",
    )
    parser.add_argument(
        "--allow-capitals",
        action="store_true",
        default=ALLOW_CAPITALS,
        help="Allow words with uppercase",
    )
    args = parser.parse_args()

    print(f"Loading words from: {args.input}")
    with open(args.input, "r") as file:
        words = json.load(file)

    before = len(words)
    cleaned = {
        word: value
        for word, value in words.items()
        if is_valid(
            word,
            args.min_length,
            args.max_length,
            args.allow_numbers,
            args.allow_spaces,
            args.allow_hyphens,
            args.allow_capitals,
        )
    }
    after = len(cleaned)

    print(f"Words before: {before}")
    print(f"Words after:  {after}")
    print(f"Words removed: {before - after}")

    with open(args.output, "w") as file:
        json.dump(cleaned, file, indent=2)

    print(f"Saved to: {args.output}")


main()
