# stats.py

def count_words(text):
    """
    Returns the number of words in the given text.
    """
    return len(text.split())


def count_chars(text):
    """
    Returns a dictionary mapping each lowercase character in `text` to its count,
    including symbols and spaces.
    """
    counts = {}
    for char in text.lower():
        counts[char] = counts.get(char, 0) + 1
    return counts


def sort_char_counts(char_counts):
    """
    Takes a dict of character counts and returns a list of dicts sorted descending by count.
    Each dict has keys 'char' and 'num'. Only alphabetical characters are included.
    """
    items = [
        {"char": char, "num": count}
        for char, count in char_counts.items()
        if char.isalpha()
    ]
    items.sort(key=lambda x: x['num'], reverse=True)
    return items
