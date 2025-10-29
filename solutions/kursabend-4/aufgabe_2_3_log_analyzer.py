"""
Log-File-Analyzer
Musterlösung für Kursabend 4, Aufgabe 2.3
"""


def lese_log_datei(dateiname):
    """
    Liest eine Log-Datei und gibt alle Zeilen zurück.

    Args:
        dateiname (str): Pfad zur Log-Datei

    Returns:
        list: Liste aller Zeilen
    """
    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            return datei.readlines()
    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden!")
        return []


def analysiere_logs(zeilen, schluesselwoerter):
    """
    Analysiert Log-Zeilen nach bestimmten Schlüsselwörtern.

    Args:
        zeilen (list): Liste aller Log-Zeilen
        schluesselwoerter (list): Liste der zu suchenden Schlüsselwörter

    Returns:
        dict: Dictionary mit Analyseergebnissen
    """
    ergebnisse = {}

    for wort in schluesselwoerter:
        ergebnisse[wort] = {"anzahl": 0, "zeilen": []}

    for zeile in zeilen:
        zeile = zeile.strip()
        if not zeile:
            continue

        for wort in schluesselwoerter:
            if wort in zeile:
                ergebnisse[wort]["anzahl"] += 1
                ergebnisse[wort]["zeilen"].append(zeile)

    return ergebnisse


def zeige_analyse(ergebnisse):
    """
    Zeigt die Analyseergebnisse an.

    Args:
        ergebnisse (dict): Dictionary mit Analyseergebnissen
    """
    print("\n" + "=" * 70)
    print("LOG-ANALYSE ERGEBNISSE")
    print("=" * 70)

    for wort, daten in ergebnisse.items():
        print(f"\n{wort}: {daten['anzahl']} Vorkommen")

        if daten["zeilen"]:
            print("-" * 70)
            for zeile in daten["zeilen"][:5]:  # Zeige max. 5 Beispiele
                print(f"  {zeile}")

            if len(daten["zeilen"]) > 5:
                print(f"  ... und {len(daten['zeilen']) - 5} weitere")

    print("=" * 70)


def speichere_fehler(zeilen, ausgabedatei="errors.log"):
    """
    Speichert nur die Fehlerzeilen in einer separaten Datei.

    Args:
        zeilen (list): Liste aller Log-Zeilen
        ausgabedatei (str): Name der Ausgabedatei
    """
    fehler_zeilen = [z for z in zeilen if "ERROR" in z]

    if not fehler_zeilen:
        print("\n✓ Keine Fehler gefunden.")
        return

    with open(ausgabedatei, "w", encoding="utf-8") as datei:
        datei.write("=" * 70 + "\n")
        datei.write("FEHLERPROTOKOLL\n")
        datei.write("=" * 70 + "\n\n")

        for zeile in fehler_zeilen:
            datei.write(zeile)
            if not zeile.endswith("\n"):
                datei.write("\n")

    print(
        f"\n✓ {len(fehler_zeilen)} Fehlerzeile(n) wurden in '{ausgabedatei}' gespeichert."
    )


def erstelle_bericht(ergebnisse, ausgabedatei="log_bericht.txt"):
    """
    Erstellt einen detaillierten Bericht der Analyse.

    Args:
        ergebnisse (dict): Dictionary mit Analyseergebnissen
        ausgabedatei (str): Name der Ausgabedatei
    """
    with open(ausgabedatei, "w", encoding="utf-8") as datei:
        datei.write("=" * 70 + "\n")
        datei.write("LOG-ANALYSE BERICHT\n")
        datei.write("=" * 70 + "\n\n")

        # Zusammenfassung
        datei.write("ZUSAMMENFASSUNG\n")
        datei.write("-" * 70 + "\n")
        for wort, daten in ergebnisse.items():
            datei.write(f"{wort}: {daten['anzahl']} Vorkommen\n")

        datei.write("\n")

        # Details
        datei.write("DETAILS\n")
        datei.write("=" * 70 + "\n\n")

        for wort, daten in ergebnisse.items():
            datei.write(f"\n{wort} ({daten['anzahl']} Vorkommen)\n")
            datei.write("-" * 70 + "\n")

            if daten["zeilen"]:
                for zeile in daten["zeilen"]:
                    datei.write(f"{zeile}\n")
            else:
                datei.write("Keine Vorkommen gefunden.\n")

            datei.write("\n")

        datei.write("=" * 70 + "\n")

    print(f"\n✓ Bericht wurde in '{ausgabedatei}' gespeichert.")


def erstelle_beispiel_log():
    """Erstellt eine Beispiel-Log-Datei zum Testen."""
    beispieldaten = """2025-10-15 10:23:45 INFO Server gestartet
2025-10-15 10:24:12 INFO Verbindung hergestellt
2025-10-15 10:25:33 WARNING Langsame Antwortzeit
2025-10-15 10:26:01 ERROR Verbindung fehlgeschlagen
2025-10-15 10:27:15 INFO Neustart erfolgreich
2025-10-15 10:28:22 INFO Benutzer angemeldet: user123
2025-10-15 10:29:45 WARNING Speicher bei 85%
2025-10-15 10:30:12 ERROR Datenbankverbindung verloren
2025-10-15 10:31:33 INFO Verbindung wiederhergestellt
2025-10-15 10:32:01 ERROR Timeout bei Anfrage
2025-10-15 10:33:15 WARNING Hohe CPU-Auslastung
2025-10-15 10:34:22 INFO Backup gestartet
2025-10-15 10:35:45 INFO Backup abgeschlossen
2025-10-15 10:36:12 ERROR Schreibfehler in Datei
2025-10-15 10:37:33 WARNING Festplatte fast voll
2025-10-15 10:38:01 INFO Bereinigung durchgeführt
2025-10-15 10:39:15 INFO System läuft normal"""

    with open("server.log", "w", encoding="utf-8") as datei:
        datei.write(beispieldaten)

    print("✓ Beispieldatei 'server.log' wurde erstellt.")


def zeige_statistik(zeilen, ergebnisse):
    """
    Zeigt eine Statistik-Übersicht an.

    Args:
        zeilen (list): Liste aller Log-Zeilen
        ergebnisse (dict): Dictionary mit Analyseergebnissen
    """
    print("\n" + "=" * 70)
    print("STATISTIK")
    print("=" * 70)
    print(f"Gesamtanzahl Zeilen: {len(zeilen)}")
    print()

    for wort, daten in ergebnisse.items():
        prozent = (daten["anzahl"] / len(zeilen) * 100) if len(zeilen) > 0 else 0
        print(f"{wort:15} {daten['anzahl']:5} ({prozent:5.1f}%)")

    print("=" * 70)


def hauptprogramm():
    """Hauptprogramm für den Log-Analyzer."""
    print("=" * 70)
    print("LOG-FILE-ANALYZER")
    print("=" * 70)

    dateiname = input("\nLog-Dateiname (z.B. server.log): ")

    # Lese Log-Datei
    zeilen = lese_log_datei(dateiname)

    if not zeilen:
        erstellen = input("\nMöchtest du eine Beispieldatei erstellen? (j/n): ")
        if erstellen.lower() == "j":
            erstelle_beispiel_log()
            zeilen = lese_log_datei("server.log")
        else:
            return

    # Definiere Schlüsselwörter
    schluesselwoerter = ["ERROR", "WARNING", "INFO"]

    # Analysiere Logs
    ergebnisse = analysiere_logs(zeilen, schluesselwoerter)

    # Zeige Ergebnisse
    zeige_analyse(ergebnisse)
    zeige_statistik(zeilen, ergebnisse)

    # Speichere Fehler
    speichere_fehler(zeilen)

    # Bericht erstellen
    bericht = input("\nDetaillierten Bericht erstellen? (j/n): ")
    if bericht.lower() == "j":
        erstelle_bericht(ergebnisse)


if __name__ == "__main__":
    hauptprogramm()
