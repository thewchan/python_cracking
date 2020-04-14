"""detect_english.py - Module to determine if string contains English.
Only function that should be called is is_english().
is_english(message, dict_path, word_percentage=20, letter_percentage=85.
message: String of message.
dict_path: Absolute or relative path to dictionary path file. No exception
handling in this module.
word_percentage: Default at 20%. Threshold set for the fraction of words in
message must be in dictionary for it to English.
letter_percentage: Default at 85%. Threshold set for characters in message as
 letters and spaces (not punctuation or numbers).
"""
LETTERS_AND_SPACE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz\t\n '


def load_dictionary(dict_path):
    """Takes dictionary text file and return a dictionary with the words
     as keys.
    """
    with open(dict_path) as dictionary_file:
        english_words = {}

        for word in dictionary_file.read().split('\n'):
            english_words[word.upper()] = None

    return english_words


def remove_non_letters(message):
    """Removes punctuation, non-English alphabets, and symbols from message."""
    letters_only = []

    for symbol in message:

        if symbol in LETTERS_AND_SPACE:
            letters_only.append(symbol)

    return ''.join(letters_only)


def get_english_count(message, path):
    """Load dictionary file by calling load_dictionary(), returns ratio between
    number of matched words and words in message.
    """
    english_words = load_dictionary(path)
    matches = 0
    message = message.upper()
    message = remove_non_letters(message)
    possible_words = message.split()

    if possible_words == []:
        return 0.0

    for word in possible_words:

        if word in english_words:
            matches += 1

    return float(matches) / len(possible_words)


def is_english(message, dict_path, word_percentage=20, letter_percentage=85):
    """Calls get_english_count() and returns two boolean values if the
     percentage of words-matched and letters-matched is equal or greater than
     the default or user-set thresholds.
    """
    words_match = (
        get_english_count(message, dict_path) * 100 >= word_percentage
        )
    num_letters = len(remove_non_letters(message))
    message_letters_percentage = float(num_letters / len(message) * 100)
    letters_match = message_letters_percentage >= letter_percentage

    return words_match and letters_match
