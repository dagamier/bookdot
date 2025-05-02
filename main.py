# main.py

import sys
import os
from stats import count_words, count_chars, sort_char_counts


def get_book_text(filepath):
    """
    Reads the file at the given filepath and returns its contents as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as f:
        return f.read()


def main():
    # Ensure a filepath argument is provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]

    # Validate path
    if not os.path.exists(filepath):
        print(f"Error: File '{filepath}' does not exist.")
        sys.exit(1)
    if not os.path.isfile(filepath):
        print(f"Error: '{filepath}' is not a file.")
        sys.exit(1)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    # Load text
    book_text = get_book_text(filepath)

    # Word count
    num_words = count_words(book_text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")

    # Character counts
    char_counts = count_chars(book_text)
    sorted_chars = sort_char_counts(char_counts)
    print("--------- Character Count -------")
    for entry in sorted_chars:
        print(f"{entry['char']}: {entry['num']}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
