# Simple Wordlist Cleaner

This simple cleaner was made for the development of [Matriwordska.com](https://Matriwordska.com) and with [words_dictionary.json](https://github.com/dwyl/english-words/blob/master/words_dictionary.json) in mind.

## Usage

```bash
python clean_wordlist.py
```

## Arguments

You can customize the behavior with command-line arguments:

| Argument | Type | Default | Description |
|----------|------|---------|-------------|
| `--input` | text | `words_dictionary.json` | Path to the input JSON file |
| `--output` | text | `cleaned_words.json` | Path to the output JSON file |
| `--min-length` | number | `3` | Minimum word length |
| `--max-length` | number | `99` | Maximum word length |
| `--allow-numbers` | flag | disabled | Allow words with digits |
| `--allow-spaces` | flag | disabled | Allow words with spaces |
| `--allow-hyphens` | flag | disabled | Allow words with hyphens |
| `--allow-capitals` | flag | disabled | Allow words with uppercase letters |

## Examples

```bash
# Basic usage with defaults
python clean_wordlist.py

# Custom input and output files
python clean_wordlist.py --input my_words.json --output result.json

# Only words between 4 and 8 characters
python clean_wordlist.py --min-length 4 --max-length 8

# Allow numbers and hyphens
python clean_wordlist.py --allow-numbers --allow-hyphens

# Combine multiple options
python clean_wordlist.py --input words.json --min-length 5 --max-length 12 --allow-capitals
```

For all available options, run:
```bash
python clean_wordlist.py --help
```