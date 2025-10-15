"""
Beispiel 3: Fehlerbehandlung bei Dateien
Zeigt, wie man mit Fehlern beim Lesen von Dateien umgeht.
"""

# Ohne Fehlerbehandlung (würde abstürzen, wenn Datei nicht existiert)
print("=== Versuch 1: Ohne Fehlerbehandlung ===")
print("Wenn die Datei nicht existiert, stürzt das Programm ab!")
print()

# Mit Fehlerbehandlung
print("=== Versuch 2: Mit try-except ===")
dateiname = input("Dateiname eingeben: ")

try:
    with open(dateiname, 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
        print(f"\n✓ Datei erfolgreich gelesen!")
        print(f"Inhalt:\n{inhalt}")
except FileNotFoundError:
    print(f"\n❌ Fehler: Die Datei '{dateiname}' wurde nicht gefunden!")
    print("Bitte überprüfe den Dateinamen und versuche es erneut.")
except PermissionError:
    print(f"\n❌ Fehler: Keine Berechtigung, die Datei '{dateiname}' zu lesen!")
except Exception as e:
    print(f"\n❌ Ein unerwarteter Fehler ist aufgetreten: {e}")

print("\n✓ Das Programm läuft weiter, auch wenn ein Fehler aufgetreten ist!")
