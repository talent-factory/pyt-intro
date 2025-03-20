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

# noinspection PyShadowingNames
def berechne_menschenjahre(hunde_alter):
    """
    Rechnet das Alter eines Hundes in menschliche Jahre um.

    Parameter:
    hunde_alter (float): Das Alter des Hundes in Jahren

    Rückgabe:
    float: Das entsprechende Alter in Menschenjahren
    """
    # Überprüfe, ob das Alter positiv ist
    if hunde_alter < 0:
        return "Das Alter muss positiv sein!"

    # Umrechnung gemäß den Regeln
    if hunde_alter <= 1:
        # Für Hunde bis zu einem Jahr: linear von 0 bis 14 Jahre
        menschen_alter = hunde_alter * 14
    elif hunde_alter <= 2:
        # Für Hunde zwischen 1 und 2 Jahren:
        # 14 Jahre + die zusätzlichen Monate (anteilig von 8 Jahren)
        menschen_alter = 14 + (hunde_alter - 1) * 8
    else:
        # Für Hunde über 2 Jahre:
        # 22 Jahre + 5 Jahre für jedes weitere Jahr
        menschen_alter = 22 + (hunde_alter - 2) * 5

    return menschen_alter


# Hauptprogramm
try:
    # Benutzereingabe für das Hundealter
    hunde_alter_eingabe = input("Wie alt ist dein Hund? (in Jahren): ")

    # Umwandlung der Eingabe in eine Dezimalzahl
    hunde_alter = float(hunde_alter_eingabe)

    # Berechnung des Menschenalters
    menschen_alter = berechne_menschenjahre(hunde_alter)

    # Ausgabe des Ergebnisses
    if isinstance(menschen_alter, str):
        print(menschen_alter)
    else:
        print(f"Dein Hund ist {hunde_alter} Jahre alt.")
        print(f"Das entspricht einem menschlichen Alter von {menschen_alter:.1f} Jahren.")

except ValueError:
    # Fehlerbehandlung bei ungültiger Eingabe
    print("Bitte gib eine gültige Zahl ein!")
