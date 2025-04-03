# -*- coding: utf-8 -*-
def pascal_dreieck(zeilen):
    """
    Erzeugt und visualisiert das Pascal'sche Dreieck für eine bestimmte Anzahl von Zeilen.

    Args:
        zeilen: Die Anzahl der Zeilen, die im Pascal'schen Dreieck dargestellt werden sollen

    Returns:
        Eine Liste von Listen, wobei jede innere Liste eine Zeile des Pascal'schen Dreiecks darstellt.

    Beispiele:
    >>> pascal_dreieck(1)
    [[1]]

    >>> pascal_dreieck(3)
    [[1], [1, 1], [1, 2, 1]]

    >>> pascal_dreieck(5)
    [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

    >>> len(pascal_dreieck(7))
    7

    >>> pascal_dreieck(4)[2]
    [1, 2, 1]

    >>> pascal_dreieck(6)[5][3]
    10
    """
    # Erstelle eine leere Liste, die das Dreieck speichern wird
    dreieck = []

    # Erzeuge jede Zeile des Dreiecks
    for i in range(zeilen):
        # Jede Zeile beginnt als leere Liste
        aktuelle_zeile = []

        # Fülle die aktuelle Zeile
        for j in range(i + 1):
            # Die ersten und letzten Elemente jeder Zeile sind immer 1
            if j == 0 or j == i:
                aktuelle_zeile.append(1)
            else:
                # Andere Elemente sind die Summe der zwei Zahlen direkt darüber
                vorherige_zeile = dreieck[i - 1]
                wert = vorherige_zeile[j - 1] + vorherige_zeile[j]
                aktuelle_zeile.append(wert)

        # Füge die fertige Zeile zum Dreieck hinzu
        dreieck.append(aktuelle_zeile)

    # Visualisiere das Dreieck (mit schöner Formatierung)
    for i, zeile in enumerate(dreieck):
        # Berechne Einrückung für eine zentrierte Darstellung
        einrueckung = " " * (zeilen - i - 1) * 2

        # Wandle die Zahlen in Strings um und füge Leerzeichen dazwischen
        zahlen_mit_abstand = "  ".join(str(zahl) for zahl in zeile)

        # Gib die formatierte Zeile aus
        print(f'{einrueckung}{zahlen_mit_abstand}')

    # Gib das erstellte Dreieck zurück (für Tests und weitere Verarbeitung)
    return dreieck


# Beispielaufruf: Zeige die ersten 7 Zeilen des Pascal'schen Dreiecks
print("Pascal'sches Dreieck mit 7 Zeilen:")
pascal_dreieck(7)

# Führe die Doctests aus, wenn die Datei direkt ausgeführt wird
if __name__ == "__main__":
    import doctest

    doctest.testmod(verbose=True)

    # Zusätzlicher interaktiver Test
    print("\nInteraktiver Test:")
    try:
        anzahl_zeilen = int(input("Gib die gewünschte Anzahl von Zeilen ein (1-20): "))
        if 1 <= anzahl_zeilen <= 20:
            print(f"\nPascal'sches Dreieck mit {anzahl_zeilen} Zeilen:")
            pascal_dreieck(anzahl_zeilen)
        else:
            print("Bitte gib eine Zahl zwischen 1 und 20 ein.")
    except ValueError:
        print("Bitte gib eine gültige Zahl ein.")
