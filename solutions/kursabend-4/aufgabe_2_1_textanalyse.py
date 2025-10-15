"""
Textanalyse-Tool
Musterlösung für Kursabend 4, Aufgabe 2.1
"""

from collections import Counter


def analysiere_text(dateiname):
    """
    Analysiert eine Textdatei und gibt verschiedene Statistiken zurück.
    
    Args:
        dateiname (str): Pfad zur Textdatei
        
    Returns:
        dict: Dictionary mit Analyseergebnissen
    """
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            zeilen = datei.readlines()
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden!")
        return None
    
    # Zähle Zeilen
    anzahl_zeilen = len(zeilen)
    
    # Sammle alle Wörter
    alle_woerter = []
    for zeile in zeilen:
        # Entferne Satzzeichen und teile in Wörter
        woerter = zeile.split()
        alle_woerter.extend(woerter)
    
    # Bereinige Wörter (entferne Satzzeichen)
    bereinigte_woerter = []
    for wort in alle_woerter:
        # Entferne Satzzeichen am Anfang und Ende
        wort = wort.strip('.,!?;:()[]{}"-')
        if wort:  # Nur nicht-leere Wörter
            bereinigte_woerter.append(wort.lower())
    
    # Zähle Wörter
    anzahl_woerter = len(bereinigte_woerter)
    
    # Zähle Zeichen (ohne Leerzeichen)
    gesamttext = ''.join(zeilen)
    anzahl_zeichen = len(gesamttext.replace(' ', '').replace('\n', ''))
    
    # Berechne durchschnittliche Wortlänge
    if anzahl_woerter > 0:
        gesamtlaenge = sum(len(wort) for wort in bereinigte_woerter)
        durchschnitt_wortlaenge = gesamtlaenge / anzahl_woerter
    else:
        durchschnitt_wortlaenge = 0
    
    # Finde längstes Wort
    if bereinigte_woerter:
        laengstes_wort = max(bereinigte_woerter, key=len)
    else:
        laengstes_wort = ""
    
    # Finde häufigstes Wort
    if bereinigte_woerter:
        wort_zaehler = Counter(bereinigte_woerter)
        haeufigste = wort_zaehler.most_common(1)[0]
        haeufigste_wort = haeufigste[0]
        haeufigste_anzahl = haeufigste[1]
    else:
        haeufigste_wort = ""
        haeufigste_anzahl = 0
    
    return {
        'dateiname': dateiname,
        'zeilen': anzahl_zeilen,
        'woerter': anzahl_woerter,
        'zeichen': anzahl_zeichen,
        'durchschnitt_wortlaenge': durchschnitt_wortlaenge,
        'laengstes_wort': laengstes_wort,
        'haeufigste_wort': haeufigste_wort,
        'haeufigste_anzahl': haeufigste_anzahl
    }


def zeige_analyse(ergebnis):
    """
    Zeigt die Analyseergebnisse formatiert an.
    
    Args:
        ergebnis (dict): Dictionary mit Analyseergebnissen
    """
    if not ergebnis:
        return
    
    print("\n" + "=" * 60)
    print("TEXTANALYSE")
    print("=" * 60)
    print(f"Datei: {ergebnis['dateiname']}")
    print()
    print(f"Zeilen:                    {ergebnis['zeilen']:,}")
    print(f"Wörter:                    {ergebnis['woerter']:,}")
    print(f"Zeichen:                   {ergebnis['zeichen']:,}")
    print(f"Durchschnittliche Wortlänge: {ergebnis['durchschnitt_wortlaenge']:.1f} Zeichen")
    print(f"Längstes Wort:             {ergebnis['laengstes_wort']} ({len(ergebnis['laengstes_wort'])} Zeichen)")
    print(f"Häufigstes Wort:           {ergebnis['haeufigste_wort']} ({ergebnis['haeufigste_anzahl']} mal)")
    print("=" * 60)


def speichere_bericht(ergebnis, ausgabedatei='analyse.txt'):
    """
    Speichert die Analyseergebnisse in einer Datei.
    
    Args:
        ergebnis (dict): Dictionary mit Analyseergebnissen
        ausgabedatei (str): Pfad zur Ausgabedatei
    """
    if not ergebnis:
        return
    
    with open(ausgabedatei, 'w', encoding='utf-8') as datei:
        datei.write("=" * 60 + "\n")
        datei.write("TEXTANALYSE\n")
        datei.write("=" * 60 + "\n")
        datei.write(f"Datei: {ergebnis['dateiname']}\n")
        datei.write("\n")
        datei.write(f"Zeilen:                    {ergebnis['zeilen']:,}\n")
        datei.write(f"Wörter:                    {ergebnis['woerter']:,}\n")
        datei.write(f"Zeichen:                   {ergebnis['zeichen']:,}\n")
        datei.write(f"Durchschnittliche Wortlänge: {ergebnis['durchschnitt_wortlaenge']:.1f} Zeichen\n")
        datei.write(f"Längstes Wort:             {ergebnis['laengstes_wort']} ({len(ergebnis['laengstes_wort'])} Zeichen)\n")
        datei.write(f"Häufigstes Wort:           {ergebnis['haeufigste_wort']} ({ergebnis['haeufigste_anzahl']} mal)\n")
        datei.write("=" * 60 + "\n")
    
    print(f"\n✓ Bericht wurde in '{ausgabedatei}' gespeichert.")


def hauptprogramm():
    """Hauptprogramm für die Textanalyse."""
    print("=" * 60)
    print("TEXTANALYSE-TOOL")
    print("=" * 60)
    
    dateiname = input("\nDateiname (z.B. beispieltext.txt): ")
    
    # Analysiere Text
    ergebnis = analysiere_text(dateiname)
    
    if ergebnis:
        # Zeige Ergebnisse
        zeige_analyse(ergebnis)
        
        # Speichere Bericht
        speichern = input("\nBericht speichern? (j/n): ")
        if speichern.lower() == 'j':
            speichere_bericht(ergebnis)


if __name__ == '__main__':
    hauptprogramm()
