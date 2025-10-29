"""
CSV-Verarbeitung
Musterlösung für Kursabend 4, Aufgabe 2.2
"""


def lese_csv(dateiname):
    """
    Liest CSV-Datei und gibt Liste von Produkten zurück.

    Args:
        dateiname (str): Pfad zur CSV-Datei

    Returns:
        list: Liste von Produkt-Dictionaries
    """
    produkte = []

    try:
        with open(dateiname, "r", encoding="utf-8") as datei:
            for zeile in datei:
                zeile = zeile.strip()
                if not zeile:  # Überspringe leere Zeilen
                    continue

                teile = zeile.split(",")

                if len(teile) != 3:
                    print(f"Warnung: Ungültige Zeile übersprungen: {zeile}")
                    continue

                try:
                    produkt = {
                        "name": teile[0].strip(),
                        "preis": float(teile[1].strip()),
                        "anzahl": int(teile[2].strip()),
                    }
                    produkte.append(produkt)
                except ValueError:
                    print(f"Warnung: Ungültige Daten in Zeile: {zeile}")
                    continue

        return produkte

    except FileNotFoundError:
        print(f"Fehler: Datei '{dateiname}' nicht gefunden!")
        return []


def berechne_statistiken(produkte):
    """
    Berechnet verschiedene Statistiken für die Produkte.

    Args:
        produkte (list): Liste von Produkt-Dictionaries

    Returns:
        dict: Dictionary mit Statistiken
    """
    if not produkte:
        return None

    # Gesamtwert aller Produkte
    gesamtwert = sum(p["preis"] * p["anzahl"] for p in produkte)

    # Durchschnittspreis
    durchschnittspreis = sum(p["preis"] for p in produkte) / len(produkte)

    # Teuerstes Produkt
    teuerstes = max(produkte, key=lambda p: p["preis"])

    # Günstigstes Produkt
    guenstigstes = min(produkte, key=lambda p: p["preis"])

    # Produkt mit höchstem Gesamtwert
    hoechster_wert = max(produkte, key=lambda p: p["preis"] * p["anzahl"])

    return {
        "gesamtwert": gesamtwert,
        "durchschnittspreis": durchschnittspreis,
        "teuerstes": teuerstes,
        "guenstigstes": guenstigstes,
        "hoechster_wert": hoechster_wert,
        "anzahl_produkte": len(produkte),
    }


def zeige_produkte(produkte):
    """
    Zeigt alle Produkte in einer formatierten Tabelle an.

    Args:
        produkte (list): Liste von Produkt-Dictionaries
    """
    if not produkte:
        print("\nKeine Produkte vorhanden.")
        return

    print("\n" + "=" * 70)
    print("PRODUKTLISTE")
    print("=" * 70)
    print(f"{'Produkt':<20} {'Preis':>10} {'Anzahl':>10} {'Gesamtwert':>15}")
    print("-" * 70)

    for p in produkte:
        gesamtwert = p["preis"] * p["anzahl"]
        print(
            f"{p['name']:<20} {p['preis']:>10.2f} {p['anzahl']:>10} {gesamtwert:>15.2f}"
        )

    print("=" * 70)


def zeige_statistiken(stats):
    """
    Zeigt die berechneten Statistiken an.

    Args:
        stats (dict): Dictionary mit Statistiken
    """
    if not stats:
        print("\nKeine Statistiken verfügbar.")
        return

    print("\n" + "=" * 70)
    print("STATISTIKEN")
    print("=" * 70)
    print(f"Anzahl Produkte:        {stats['anzahl_produkte']}")
    print(f"Gesamtwert aller Produkte: CHF {stats['gesamtwert']:.2f}")
    print(f"Durchschnittspreis:     CHF {stats['durchschnittspreis']:.2f}")
    print()
    print(
        f"Teuerstes Produkt:      {stats['teuerstes']['name']} (CHF {stats['teuerstes']['preis']:.2f})"
    )
    print(
        f"Günstigstes Produkt:    {stats['guenstigstes']['name']} (CHF {stats['guenstigstes']['preis']:.2f})"
    )
    print()
    print(f"Höchster Gesamtwert:    {stats['hoechster_wert']['name']}")
    print(
        f"  (CHF {stats['hoechster_wert']['preis']:.2f} × {stats['hoechster_wert']['anzahl']} = CHF {stats['hoechster_wert']['preis'] * stats['hoechster_wert']['anzahl']:.2f})"
    )
    print("=" * 70)


def erstelle_bericht(dateiname, produkte, stats):
    """
    Erstellt einen Bericht und speichert ihn in einer Datei.

    Args:
        dateiname (str): Name der Ausgabedatei
        produkte (list): Liste von Produkt-Dictionaries
        stats (dict): Dictionary mit Statistiken
    """
    with open(dateiname, "w", encoding="utf-8") as datei:
        datei.write("=" * 70 + "\n")
        datei.write("PRODUKTBERICHT\n")
        datei.write("=" * 70 + "\n\n")

        # Produktliste
        datei.write("PRODUKTLISTE\n")
        datei.write("-" * 70 + "\n")
        datei.write(
            f"{'Produkt':<20} {'Preis':>10} {'Anzahl':>10} {'Gesamtwert':>15}\n"
        )
        datei.write("-" * 70 + "\n")

        for p in produkte:
            gesamtwert = p["preis"] * p["anzahl"]
            datei.write(
                f"{p['name']:<20} {p['preis']:>10.2f} {p['anzahl']:>10} {gesamtwert:>15.2f}\n"
            )

        datei.write("\n")

        # Statistiken
        datei.write("STATISTIKEN\n")
        datei.write("-" * 70 + "\n")
        datei.write(f"Anzahl Produkte:           {stats['anzahl_produkte']}\n")
        datei.write(f"Gesamtwert aller Produkte: CHF {stats['gesamtwert']:.2f}\n")
        datei.write(
            f"Durchschnittspreis:        CHF {stats['durchschnittspreis']:.2f}\n"
        )
        datei.write("\n")
        datei.write(
            f"Teuerstes Produkt:         {stats['teuerstes']['name']} (CHF {stats['teuerstes']['preis']:.2f})\n"
        )
        datei.write(
            f"Günstigstes Produkt:       {stats['guenstigstes']['name']} (CHF {stats['guenstigstes']['preis']:.2f})\n"
        )
        datei.write("\n")
        datei.write(f"Höchster Gesamtwert:       {stats['hoechster_wert']['name']}\n")
        datei.write(
            f"  (CHF {stats['hoechster_wert']['preis']:.2f} × {stats['hoechster_wert']['anzahl']} = CHF {stats['hoechster_wert']['preis'] * stats['hoechster_wert']['anzahl']:.2f})\n"
        )
        datei.write("=" * 70 + "\n")

    print(f"\n✓ Bericht wurde in '{dateiname}' gespeichert.")


def erstelle_beispiel_csv():
    """Erstellt eine Beispiel-CSV-Datei zum Testen."""
    beispieldaten = """Apfel,1.50,10
Banane,0.80,15
Orange,2.00,8
Birne,1.80,12
Trauben,3.50,5
Erdbeeren,4.20,6
Kiwi,0.90,20
Mango,2.50,4"""

    with open("produkte.csv", "w", encoding="utf-8") as datei:
        datei.write(beispieldaten)

    print("✓ Beispieldatei 'produkte.csv' wurde erstellt.")


def hauptprogramm():
    """Hauptprogramm für die CSV-Verarbeitung."""
    print("=" * 70)
    print("CSV-VERARBEITUNG - PRODUKTANALYSE")
    print("=" * 70)

    dateiname = input("\nDateiname (z.B. produkte.csv): ")

    # Lese CSV-Datei
    produkte = lese_csv(dateiname)

    if not produkte:
        erstellen = input("\nMöchtest du eine Beispieldatei erstellen? (j/n): ")
        if erstellen.lower() == "j":
            erstelle_beispiel_csv()
            produkte = lese_csv("produkte.csv")
        else:
            return

    # Zeige Produkte
    zeige_produkte(produkte)

    # Berechne und zeige Statistiken
    stats = berechne_statistiken(produkte)
    zeige_statistiken(stats)

    # Bericht speichern
    speichern = input("\nBericht speichern? (j/n): ")
    if speichern.lower() == "j":
        erstelle_bericht("produktbericht.txt", produkte, stats)


if __name__ == "__main__":
    hauptprogramm()
