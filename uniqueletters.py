def  unique_english_letters(word):
    """
    Finds the number of unique letters in a word.
    """
    unique_letters = set()
    for letter in word:
        unique_letters.add(letter)
    return len(unique_letters)

