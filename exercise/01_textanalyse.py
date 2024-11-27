def analyze_text(text):
    """
    Analysiert einen Text und gibt verschiedene Statistiken zurück.

    Args:
        text (str): Der zu analysierende Text

    Returns:
        dict: Dictionary mit verschiedenen Textstatistiken

    Examples:
        >>> result = analyze_text("Hello World! Python is amazing.")
        >>> result['word_count']
        5
        >>> result['longest_word']
        'amazing'
        >>> result['avg_word_length']
        5.0
        >>> sorted(result['letter_frequency'].items())[:3]
        [('a', 2), ('d', 1), ('e', 1)]
    """
    # Text bereinigen und in Wörter aufteilen
    words = text.lower().replace("!", "").replace(".", "").split()

    # Wörter zählen
    word_count = len(words)

    # Längstes Wort finden
    longest_word = max(words, key=len)

    # Durchschnittliche Wortlänge berechnen
    avg_word_length = sum(len(word) for word in words) / word_count

    # Buchstabenhäufigkeit ermitteln
    letter_frequency = {}
    for word in words:
        for char in word:
            if char.isalpha():
                letter_frequency[char] = letter_frequency.get(char, 0) + 1

    return {
        "word_count": word_count,
        "longest_word": longest_word,
        "avg_word_length": avg_word_length,
        "letter_frequency": letter_frequency,
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
