"""
Beispiel 1: Datei lesen
Zeigt verschiedene Methoden, um eine Datei zu lesen.
"""

# Methode 1: Gesamte Datei auf einmal lesen
print("=== Methode 1: Gesamte Datei lesen ===")
with open('beispiel.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print(inhalt)

print("\n" + "=" * 50 + "\n")

# Methode 2: Datei zeilenweise lesen
print("=== Methode 2: Zeilenweise lesen ===")
with open('beispiel.txt', 'r', encoding='utf-8') as datei:
    for zeile in datei:
        zeile = zeile.strip()  # Entfernt Leerzeichen und Zeilenumbrüche
        print(f"Zeile: {zeile}")

print("\n" + "=" * 50 + "\n")

# Methode 3: Alle Zeilen in eine Liste
print("=== Methode 3: Alle Zeilen in Liste ===")
with open('beispiel.txt', 'r', encoding='utf-8') as datei:
    zeilen = datei.readlines()
    print(f"Anzahl Zeilen: {len(zeilen)}")
    for i, zeile in enumerate(zeilen, 1):
        print(f"Zeile {i}: {zeile.strip()}")
