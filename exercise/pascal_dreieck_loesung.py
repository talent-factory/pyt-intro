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

"""
Musterlösung für Aufgabe 6: Pascal'sches Dreieck
"""


def pascal_dreieck(zeilen):
    """
    Berechnet das Pascal'sche Dreieck für die angegebene Anzahl von Zeilen

    Parameter:
    zeilen (int): Die Anzahl der zu berechnenden Zeilen

    Returns:
    list: Das Pascal'sche Dreieck als Liste von Listen
    """
    if zeilen <= 0:
        return []

    # Initialisieren mit der ersten Zeile
    dreieck = [[1]]

    # Berechnen der weiteren Zeilen
    for i in range(1, zeilen):
        vorherige_zeile = dreieck[i - 1]
        neue_zeile = [1]  # Erste Zahl in jeder Zeile ist immer 1

        # Berechnen der mittleren Zahlen (Summe der beiden Zahlen darüber)
        for j in range(1, i):
            neue_zeile.append(vorherige_zeile[j - 1] + vorherige_zeile[j])

        neue_zeile.append(1)  # Letzte Zahl in jeder Zeile ist immer 1
        dreieck.append(neue_zeile)

    return dreieck


def pascal_dreieck_ausgeben(dreieck):
    """
    Gibt das Pascal'sche Dreieck formatiert aus

    Parameter:
    dreieck (list): Das Pascal'sche Dreieck als Liste von Listen
    """
    if not dreieck:
        print("Leeres Dreieck")
        return

    # Anzahl der Zeilen
    zeilen = len(dreieck)

    # Maximale Breite ermitteln (basierend auf der letzten Zeile, die am breitesten ist)
    max_breite = len(" ".join(str(zahl) for zahl in dreieck[-1]))

    # Ausgabe jeder Zeile
    for i, zeile in enumerate(dreieck):
        # Umwandeln der Zahlen in Strings und Verbinden mit Leerzeichen
        zeile_str = " ".join(str(zahl) for zahl in zeile)

        # Zentrieren der Zeile auf die maximale Breite
        zentrierte_zeile = zeile_str.center(max_breite)

        print(zentrierte_zeile)


# Testen der Funktionen
dreieck = pascal_dreieck(5)
print("Pascal'sches Dreieck als Liste von Listen:")
print(dreieck)
# Sollte ausgeben: [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

print("\nFormatierte Ausgabe des Pascal'schen Dreiecks:")
pascal_dreieck_ausgeben(dreieck)
# Sollte formatiert ausgeben:
#     1
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1

print("\nPascal'sches Dreieck mit 10 Zeilen:")
grosses_dreieck = pascal_dreieck(10)
pascal_dreieck_ausgeben(grosses_dreieck)

# Testen mit Randfall
print("\nPascal'sches Dreieck mit 0 Zeilen:")
leeres_dreieck = pascal_dreieck(0)
pascal_dreieck_ausgeben(leeres_dreieck)

print("\nPascal'sches Dreieck mit 1 Zeile:")
einzel_dreieck = pascal_dreieck(1)
pascal_dreieck_ausgeben(einzel_dreieck)
