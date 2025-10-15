"""
Quiz-Generator
Musterlösung für Kursabend 5, Projekt 3
"""

import random
from datetime import datetime


def lade_fragen(dateiname):
    """
    Lädt Fragen aus einer Datei.
    
    Args:
        dateiname (str): Pfad zur Fragen-Datei
        
    Returns:
        list: Liste von Fragen-Dictionaries
    """
    fragen = []
    
    try:
        with open(dateiname, 'r', encoding='utf-8') as datei:
            inhalt = datei.read()
            fragen_text = inhalt.split('---')
            
            for frage_text in fragen_text:
                frage_text = frage_text.strip()
                if not frage_text:
                    continue
                
                zeilen = frage_text.split('\n')
                if len(zeilen) >= 6:
                    frage = {
                        'frage': zeilen[0],
                        'antworten': zeilen[1:5],
                        'richtig': zeilen[5].strip()
                    }
                    fragen.append(frage)
    
    except FileNotFoundError:
        print(f"❌ Fehler: Datei '{dateiname}' nicht gefunden!")
        return []
    
    return fragen


def stelle_frage(frage, nummer, gesamt):
    """
    Stellt eine einzelne Frage.
    
    Args:
        frage (dict): Fragen-Dictionary
        nummer (int): Aktuelle Fragennummer
        gesamt (int): Gesamtanzahl Fragen
        
    Returns:
        bool: True wenn richtig beantwortet, sonst False
    """
    print(f"\n{'=' * 60}")
    print(f"FRAGE {nummer}/{gesamt}")
    print("=" * 60)
    print(frage['frage'])
    print()
    for antwort in frage['antworten']:
        print(antwort)
    
    while True:
        eingabe = input("\nDeine Antwort (A/B/C/D): ").upper()
        if eingabe in ['A', 'B', 'C', 'D']:
            break
        print("❌ Ungültige Eingabe! Bitte A, B, C oder D eingeben.")
    
    if eingabe == frage['richtig']:
        print("✅ Richtig!")
        return True
    else:
        print(f"❌ Falsch! Die richtige Antwort war {frage['richtig']}")
        return False


def spiele_quiz(dateiname='quiz.txt'):
    """
    Führt das Quiz durch.
    
    Args:
        dateiname (str): Pfad zur Fragen-Datei
        
    Returns:
        tuple: (punkte, gesamt)
    """
    fragen = lade_fragen(dateiname)
    
    if not fragen:
        return 0, 0
    
    random.shuffle(fragen)  # Zufällige Reihenfolge
    
    punkte = 0
    gesamt = len(fragen)
    
    print("\n" + "=" * 60)
    print("🎯 QUIZ START!")
    print("=" * 60)
    print(f"Es erwarten dich {gesamt} Fragen. Viel Erfolg!")
    
    for i, frage in enumerate(fragen, 1):
        if stelle_frage(frage, i, gesamt):
            punkte += 1
        
        # Zwischenstand
        if i < gesamt:
            input("\nDrücke Enter für die nächste Frage...")
    
    return punkte, gesamt


def zeige_ergebnis(punkte, gesamt):
    """
    Zeigt das Endergebnis an.
    
    Args:
        punkte (int): Erreichte Punkte
        gesamt (int): Maximale Punkte
    """
    if gesamt == 0:
        return
    
    prozent = (punkte / gesamt) * 100
    
    print("\n" + "=" * 60)
    print("🏁 QUIZ BEENDET!")
    print("=" * 60)
    print(f"Punkte: {punkte}/{gesamt} ({prozent:.1f}%)")
    
    # Bewertung
    if prozent >= 90:
        print("🌟 Ausgezeichnet! Du bist ein Experte!")
    elif prozent >= 70:
        print("👍 Sehr gut! Du kennst dich gut aus!")
    elif prozent >= 50:
        print("👌 Gut gemacht! Noch etwas Übung und du bist top!")
    else:
        print("💪 Nicht aufgeben! Übung macht den Meister!")
    
    print("=" * 60)


def speichere_ergebnis(punkte, gesamt):
    """
    Speichert das Quiz-Ergebnis in der Highscore-Liste.
    
    Args:
        punkte (int): Erreichte Punkte
        gesamt (int): Maximale Punkte
    """
    if gesamt == 0:
        return
    
    datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    prozent = (punkte / gesamt) * 100
    
    with open('quiz_ergebnisse.txt', 'a', encoding='utf-8') as datei:
        datei.write(f"{datum}|{punkte}|{gesamt}|{prozent:.1f}\n")
    
    print("\n✓ Ergebnis wurde gespeichert!")


def zeige_highscore():
    """Zeigt die Highscore-Liste an."""
    try:
        with open('quiz_ergebnisse.txt', 'r', encoding='utf-8') as datei:
            zeilen = datei.readlines()
        
        if not zeilen:
            print("\nNoch keine Ergebnisse vorhanden.")
            return
        
        print(f"\n{'=' * 60}")
        print("🏆 HIGHSCORE")
        print("=" * 60)
        print(f"{'Datum':<20} {'Punkte':>10} {'Prozent':>10}")
        print("-" * 60)
        
        # Sortiere nach Prozent (absteigend)
        ergebnisse = []
        for zeile in zeilen:
            teile = zeile.strip().split('|')
            if len(teile) == 4:
                datum, punkte, gesamt, prozent = teile
                ergebnisse.append({
                    'datum': datum,
                    'punkte': f"{punkte}/{gesamt}",
                    'prozent': float(prozent)
                })
        
        ergebnisse.sort(key=lambda x: x['prozent'], reverse=True)
        
        for i, erg in enumerate(ergebnisse[:10], 1):  # Top 10
            symbol = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}."
            print(f"{symbol:<3} {erg['datum']:<17} {erg['punkte']:>10} {erg['prozent']:>9.1f}%")
        
        print("=" * 60)
    
    except FileNotFoundError:
        print("\nNoch keine Ergebnisse vorhanden.")


def hauptmenu():
    """Zeigt das Hauptmenü an."""
    while True:
        print(f"\n{'=' * 60}")
        print("🎯 QUIZ-GENERATOR")
        print("=" * 60)
        print("1. Quiz starten")
        print("2. Highscore anzeigen")
        print("3. Beenden")
        
        wahl = input("\nWähle eine Option (1-3): ")
        
        if wahl == '1':
            dateiname = input("\nFragen-Datei (Enter für 'quiz.txt'): ") or 'quiz.txt'
            punkte, gesamt = spiele_quiz(dateiname)
            zeige_ergebnis(punkte, gesamt)
            
            if gesamt > 0:
                speichere_ergebnis(punkte, gesamt)
        
        elif wahl == '2':
            zeige_highscore()
        
        elif wahl == '3':
            print("\n👋 Auf Wiedersehen! Bis zum nächsten Mal!")
            break
        
        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-3.")


if __name__ == '__main__':
    hauptmenu()
