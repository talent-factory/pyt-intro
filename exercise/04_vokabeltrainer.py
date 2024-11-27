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

import random


class VocabularyTrainer:
    """
    Eine Klasse für einen einfachen Vokabeltrainer.

    Examples:
        >>> trainer = VocabularyTrainer()
        >>> trainer.add_word("house", "Haus")
        >>> trainer.add_word("cat", "Katze")
        >>> trainer.mark_as_learned("house")
        >>> stats = trainer.get_statistics()
        >>> stats["learned_count"]
        1
        >>> stats["total_count"]
        2
    """

    def __init__(self):
        """Initialisiert den Vokabeltrainer."""
        self.words = {}  # Format: {word: {'translation': trans, 'language': lang}}
        self.learned_words = set()

    def add_word(self, word, translation, language="EN"):
        """Fügt ein neues Wort hinzu."""
        self.words[word] = {"translation": translation, "language": language}

    def practice_word(self):
        """Wählt ein zufälliges Wort zum Üben aus."""
        if not self.words:
            return None

        word = random.choice(list(self.words.keys()))
        return {"word": word, "translation": self.words[word]["translation"]}

    def mark_as_learned(self, word):
        """Markiert ein Wort als gelernt."""
        if word in self.words:
            self.learned_words.add(word)

    def get_statistics(self):
        """Gibt Statistiken über gelernte/nicht gelernte Wörter zurück."""
        total_count = len(self.words)
        learned_count = len(self.learned_words)

        return {
            "total_count": total_count,
            "learned_count": learned_count,
            "remaining_count": total_count - learned_count,
            "progress_percentage": (
                (learned_count / total_count * 100) if total_count > 0 else 0
            ),
        }


if __name__ == "__main__":
    import doctest

    doctest.testmod()
