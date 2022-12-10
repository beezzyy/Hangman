def get_words():
    with open('words.txt') as f:
        words = f.read().splitlines()
    return words
