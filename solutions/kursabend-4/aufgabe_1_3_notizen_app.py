"""
Notizen-App
Musterlösung für Kursabend 4, Aufgabe 1.3
"""

import os
from datetime import datetime


def erstelle_notiz():
    """
    Erstellt eine neue Notiz und speichert sie mit Zeitstempel.
    """
    print("\n" + "=" * 60)
    print("NEUE NOTIZ")
    print("=" * 60)
    print("Gib deine Notiz ein (leere Zeile zum Beenden):")

    zeilen = []
    while True:
        zeile = input()
        if zeile == "":
            break
        zeilen.append(zeile)

    if not zeilen:
        print("\n❌ Keine Notiz erfasst.")
        return

    notiz = "\n".join(zeilen)

    # Erstelle Verzeichnis für Notizen, falls nicht vorhanden
    os.makedirs("notizen", exist_ok=True)

    # Erstelle Dateinamen mit Zeitstempel
    zeitstempel = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    dateiname = f"notizen/notiz_{zeitstempel}.txt"

    # Speichere Notiz
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write(f"Erstellt am: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        datei.write("=" * 60 + "\n\n")
        datei.write(notiz)
        datei.write("\n")

    print(f"\n✓ Notiz gespeichert als '{dateiname}'")


def liste_notizen():
    """
    Listet alle vorhandenen Notizen auf.

    Returns:
        list: Liste der Notiz-Dateinamen
    """
    if not os.path.exists("notizen"):
        print("\n📝 Noch keine Notizen vorhanden.")
        return []

    dateien = [f for f in os.listdir("notizen") if f.endswith(".txt")]

    if not dateien:
        print("\n📝 Noch keine Notizen vorhanden.")
        return []

    # Sortiere nach Datum (neueste zuerst)
    dateien.sort(reverse=True)

    print("\n" + "=" * 60)
    print("ALLE NOTIZEN")
    print("=" * 60)

    for i, datei in enumerate(dateien, 1):
        # Extrahiere Datum und Zeit aus Dateinamen
        # Format: notiz_YYYY-MM-DD_HH-MM-SS.txt
        teile = datei.replace("notiz_", "").replace(".txt", "").split("_")
        if len(teile) == 2:
            datum = teile[0]
            zeit = teile[1].replace("-", ":")
            print(f"{i}. {datum} {zeit}")
        else:
            print(f"{i}. {datei}")

    print("=" * 60)
    return dateien


def lese_notiz(dateien):
    """
    Liest und zeigt eine bestimmte Notiz an.

    Args:
        dateien (list): Liste der verfügbaren Notiz-Dateinamen
    """
    if not dateien:
        return

    try:
        nummer = int(input("\nWelche Notiz möchtest du lesen? (Nummer): "))
        if 1 <= nummer <= len(dateien):
            dateiname = f"notizen/{dateien[nummer - 1]}"

            with open(dateiname, "r", encoding="utf-8") as datei:
                inhalt = datei.read()

            print("\n" + "=" * 60)
            print(inhalt)
            print("=" * 60)
        else:
            print("❌ Ungültige Nummer!")
    except ValueError:
        print("❌ Bitte eine Zahl eingeben!")
    except FileNotFoundError:
        print("❌ Notiz nicht gefunden!")


def suche_notizen():
    """
    Sucht in allen Notizen nach einem Stichwort.
    """
    if not os.path.exists("notizen"):
        print("\n📝 Noch keine Notizen vorhanden.")
        return

    stichwort = input("\nStichwort: ").lower()

    dateien = [f for f in os.listdir("notizen") if f.endswith(".txt")]
    gefunden = []

    for datei in dateien:
        with open(f"notizen/{datei}", "r", encoding="utf-8") as f:
            inhalt = f.read().lower()
            if stichwort in inhalt:
                gefunden.append(datei)

    if gefunden:
        print(f"\n✓ {len(gefunden)} Notiz(en) gefunden:")
        for i, datei in enumerate(gefunden, 1):
            teile = datei.replace("notiz_", "").replace(".txt", "").split("_")
            if len(teile) == 2:
                datum = teile[0]
                zeit = teile[1].replace("-", ":")
                print(f"{i}. {datum} {zeit}")
            else:
                print(f"{i}. {datei}")
    else:
        print(f"\n❌ Keine Notizen mit '{stichwort}' gefunden.")


def zeige_menu():
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 60)
    print("=== NOTIZEN-APP ===")
    print("=" * 60)
    print("1. Neue Notiz erstellen")
    print("2. Alle Notizen anzeigen")
    print("3. Notiz lesen")
    print("4. Notizen durchsuchen")
    print("5. Beenden")
    print("=" * 60)


def hauptprogramm():
    """Hauptprogramm für die Notizen-App."""
    while True:
        zeige_menu()

        wahl = input("\nWähle eine Option (1-5): ")

        if wahl == "1":
            erstelle_notiz()
        elif wahl == "2":
            liste_notizen()
        elif wahl == "3":
            dateien = liste_notizen()
            if dateien:
                lese_notiz(dateien)
        elif wahl == "4":
            suche_notizen()
        elif wahl == "5":
            print("\n👋 Auf Wiedersehen!")
            break
        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-5.")


if __name__ == "__main__":
    hauptprogramm()
