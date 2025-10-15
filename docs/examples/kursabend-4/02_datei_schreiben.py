"""
Beispiel 2: Datei schreiben
Zeigt verschiedene Modi zum Schreiben in Dateien.
"""

# Modus 'w': Schreiben (überschreibt die Datei!)
print("=== Modus 'w': Datei neu schreiben ===")
with open('ausgabe.txt', 'w', encoding='utf-8') as datei:
    datei.write('Dies ist die erste Zeile.\n')
    datei.write('Dies ist die zweite Zeile.\n')
    datei.write('Dies ist die dritte Zeile.\n')

print("✓ Datei 'ausgabe.txt' wurde erstellt.")

# Modus 'a': Anhängen (fügt am Ende hinzu)
print("\n=== Modus 'a': An Datei anhängen ===")
with open('ausgabe.txt', 'a', encoding='utf-8') as datei:
    datei.write('Diese Zeile wurde angehängt.\n')
    datei.write('Noch eine angehängte Zeile.\n')

print("✓ Zeilen wurden an 'ausgabe.txt' angehängt.")

# Datei lesen und anzeigen
print("\n=== Inhalt von ausgabe.txt ===")
with open('ausgabe.txt', 'r', encoding='utf-8') as datei:
    print(datei.read())
