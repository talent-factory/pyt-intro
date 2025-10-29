"""
Kontaktverwaltung
Musterlösung für Kursabend 4, Aufgabe 3.2
"""


def lade_kontakte(dateiname="kontakte.txt"):
    """
    Lädt Kontakte aus einer Datei.

    Args:
        dateiname (str): Pfad zur Kontaktdatei

    Returns:
        list: Liste von Kontakt-Dictionaries
    """
    kontakte = []

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if not zeile or "|" not in zeile:
                    continue

                teile = zeile.split("|")
                if len(teile) == 3:
                    kontakte.append(
                        {
                            "name": teile[0].strip(),
                            "telefon": teile[1].strip(),
                            "email": teile[2].strip(),
                        }
                    )

        return kontakte

    except FileNotFoundError:
        return []


def speichere_kontakte(kontakte, dateiname="kontakte.txt"):
    """
    Speichert Kontakte in einer Datei.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
        dateiname (str): Pfad zur Kontaktdatei
    """
    with open(dateiname, "w", encoding="utf-8") as datei:
        for kontakt in kontakte:
            datei.write(f"{kontakt['name']}|{kontakt['telefon']}|{kontakt['email']}\n")

    print("\n✓ Kontakte gespeichert.")


def zeige_kontakte(kontakte):
    """
    Zeigt alle Kontakte an.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
    """
    if not kontakte:
        print("\n📇 Keine Kontakte vorhanden.")
        return

    print("\n" + "=" * 80)
    print("ALLE KONTAKTE")
    print("=" * 80)
    print(f"{'Nr.':<5} {'Name':<25} {'Telefon':<20} {'E-Mail':<30}")
    print("-" * 80)

    for i, kontakt in enumerate(kontakte, 1):
        print(
            f"{i:<5} {kontakt['name']:<25} {kontakt['telefon']:<20} {kontakt['email']:<30}"
        )

    print("=" * 80)
    print(f"Gesamt: {len(kontakte)} Kontakt(e)")


def kontakt_hinzufuegen(kontakte):
    """
    Fügt einen neuen Kontakt hinzu.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
    """
    print("\n" + "=" * 60)
    print("NEUER KONTAKT")
    print("=" * 60)

    name = input("Name: ").strip()
    if not name:
        print("❌ Name darf nicht leer sein!")
        return

    # Prüfe, ob Kontakt bereits existiert
    for kontakt in kontakte:
        if kontakt["name"].lower() == name.lower():
            print(f"❌ Kontakt '{name}' existiert bereits!")
            return

    telefon = input("Telefon: ").strip()
    email = input("E-Mail: ").strip()

    kontakte.append({"name": name, "telefon": telefon, "email": email})

    print(f"\n✓ Kontakt '{name}' wurde hinzugefügt.")


def kontakt_suchen(kontakte):
    """
    Sucht einen Kontakt nach Name.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries

    Returns:
        list: Liste gefundener Kontakte
    """
    suchbegriff = input("\nSuchbegriff (Name): ").strip().lower()

    if not suchbegriff:
        print("❌ Suchbegriff darf nicht leer sein!")
        return []

    gefunden = [k for k in kontakte if suchbegriff in k["name"].lower()]

    if gefunden:
        print(f"\n✓ {len(gefunden)} Kontakt(e) gefunden:")
        print("\n" + "=" * 80)
        print(f"{'Nr.':<5} {'Name':<25} {'Telefon':<20} {'E-Mail':<30}")
        print("-" * 80)

        for i, kontakt in enumerate(gefunden, 1):
            print(
                f"{i:<5} {kontakt['name']:<25} {kontakt['telefon']:<20} {kontakt['email']:<30}"
            )

        print("=" * 80)
    else:
        print(f"\n❌ Kein Kontakt mit '{suchbegriff}' gefunden.")

    return gefunden


def kontakt_bearbeiten(kontakte):
    """
    Bearbeitet einen existierenden Kontakt.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
    """
    if not kontakte:
        print("\n❌ Keine Kontakte vorhanden.")
        return

    gefunden = kontakt_suchen(kontakte)

    if not gefunden:
        return

    if len(gefunden) == 1:
        kontakt = gefunden[0]
    else:
        try:
            nr = int(input("\nWelchen Kontakt möchtest du bearbeiten? (Nummer): "))
            if 1 <= nr <= len(gefunden):
                kontakt = gefunden[nr - 1]
            else:
                print("❌ Ungültige Nummer!")
                return
        except ValueError:
            print("❌ Bitte eine Zahl eingeben!")
            return

    print("\n" + "=" * 60)
    print(f"KONTAKT BEARBEITEN: {kontakt['name']}")
    print("=" * 60)
    print("(Leer lassen, um Wert beizubehalten)")

    neuer_name = input(f"Name [{kontakt['name']}]: ").strip()
    neues_telefon = input(f"Telefon [{kontakt['telefon']}]: ").strip()
    neue_email = input(f"E-Mail [{kontakt['email']}]: ").strip()

    # Aktualisiere nur, wenn neue Werte eingegeben wurden
    if neuer_name:
        kontakt["name"] = neuer_name
    if neues_telefon:
        kontakt["telefon"] = neues_telefon
    if neue_email:
        kontakt["email"] = neue_email

    print(f"\n✓ Kontakt '{kontakt['name']}' wurde aktualisiert.")


def kontakt_loeschen(kontakte):
    """
    Löscht einen Kontakt.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
    """
    if not kontakte:
        print("\n❌ Keine Kontakte vorhanden.")
        return

    gefunden = kontakt_suchen(kontakte)

    if not gefunden:
        return

    if len(gefunden) == 1:
        kontakt = gefunden[0]
    else:
        try:
            nr = int(input("\nWelchen Kontakt möchtest du löschen? (Nummer): "))
            if 1 <= nr <= len(gefunden):
                kontakt = gefunden[nr - 1]
            else:
                print("❌ Ungültige Nummer!")
                return
        except ValueError:
            print("❌ Bitte eine Zahl eingeben!")
            return

    # Sicherheitsabfrage
    bestaetigung = input(f"\nMöchtest du '{kontakt['name']}' wirklich löschen? (j/n): ")

    if bestaetigung.lower() == "j":
        kontakte.remove(kontakt)
        print(f"\n✓ Kontakt '{kontakt['name']}' wurde gelöscht.")
    else:
        print("\n❌ Löschen abgebrochen.")


def exportiere_kontakte(kontakte):
    """
    Exportiert Kontakte in eine lesbare Textdatei.

    Args:
        kontakte (list): Liste von Kontakt-Dictionaries
    """
    if not kontakte:
        print("\n❌ Keine Kontakte zum Exportieren vorhanden.")
        return

    ausgabedatei = "kontakte_export.txt"

    with open(ausgabedatei, "w", encoding="utf-8") as datei:
        datei.write("=" * 80 + "\n")
        datei.write("KONTAKTLISTE\n")
        datei.write("=" * 80 + "\n\n")

        for i, kontakt in enumerate(kontakte, 1):
            datei.write(f"{i}. {kontakt['name']}\n")
            datei.write(f"   Telefon: {kontakt['telefon']}\n")
            datei.write(f"   E-Mail:  {kontakt['email']}\n")
            datei.write("\n")

        datei.write("=" * 80 + "\n")
        datei.write(f"Gesamt: {len(kontakte)} Kontakt(e)\n")

    print(f"\n✓ {len(kontakte)} Kontakt(e) wurden in '{ausgabedatei}' exportiert.")


def erstelle_beispiel_kontakte():
    """Erstellt Beispiel-Kontakte zum Testen."""
    beispieldaten = """Max Mustermann|079 123 45 67|max@example.com
Anna Schmidt|078 987 65 43|anna@example.com
Peter Müller|076 555 12 34|peter@example.com
Lisa Weber|077 444 56 78|lisa@example.com"""

    with open("kontakte.txt", "w", encoding="utf-8") as datei:
        datei.write(beispieldaten)

    print("✓ Beispieldatei 'kontakte.txt' wurde erstellt.")


def zeige_menu():
    """Zeigt das Hauptmenü an."""
    print("\n" + "=" * 60)
    print("KONTAKTVERWALTUNG")
    print("=" * 60)
    print("1. Kontakt hinzufügen")
    print("2. Kontakt suchen")
    print("3. Kontakt bearbeiten")
    print("4. Kontakt löschen")
    print("5. Alle Kontakte anzeigen")
    print("6. Kontakte exportieren")
    print("7. Speichern")
    print("8. Beenden")
    print("=" * 60)


def hauptprogramm():
    """Hauptprogramm für die Kontaktverwaltung."""
    # Lade Kontakte beim Start
    kontakte = lade_kontakte()

    if kontakte:
        print(f"✓ {len(kontakte)} Kontakt(e) geladen.")
    else:
        print("Noch keine Kontakte vorhanden.")
        erstellen = input("Möchtest du Beispiel-Kontakte erstellen? (j/n): ")
        if erstellen.lower() == "j":
            erstelle_beispiel_kontakte()
            kontakte = lade_kontakte()

    geaendert = False  # Flag, um zu tracken, ob Änderungen vorgenommen wurden

    while True:
        zeige_menu()

        wahl = input("\nWähle eine Option (1-8): ")

        if wahl == "1":
            kontakt_hinzufuegen(kontakte)
            geaendert = True
        elif wahl == "2":
            kontakt_suchen(kontakte)
        elif wahl == "3":
            kontakt_bearbeiten(kontakte)
            geaendert = True
        elif wahl == "4":
            kontakt_loeschen(kontakte)
            geaendert = True
        elif wahl == "5":
            zeige_kontakte(kontakte)
        elif wahl == "6":
            exportiere_kontakte(kontakte)
        elif wahl == "7":
            speichere_kontakte(kontakte)
            geaendert = False
        elif wahl == "8":
            if geaendert:
                speichern = input("\nÄnderungen speichern? (j/n): ")
                if speichern.lower() == "j":
                    speichere_kontakte(kontakte)
            print("\n👋 Auf Wiedersehen!")
            break
        else:
            print("\n❌ Ungültige Eingabe! Bitte wähle 1-8.")


if __name__ == "__main__":
    hauptprogramm()
