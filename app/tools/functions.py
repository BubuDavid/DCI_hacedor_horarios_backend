import unicodedata

# Normalize text function
def normalize_text(word):
    """
    This function takes a string 'word' and normalized
    Example: hElLó wÓrlD = HELLO WORLD
    """
    word = str(word) # Making sure this is a string
    upper_word = word.upper() # Only upper case letters
    striped_word = upper_word.strip() # No spaces at the beginning or end of the word
    # No accents -> https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize
    normalized_word = ''.join([
        letter for letter in unicodedata.normalize('NFD', striped_word)
        if unicodedata.category(letter) != 'Mn'
    ])

    return normalized_word