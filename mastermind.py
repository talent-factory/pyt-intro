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
    print("Mastermind")

    # Computer denkt sich 4 Zufallszahlen im Bereich 1..6 aus
    code = ""
    for _ in range(4):
        code += str(randint(1, 6))

    while True:  # Schleife für mehrere Rateversuche
        # Benutzer muss eine 4stellige Zahl (als Zeichenkette) eingeben
        guess = input("Gib eine 4stellige Zahl ein: ")

        # Prüfe Eingabe auf Gültigkeit
        if len(guess) != 4 or not guess.isdigit():
            print("Bitte gib genau 4 Ziffern ein!")
            continue

        correct_place = sum(x == y for x, y in zip(code, guess))

        # Berechne richtige Zahlen an falscher Position
        code_list = list(code)
        guess_list = list(guess)
        correct_numbers = 0

        for i in range(len(guess)):
            if guess_list[i] in code_list:
                if guess_list[i] != code_list[i]:  # Nur zählen, wenn nicht schon als "correct_place" gezählt
                    correct_numbers += 1
                    code_list[code_list.index(guess_list[i])] = 'X'  # Markiere als verwendet

        print(f"Deine Eingabe: {guess}")
        print(f"Richtige Stellen: {correct_place}")
        print(f"Richtige Zahlen:  {correct_numbers}")

        # Die Zahl wurde richtig erraten
        if correct_place == 4:
            print("Richtig erraten!")
            return


if __name__ == "__main__":
    mastermind()
    print("Am Ende des Spiels")
