"""
Live-Coding Beispiel: Textdatei einlesen, Zeilen zählen, in neue Datei schreiben
Dies ist das Beispiel für die gemeinsame Live-Coding-Session.
"""

def analysiere_und_speichere(eingabe_datei, ausgabe_datei):
    """
    Liest eine Textdatei ein, zählt die Zeilen und schreibt
    einen Bericht in eine neue Datei.
    
    Args:
        eingabe_datei (str): Pfad zur Eingabedatei
        ausgabe_datei (str): Pfad zur Ausgabedatei
    """
    try:
        # Schritt 1: Datei lesen
        print(f"Lese Datei '{eingabe_datei}'...")
        with open(eingabe_datei, 'r', encoding='utf-8') as datei:
            zeilen = datei.readlines()
        
        # Schritt 2: Analyse durchführen
        anzahl_zeilen = len(zeilen)
        anzahl_zeichen = sum(len(zeile) for zeile in zeilen)
        
        # Zähle nicht-leere Zeilen
        nicht_leere_zeilen = [zeile for zeile in zeilen if zeile.strip()]
        anzahl_nicht_leer = len(nicht_leere_zeilen)
        
        print(f"✓ Datei erfolgreich gelesen!")
        print(f"  - {anzahl_zeilen} Zeilen")
        print(f"  - {anzahl_nicht_leer} nicht-leere Zeilen")
        print(f"  - {anzahl_zeichen} Zeichen")
        
        # Schritt 3: Bericht erstellen und speichern
        print(f"\nErstelle Bericht in '{ausgabe_datei}'...")
        with open(ausgabe_datei, 'w', encoding='utf-8') as datei:
            datei.write("=" * 60 + "\n")
            datei.write("TEXTANALYSE-BERICHT\n")
            datei.write("=" * 60 + "\n")
            datei.write(f"Eingabedatei: {eingabe_datei}\n")
            datei.write("\n")
            datei.write(f"Anzahl Zeilen:           {anzahl_zeilen}\n")
            datei.write(f"Nicht-leere Zeilen:      {anzahl_nicht_leer}\n")
            datei.write(f"Anzahl Zeichen:          {anzahl_zeichen}\n")
            datei.write("\n")
            datei.write("=" * 60 + "\n")
            datei.write("INHALT DER DATEI\n")
            datei.write("=" * 60 + "\n")
            
            # Schreibe alle Zeilen mit Zeilennummern
            for i, zeile in enumerate(zeilen, 1):
                datei.write(f"{i:3d}: {zeile}")
        
        print(f"✓ Bericht wurde erfolgreich erstellt!")
        
    except FileNotFoundError:
        print(f"❌ Fehler: Die Datei '{eingabe_datei}' wurde nicht gefunden!")
    except PermissionError:
        print(f"❌ Fehler: Keine Berechtigung für Dateioperationen!")
    except Exception as e:
        print(f"❌ Ein Fehler ist aufgetreten: {e}")


# Hauptprogramm
if __name__ == '__main__':
    print("=" * 60)
    print("TEXTDATEI ANALYSIEREN UND BERICHT ERSTELLEN")
    print("=" * 60)
    print()
    
    # Verwende die Beispieldatei
    eingabe = 'beispiel.txt'
    ausgabe = 'bericht.txt'
    
    analysiere_und_speichere(eingabe, ausgabe)
    
    print("\n" + "=" * 60)
    print("FERTIG!")
    print("=" * 60)
    print(f"\nDu kannst den Bericht jetzt in '{ausgabe}' ansehen.")
