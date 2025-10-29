"""
Vokabeltrainer mit Statistik
Musterlösung für Kursabend 4, Aufgabe 3.1
"""

import random


def lade_vokabeln(dateiname="vokabeln.txt"):
    """
    Lädt Vokabeln aus einer Datei.

    Args:
        dateiname (str): Pfad zur Vokabeldatei

    Returns:
        list: Liste von Vokabel-Dictionaries
    """
    vokabeln = []

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if not zeile or ":" not in zeile:
                    continue

                teile = zeile.split(":")
                if len(teile) == 2:
                    vokabeln.append(
                        {"deutsch": teile[0].strip(), "englisch": teile[1].strip()}
                    )

        return vokabeln

    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden!")
        return []


def lade_statistik(dateiname="statistik.txt"):
    """
    Lädt die Statistik aus einer Datei.

    Args:
        dateiname (str): Pfad zur Statistikdatei

    Returns:
        dict: Dictionary mit Statistiken pro Vokabel
    """
    statistik = {}

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if not zeile or "|" not in zeile:
                    continue

                teile = zeile.split("|")
                if len(teile) == 3:
                    deutsch = teile[0].strip()
                    statistik[deutsch] = {
                        "richtig": int(teile[1]),
                        "falsch": int(teile[2]),
                    }

        return statistik

    except FileNotFoundError:
        return {}
    except ValueError:
        print("Warnung: Fehler beim Lesen der Statistik.")
        return {}


def speichere_statistik(statistik, dateiname="statistik.txt"):
    """
    Speichert die Statistik in einer Datei.

    Args:
        statistik (dict): Dictionary mit Statistiken
        dateiname (str): Pfad zur Statistikdatei
    """
    with open(dateiname, "w", encoding="utf-8") as datei:
        for deutsch, stats in statistik.items():
            datei.write(f"{deutsch}|{stats['richtig']}|{stats['falsch']}\n")


def waehle_vokabel(vokabeln, statistik):
    """
    Wählt eine Vokabel aus, bevorzugt schwierige Vokabeln.

    Args:
        vokabeln (list): Liste aller Vokabeln
        statistik (dict): Dictionary mit Statistiken

    Returns:
        dict: Ausgewählte Vokabel
    """
    # Berechne Gewichtung basierend auf Fehlerquote
    gewichtete_vokabeln = []

    for vokabel in vokabeln:
        deutsch = vokabel["deutsch"]

        if deutsch in statistik:
            stats = statistik[deutsch]
            gesamt = stats["richtig"] + stats["falsch"]

            if gesamt > 0:
                fehlerquote = stats["falsch"] / gesamt
                # Je höher die Fehlerquote, desto höher die Gewichtung
                gewicht = max(1, int(fehlerquote * 10))
            else:
                gewicht = 5  # Mittlere Gewichtung für neue Vokabeln
        else:
            gewicht = 5  # Mittlere Gewichtung für neue Vokabeln

        # Füge Vokabel entsprechend der Gewichtung mehrfach hinzu
        for _ in range(gewicht):
            gewichtete_vokabeln.append(vokabel)

    return random.choice(gewichtete_vokabeln)


def trainiere(vokabeln, statistik):
    """
    Führt eine Trainingsrunde durch.

    Args:
        vokabeln (list): Liste aller Vokabeln
        statistik (dict): Dictionary mit Statistiken

    Returns:
        tuple: (richtige_antworten, falsche_antworten)
    """
    richtig = 0
    falsch = 0

    anzahl = int(input("\nWie viele Vokabeln möchtest du üben? "))

    print("\n" + "=" * 60)
    print("TRAINING GESTARTET")
    print("=" * 60)
    print("Tipp: Gib 'quit' ein, um vorzeitig zu beenden.\n")

    for i in range(anzahl):
        vokabel = waehle_vokabel(vokabeln, statistik)
        deutsch = vokabel["deutsch"]
        englisch = vokabel["englisch"]

        print(f"\nFrage {i + 1}/{anzahl}")
        antwort = input(f"Was heißt '{deutsch}' auf Englisch? ")

        if antwort.lower() == "quit":
            print("\nTraining abgebrochen.")
            break

        # Initialisiere Statistik für diese Vokabel, falls nicht vorhanden
        if deutsch not in statistik:
            statistik[deutsch] = {"richtig": 0, "falsch": 0}

        if antwort.lower() == englisch.lower():
            print("✓ Richtig!")
            richtig += 1
            statistik[deutsch]["richtig"] += 1
        else:
            print(f"✗ Falsch! Die richtige Antwort ist: {englisch}")
            falsch += 1
            statistik[deutsch]["falsch"] += 1

    return richtig, falsch


def zeige_statistik(statistik, vokabeln):
    """
    Zeigt die Gesamtstatistik an.

    Args:
        statistik (dict): Dictionary mit Statistiken
        vokabeln (list): Liste aller Vokabeln
    """
    if not statistik:
        print("\nNoch keine Statistik vorhanden.")
        return

    print("\n" + "=" * 70)
    print("STATISTIK")
    print("=" * 70)
    print(f"{'Vokabel':<20} {'Richtig':>10} {'Falsch':>10} {'Quote':>10}")
    print("-" * 70)

    gesamt_richtig = 0
    gesamt_falsch = 0

    # Sortiere nach Fehlerquote (schwierigste zuerst)
    sortierte = sorted(
        statistik.items(),
        key=lambda x: x[1]["falsch"] / (x[1]["richtig"] + x[1]["falsch"])
        if (x[1]["richtig"] + x[1]["falsch"]) > 0
        else 0,
        reverse=True,
    )

    for deutsch, stats in sortierte:
        richtig = stats["richtig"]
        falsch = stats["falsch"]
        gesamt = richtig + falsch

        if gesamt > 0:
            quote = (richtig / gesamt) * 100
        else:
            quote = 0

        print(f"{deutsch:<20} {richtig:>10} {falsch:>10} {quote:>9.1f}%")

        gesamt_richtig += richtig
        gesamt_falsch += falsch

    print("-" * 70)

    gesamt_gesamt = gesamt_richtig + gesamt_falsch
    if gesamt_gesamt > 0:
        gesamt_quote = (gesamt_richtig / gesamt_gesamt) * 100
    else:
        gesamt_quote = 0

    print(
        f"{'GESAMT':<20} {gesamt_richtig:>10} {gesamt_falsch:>10} {gesamt_quote:>9.1f}%"
    )
    print("=" * 70)


def erstelle_beispiel_vokabeln():
    """Erstellt eine Beispiel-Vokabeldatei."""
    beispieldaten = """Haus:house
Auto:car
Baum:tree
Buch:book
Tisch:table
Stuhl:chair
Fenster:window
Tür:door
Wasser:water
Brot:bread
Apfel:apple
Hund:dog
Katze:cat
Vogel:bird
Fisch:fish"""

    with open("vokabeln.txt", "w", encoding="utf-8") as datei:
        datei.write(beispieldaten)

    print("✓ Beispieldatei 'vokabeln.txt' wurde erstellt.")


def hauptprogramm():
    """Hauptprogramm für den Vokabeltrainer."""
    print("=" * 70)
    print("VOKABELTRAINER")
    print("=" * 70)

    # Lade Vokabeln
    vokabeln = lade_vokabeln()

    if not vokabeln:
        erstellen = input("\nMöchtest du eine Beispieldatei erstellen? (j/n): ")
        if erstellen.lower() == "j":
            erstelle_beispiel_vokabeln()
            vokabeln = lade_vokabeln()
        else:
            return

    print(f"\n✓ {len(vokabeln)} Vokabeln geladen.")

    # Lade Statistik
    statistik = lade_statistik()

    while True:
        print("\n" + "=" * 70)
        print("MENÜ")
        print("=" * 70)
        print("1. Training starten")
        print("2. Statistik anzeigen")
        print("3. Beenden")

        wahl = input("\nWähle eine Option (1-3): ")

        if wahl == "1":
            richtig, falsch = trainiere(vokabeln, statistik)

            print("\n" + "=" * 60)
            print("TRAINING BEENDET")
            print("=" * 60)
            print(f"Richtige Antworten: {richtig}")
            print(f"Falsche Antworten:  {falsch}")

            if richtig + falsch > 0:
                quote = (richtig / (richtig + falsch)) * 100
                print(f"Erfolgsquote:       {quote:.1f}%")

            print("=" * 60)

            # Speichere Statistik
            speichere_statistik(statistik)
            print("\n✓ Statistik gespeichert.")

        elif wahl == "2":
            zeige_statistik(statistik, vokabeln)

        elif wahl == "3":
            print("\n👋 Auf Wiedersehen! Viel Erfolg beim Lernen!")
            break

        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-3.")


if __name__ == "__main__":
    hauptprogramm()
