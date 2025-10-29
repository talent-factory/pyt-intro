"""
Einkaufsliste
Musterlösung für Kursabend 4, Aufgabe 1.2
"""


def lade_liste():
    """
    Lädt die Einkaufsliste aus der Datei.

    Returns:
        list: Liste der Artikel
    """
    try:
        with open("einkaufsliste.txt", "r", encoding="utf-8") as datei:
            artikel = []
            for zeile in datei:
                zeile = zeile.strip()
                if zeile:  # Nur nicht-leere Zeilen
                    artikel.append(zeile)
            return artikel
    except FileNotFoundError:
        return []


def speichere_liste(artikel):
    """
    Speichert die Einkaufsliste in der Datei.

    Args:
        artikel (list): Liste der Artikel
    """
    with open("einkaufsliste.txt", "w", encoding="utf-8") as datei:
        for item in artikel:
            datei.write(f"{item}\n")
    print("\n✓ Liste wurde gespeichert!")


def zeige_liste(artikel):
    """
    Zeigt die aktuelle Einkaufsliste an.

    Args:
        artikel (list): Liste der Artikel
    """
    if not artikel:
        print("\n📝 Die Einkaufsliste ist leer.")
        return

    print("\n" + "=" * 50)
    print("📝 EINKAUFSLISTE")
    print("=" * 50)
    for i, item in enumerate(artikel, 1):
        print(f"{i}. {item}")
    print("=" * 50)


def artikel_hinzufuegen(artikel):
    """
    Fügt einen neuen Artikel zur Liste hinzu.

    Args:
        artikel (list): Liste der Artikel
    """
    neuer_artikel = input("\nArtikel: ")
    if neuer_artikel:
        artikel.append(neuer_artikel)
        print(f"✓ '{neuer_artikel}' wurde hinzugefügt.")
    else:
        print("❌ Kein Artikel eingegeben.")


def artikel_loeschen(artikel):
    """
    Löscht einen Artikel aus der Liste.

    Args:
        artikel (list): Liste der Artikel
    """
    if not artikel:
        print("\n❌ Die Liste ist leer.")
        return

    zeige_liste(artikel)

    try:
        nummer = int(input("\nNummer des zu löschenden Artikels: "))
        if 1 <= nummer <= len(artikel):
            geloeschter = artikel.pop(nummer - 1)
            print(f"✓ '{geloeschter}' wurde gelöscht.")
        else:
            print("❌ Ungültige Nummer!")
    except ValueError:
        print("❌ Bitte eine Zahl eingeben!")


def zeige_menu():
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 50)
    print("=== EINKAUFSLISTE ===")
    print("=" * 50)
    print("1. Artikel hinzufügen")
    print("2. Liste anzeigen")
    print("3. Artikel löschen")
    print("4. Liste speichern")
    print("5. Liste laden")
    print("6. Beenden")
    print("=" * 50)


def hauptprogramm():
    """Hauptprogramm für die Einkaufsliste."""
    # Versuche beim Start, eine existierende Liste zu laden
    artikel = lade_liste()
    if artikel:
        print(f"✓ {len(artikel)} Artikel aus Datei geladen.")

    while True:
        zeige_menu()

        wahl = input("\nWähle eine Option (1-6): ")

        if wahl == "1":
            artikel_hinzufuegen(artikel)
        elif wahl == "2":
            zeige_liste(artikel)
        elif wahl == "3":
            artikel_loeschen(artikel)
        elif wahl == "4":
            speichere_liste(artikel)
        elif wahl == "5":
            artikel = lade_liste()
            print(f"✓ {len(artikel)} Artikel geladen.")
        elif wahl == "6":
            # Frage, ob vor dem Beenden gespeichert werden soll
            speichern = input("\nListe vor dem Beenden speichern? (j/n): ")
            if speichern.lower() == "j":
                speichere_liste(artikel)
            print("\n👋 Auf Wiedersehen!")
            break
        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-6.")


if __name__ == "__main__":
    hauptprogramm()
