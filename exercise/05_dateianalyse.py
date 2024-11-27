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

from collections import Counter


class FileAnalyzer:
    """
    Eine Klasse zur Analyse von Textdateien.

    Examples:
        >>> analyzer = FileAnalyzer()
        >>> analyzer.analyze_file("sample.txt")  # Enthält: "Hello world hello python"
        >>> analyzer.get_unique_words()
        ['hello', 'python', 'world']
        >>> freq = analyzer.get_word_frequency()
        >>> freq['hello']
        2
        >>> similar = analyzer.find_similar_words('python')
        >>> 'python' in similar
        True
    """

    def __init__(self):
        """Initialisiert den FileAnalyzer."""
        self.words = []
        self.word_frequency = Counter()
        self.unique_words = set()

    def analyze_file(self, filename):
        """Liest und analysiert eine Textdatei."""
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.analyze_text(file.read())
        except FileNotFoundError:
            raise FileNotFoundError(f"Die Datei {filename} wurde nicht gefunden.")

    def analyze_text(self, text):
        """Analysiert einen gegebenen Text."""
        # Text in Wörter aufteilen und bereinigen
        words = text.lower().split()
        self.words = [word.strip('.,!?()[]{}":;') for word in words]

        # Worthäufigkeit und eindeutige Wörter aktualisieren
        self.word_frequency = Counter(self.words)
        self.unique_words = set(self.words)

    def get_word_frequency(self):
        """Gibt die Häufigkeit aller Wörter zurück."""
        return dict(self.word_frequency)

    def get_unique_words(self):
        """Gibt eine Menge aller einzigartigen Wörter zurück."""
        return sorted(self.unique_words)

    def export_statistics(self, format="dict"):
        """Exportiert die Statistiken in verschiedenen Formaten."""
        stats = {
            "total_words": len(self.words),
            "unique_words": len(self.unique_words),
            "word_frequency": dict(self.word_frequency),
        }

        if format == "dict":
            return stats
        elif format == "list":
            return [(word, freq) for word, freq in self.word_frequency.items()]
        elif format == "set":
            return self.unique_words
        else:
            raise ValueError("Ungültiges Format. Erlaubt sind: dict, list, set")

    def find_similar_words(self, word):
        """Findet ähnliche Wörter basierend auf gemeinsamen Buchstaben."""
        word_chars = set(word.lower())
        similar_words = set()

        for other_word in self.unique_words:
            other_chars = set(other_word)
            similarity = len(word_chars & other_chars) / len(word_chars | other_chars)
            if similarity >= 0.5:  # Mindestens 50 % Übereinstimmung
                similar_words.add(other_word)

        return similar_words

    def get_top_words(self, n=10):
        """Gibt die häufigsten N Wörter zurück."""
        return dict(self.word_frequency.most_common(n))


if __name__ == "__main__":
    import doctest

    doctest.testmod()
