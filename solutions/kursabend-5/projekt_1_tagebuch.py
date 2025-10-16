"""
Digitales Tagebuch
Musterlösung für Kursabend 5, Projekt 1
"""

from datetime import datetime
import os


def neuer_eintrag():
    """Erstellt einen neuen Tagebucheintrag."""
    heute = datetime.now()
    datum_str = heute.strftime('%Y-%m-%d')
    zeit_str = heute.strftime('%H:%M:%S')
    
    print(f"\n{'=' * 60}")
    print(f"NEUER EINTRAG ({datum_str})")
    print("=" * 60)
    
    # Optional: Stimmung erfassen
    print("\nWie fühlst du dich heute?")
    print("1. 😊 Gut")
    print("2. 😐 Neutral")
    print("3. 😢 Schlecht")
    
    try:
        stimmung_nr = int(input("Wähle (1-3, Enter für keine Angabe): ") or "0")
        stimmungen = {1: "😊", 2: "😐", 3: "😢"}
        stimmung = stimmungen.get(stimmung_nr, "")
    except ValueError:
        stimmung = ""
    
    # Eintrag erfassen
    print("\nWas möchtest du festhalten? (Beende mit einer leeren Zeile)")
    zeilen = []
    while True:
        zeile = input()
        if not zeile:
            break
        zeilen.append(zeile)
    
    eintrag = '\n'.join(zeilen)
    
    if not eintrag:
        print("Kein Eintrag erfasst.")
        return
    
    # Erstelle Verzeichnis, falls nicht vorhanden
    os.makedirs('eintraege', exist_ok=True)
    
    # Speichere Eintrag
    dateiname = f'eintraege/{datum_str}.txt'
    with open(dateiname, 'a', encoding='utf-8') as datei:
        datei.write(f"\n[{zeit_str}]")
        if stimmung:
            datei.write(f" {stimmung}")
        datei.write("\n")
        datei.write(f"{eintrag}\n")
        datei.write("-" * 60 + "\n")
    
    print("\n✓ Eintrag gespeichert!")


def zeige_eintraege():
    """Zeigt alle Tagebucheinträge an."""
    if not os.path.exists('eintraege'):
        print("\nNoch keine Einträge vorhanden.")
        return
    
    dateien = sorted(os.listdir('eintraege'))
    
    if not dateien:
        print("\nNoch keine Einträge vorhanden.")
        return
    
    print(f"\n{'=' * 60}")
    print("ALLE EINTRÄGE")
    print("=" * 60)
    
    for datei in dateien:
        if datei.endswith('.txt'):
            datum = datei.replace('.txt', '')
            print(f"\n📅 {datum}")
            print("-" * 60)
            
            with open(f'eintraege/{datei}', 'r', encoding='utf-8') as f:
                print(f.read())


def suche_nach_datum():
    """Sucht Einträge nach einem bestimmten Datum."""
    datum_str = input("\nDatum (YYYY-MM-DD): ")
    dateiname = f'eintraege/{datum_str}.txt'
    
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            print(f"\n{'=' * 60}")
            print(f"EINTRAG VOM {datum_str}")
            print("=" * 60)
            print(datei.read())
    except FileNotFoundError:
        print(f"\nKein Eintrag für {datum_str} gefunden.")


def statistik():
    """Zeigt Statistiken über die Einträge."""
    if not os.path.exists('eintraege'):
        print("\nNoch keine Einträge vorhanden.")
        return
    
    dateien = [f for f in os.listdir('eintraege') if f.endswith('.txt')]
    
    if not dateien:
        print("\nNoch keine Einträge vorhanden.")
        return
    
    print(f"\n{'=' * 60}")
    print("STATISTIK")
    print("=" * 60)
    print(f"Anzahl Einträge: {len(dateien)}")
    
    # Zähle Einträge pro Monat
    monate = {}
    for datei in dateien:
        datum = datei.replace('.txt', '')
        monat = datum[:7]  # YYYY-MM
        monate[monat] = monate.get(monat, 0) + 1
    
    print("\nEinträge pro Monat:")
    for monat in sorted(monate.keys()):
        print(f"  {monat}: {monate[monat]} Einträge")


def exportiere_alle():
    """Exportiert alle Einträge in eine einzelne Datei."""
    if not os.path.exists('eintraege'):
        print("\nNoch keine Einträge vorhanden.")
        return
    
    dateien = sorted([f for f in os.listdir('eintraege') if f.endswith('.txt')])
    
    if not dateien:
        print("\nNoch keine Einträge vorhanden.")
        return
    
    ausgabe = f'tagebuch_export_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt'
    
    with open(ausgabe, 'w', encoding='utf-8') as export:
        export.write("=" * 60 + "\n")
        export.write("TAGEBUCH EXPORT\n")
        export.write(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        export.write("=" * 60 + "\n\n")
        
        for datei in dateien:
            datum = datei.replace('.txt', '')
            export.write(f"\n{'=' * 60}\n")
            export.write(f"📅 {datum}\n")
            export.write("=" * 60 + "\n")
            
            with open(f'eintraege/{datei}', 'r', encoding='utf-8') as f:
                export.write(f.read())
            export.write("\n")
    
    print(f"\n✓ Alle Einträge wurden in '{ausgabe}' exportiert.")


def hauptmenu():
    """Zeigt das Hauptmenü an."""
    while True:
        print(f"\n{'=' * 60}")
        print("DIGITALES TAGEBUCH")
        print("=" * 60)
        print("1. Neuer Eintrag")
        print("2. Alle Einträge anzeigen")
        print("3. Nach Datum suchen")
        print("4. Statistik")
        print("5. Alle Einträge exportieren")
        print("6. Beenden")
        
        wahl = input("\nWähle eine Option (1-6): ")
        
        if wahl == '1':
            neuer_eintrag()
        elif wahl == '2':
            zeige_eintraege()
        elif wahl == '3':
            suche_nach_datum()
        elif wahl == '4':
            statistik()
        elif wahl == '5':
            exportiere_alle()
        elif wahl == '6':
            print("\n👋 Auf Wiedersehen! Bis zum nächsten Mal!")
            break
        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-6.")


if __name__ == '__main__':
    hauptmenu()
