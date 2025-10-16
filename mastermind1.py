#  Released under MIT License
#
#  Copyright (©) 2025. Talent Factory GmbH
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

from random import randint


def mastermind():
    code = "".join(str(randint(1, 6)) for _ in range(4))

    while (
        (guess := input("Gib eine 4stellige Zahl ein: "))
        and len(guess) == 4
        and guess.isdigit()
    ):
        correct_place = sum(x == y for x, y in zip(code, guess))
        correct_numbers = (
            sum(min(code.count(d), guess.count(d)) for d in set(guess)) - correct_place
        )

        print(
            f"Deine Eingabe: {guess} | Richtige Stellen: {correct_place} | Richtige Zahlen: {correct_numbers}"
        )

        if correct_place == 4:
            print("Richtig erraten!")
            return

    print("Ungültige Eingabe! Bitte 4 Ziffern eingeben.")


if __name__ == "__main__":
    mastermind()
    print("Am Ende des Spiels")
