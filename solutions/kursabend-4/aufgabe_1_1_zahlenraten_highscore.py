"""
Zahlenraten mit Highscore-Funktion
Musterlösung für Kursabend 4, Aufgabe 1.1
"""

import random
from datetime import datetime


def lade_highscore():
    """
    Lädt den Highscore aus der Datei.
    
    Returns:
        dict: Dictionary mit 'versuche' und 'datum' oder None
    """
    try:
        with open('highscore.txt', 'r', encoding='utf-8') as datei:
            zeilen = datei.readlines()
            if zeilen:
                versuche = int(zeilen[0].strip())
                datum = zeilen[1].strip() if len(zeilen) > 1 else "Unbekannt"
                return {'versuche': versuche, 'datum': datum}
    except FileNotFoundError:
        return None
    except ValueError:
        print("Fehler beim Lesen der Highscore-Datei.")
        return None


def speichere_highscore(versuche):
    """
    Speichert einen neuen Highscore.
    
    Args:
        versuche (int): Anzahl der benötigten Versuche
    """
    datum = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('highscore.txt', 'w', encoding='utf-8') as datei:
        datei.write(f"{versuche}\n")
        datei.write(f"{datum}\n")


def spiele_runde():
    """
    Spielt eine Runde Zahlenraten.
    
    Returns:
        int: Anzahl der benötigten Versuche
    """
    zahl = random.randint(1, 100)
    versuche = 0
    
    print("\n" + "=" * 50)
    print("Ich habe mir eine Zahl zwischen 1 und 100 ausgedacht.")
    print("Kannst du sie erraten?")
    print("=" * 50)
    
    while True:
        versuche += 1
        
        try:
            tipp = int(input(f"\nVersuch {versuche}: Dein Tipp: "))
        except ValueError:
            print("Bitte gib eine gültige Zahl ein!")
            versuche -= 1  # Ungültige Eingabe zählt nicht
            continue
        
        if tipp < zahl:
            print("Zu klein! Versuche es mit einer größeren Zahl.")
        elif tipp > zahl:
            print("Zu groß! Versuche es mit einer kleineren Zahl.")
        else:
            print(f"\n🎉 Glückwunsch! Du hast die Zahl {zahl} erraten!")
            print(f"Du hast {versuche} Versuche gebraucht.")
            return versuche


def hauptprogramm():
    """Hauptprogramm mit Highscore-Verwaltung."""
    print("=" * 50)
    print("ZAHLENRATEN MIT HIGHSCORE")
    print("=" * 50)
    
    # Lade aktuellen Highscore
    highscore = lade_highscore()
    
    if highscore:
        print(f"\n🏆 Aktueller Rekord: {highscore['versuche']} Versuche")
        print(f"   Aufgestellt am: {highscore['datum']}")
    else:
        print("\n📊 Noch kein Highscore vorhanden.")
    
    while True:
        # Spiele eine Runde
        versuche = spiele_runde()
        
        # Prüfe, ob neuer Rekord
        if highscore is None or versuche < highscore['versuche']:
            print("\n" + "=" * 50)
            print("🎊 NEUER REKORD! 🎊")
            print("=" * 50)
            speichere_highscore(versuche)
            highscore = {'versuche': versuche, 'datum': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        else:
            print(f"\nDer Rekord liegt bei {highscore['versuche']} Versuchen.")
        
        # Nochmal spielen?
        nochmal = input("\nNochmal spielen? (j/n): ")
        if nochmal.lower() != 'j':
            print("\nDanke fürs Spielen! Bis zum nächsten Mal! 👋")
            break


if __name__ == '__main__':
    hauptprogramm()
