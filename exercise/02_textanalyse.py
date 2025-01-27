#  Released under MIT License
#
#  Copyright (©) 2024. Talent Factory GmbH
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights to
#  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to
#  do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.


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

    import re
    from collections import Counter

    # Entferne Sonderzeichen und Zahlen, behalte nur Buchstaben und Leerzeichen
    cleaned_text = re.sub(r"[^A-Za-z\s]", "", text)
    words = cleaned_text.split()

    # Berechnung der Anzahl der Wörter
    word_count = len(words)

    # Finde das längste Wort
    longest_word = max(words, key=len) if words else ""

    # Berechne die durchschnittliche Wortlänge
    total_word_length = sum(len(word) for word in words)
    avg_word_length = total_word_length / word_count if word_count > 0 else 0

    # Berechne die Häufigkeit der Buchstaben
    cleaned_text_lower = cleaned_text.lower().replace(" ", "")

    var = Counter(cleaned_text_lower)
    letter_frequency = dict(Counter(cleaned_text_lower))

    # Ergebnisse zurückgeben
    return {
        "word_count": word_count,
        "longest_word": longest_word,
        "avg_word_length": avg_word_length,
        "letter_frequency": letter_frequency,
    }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
