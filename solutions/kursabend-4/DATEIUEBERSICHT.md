# Dateiübersicht - Kursabend 4

Diese Übersicht zeigt, welche Dateien von den einzelnen Programmen erstellt und verwendet werden.

## 📁 Verwendete Dateien pro Programm

### Aufgabe 1.1: Zahlenraten mit Highscore

**Programm:** `aufgabe_1_1_zahlenraten_highscore.py`

**Erstellt/Verwendet:**
- `highscore.txt` - Speichert den besten Rekord
  ```
  5
  2025-10-29 14:30:45
  ```
  - Zeile 1: Anzahl Versuche
  - Zeile 2: Datum und Zeit

---

### Aufgabe 1.2: Einkaufsliste

**Programm:** `aufgabe_1_2_einkaufsliste.py`

**Erstellt/Verwendet:**
- `einkaufsliste.txt` - Speichert die Einkaufsliste
  ```
  Milch
  Brot
  Butter
  Eier
  ```
  - Eine Zeile pro Artikel

---

### Aufgabe 1.3: Notizen-App

**Programm:** `aufgabe_1_3_notizen_app.py`

**Erstellt/Verwendet:**
- `notizen/` - Verzeichnis für alle Notizen
  - `notiz_2025-10-29_14-30-45.txt` - Einzelne Notiz mit Zeitstempel
  - `notiz_2025-10-29_15-20-10.txt` - Weitere Notiz
  - ...

**Format einer Notiz:**
```
Erstellt am: 2025-10-29 14:30:45
============================================================

Hier steht der Notiztext.
Kann mehrere Zeilen haben.
```

---

### Aufgabe 2.1: Textanalyse-Tool

**Programm:** `aufgabe_2_1_textanalyse.py`

**Erstellt/Verwendet:**
- `beispieltext.txt` - Eingabedatei (wird analysiert)
- `analyse.txt` - Ausgabedatei mit Analyseergebnis

**Beispiel analyse.txt:**
```
============================================================
TEXTANALYSE
============================================================
Datei: beispieltext.txt

Zeilen:                    42
Wörter:                    387
Zeichen:                   2145
Durchschnittliche Wortlänge: 5.5 Zeichen
Längstes Wort:             Programmierung (14 Zeichen)
Häufigstes Wort:           Python (23 mal)
============================================================
```

---

### Aufgabe 2.2: CSV-Verarbeitung

**Programm:** `aufgabe_2_2_csv_verarbeitung.py`

**Erstellt/Verwendet:**
- `produkte.csv` - Eingabedatei mit Produktdaten
  ```csv
  Apfel,1.50,10
  Banane,0.80,15
  Orange,2.00,8
  ```
  - Format: `Name,Preis,Anzahl`

- `produktbericht.txt` - Ausgabedatei mit Analyse

**Beispiel produktbericht.txt:**
```
======================================================================
PRODUKTBERICHT
======================================================================

PRODUKTLISTE
----------------------------------------------------------------------
Produkt                  Preis     Anzahl     Gesamtwert
----------------------------------------------------------------------
Apfel                     1.50         10          15.00
Banane                    0.80         15          12.00
...
```

---

### Aufgabe 2.3: Log-File-Analyzer

**Programm:** `aufgabe_2_3_log_analyzer.py`

**Erstellt/Verwendet:**
- `server.log` - Eingabedatei (Log-Datei)
  ```
  2025-10-15 10:23:45 INFO Server gestartet
  2025-10-15 10:26:01 ERROR Verbindung fehlgeschlagen
  2025-10-15 10:29:45 WARNING Speicher bei 85%
  ```

- `errors.log` - Ausgabedatei nur mit Fehlern
  ```
  ======================================================================
  FEHLERPROTOKOLL
  ======================================================================
  
  2025-10-15 10:26:01 ERROR Verbindung fehlgeschlagen
  2025-10-15 10:30:12 ERROR Datenbankverbindung verloren
  ```

- `log_bericht.txt` - Detaillierter Analysebericht

---

### Aufgabe 3.1: Vokabeltrainer

**Programm:** `aufgabe_3_1_vokabeltrainer.py`

**Erstellt/Verwendet:**
- `vokabeln.txt` - Vokabelliste
  ```
  Haus:house
  Auto:car
  Baum:tree
  Buch:book
  ```
  - Format: `Deutsch:Englisch`

- `statistik.txt` - Lernstatistik
  ```
  Haus|5|2
  Auto|3|1
  Baum|8|0
  ```
  - Format: `Deutsch|Richtig|Falsch`

---

### Aufgabe 3.2: Kontaktverwaltung

**Programm:** `aufgabe_3_2_kontaktverwaltung.py`

**Erstellt/Verwendet:**
- `kontakte.txt` - Kontaktdatenbank
  ```
  Max Mustermann|079 123 45 67|max@example.com
  Anna Schmidt|078 987 65 43|anna@example.com
  ```
  - Format: `Name|Telefon|E-Mail`

- `kontakte_export.txt` - Exportierte Kontakte (lesbar formatiert)
  ```
  ================================================================================
  KONTAKTLISTE
  ================================================================================
  
  1. Max Mustermann
     Telefon: 079 123 45 67
     E-Mail:  max@example.com
  
  2. Anna Schmidt
     Telefon: 078 987 65 43
     E-Mail:  anna@example.com
  ```

---

## 🗂️ Dateiformat-Übersicht

### Textdateien (.txt)
- **Encoding:** UTF-8 (wichtig für Umlaute!)
- **Zeilenumbrüche:** `\n`
- **Verwendung:** Einfache Daten, Listen, Berichte

### CSV-Dateien (.csv)
- **Trennzeichen:** Komma (`,`)
- **Format:** `Wert1,Wert2,Wert3`
- **Verwendung:** Tabellarische Daten

### Pipe-getrennte Dateien
- **Trennzeichen:** Pipe (`|`)
- **Format:** `Wert1|Wert2|Wert3`
- **Verwendung:** Strukturierte Daten mit mehreren Feldern
- **Vorteil:** Kommas können in Werten vorkommen

---

## 📋 Tipps zum Umgang mit Dateien

### Dateien erstellen
```python
with open('datei.txt', 'w', encoding='utf-8') as datei:
    datei.write("Inhalt\n")
```

### Dateien lesen
```python
with open('datei.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
```

### Dateien anhängen
```python
with open('datei.txt', 'a', encoding='utf-8') as datei:
    datei.write("Neuer Inhalt\n")
```

### Verzeichnisse erstellen
```python
import os
os.makedirs('verzeichnis', exist_ok=True)
```

### Dateien prüfen
```python
import os
if os.path.exists('datei.txt'):
    print("Datei existiert")
```

---

## ⚠️ Wichtige Hinweise

### Encoding
**Immer `encoding='utf-8'` verwenden!**
```python
# Richtig
with open('datei.txt', 'r', encoding='utf-8') as datei:
    ...

# Falsch (kann zu Problemen mit Umlauten führen)
with open('datei.txt', 'r') as datei:
    ...
```

### with-Statement
**Immer `with` verwenden für Dateien!**
```python
# Richtig - Datei wird automatisch geschlossen
with open('datei.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()

# Falsch - Datei muss manuell geschlossen werden
datei = open('datei.txt', 'r', encoding='utf-8')
inhalt = datei.read()
datei.close()  # Kann vergessen werden!
```

### Fehlerbehandlung
**Immer FileNotFoundError abfangen!**
```python
try:
    with open('datei.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```

---

## 🧹 Aufräumen

Nach dem Testen der Programme können folgende Dateien gelöscht werden:

```bash
# Einzelne Dateien
rm highscore.txt
rm einkaufsliste.txt
rm statistik.txt
rm kontakte.txt
rm produkte.csv
rm server.log
rm errors.log
rm vokabeln.txt

# Verzeichnisse
rm -rf notizen/

# Berichte
rm analyse.txt
rm produktbericht.txt
rm log_bericht.txt
rm kontakte_export.txt
```

Oder einfach alle auf einmal:
```bash
# Vorsicht: Löscht alle Testdateien!
rm -f *.txt *.csv *.log
rm -rf notizen/
```

---

## 📚 Weiterführende Informationen

### Python-Dokumentation
- [Dateiverarbeitung](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)
- [os-Modul](https://docs.python.org/3/library/os.html)
- [pathlib](https://docs.python.org/3/library/pathlib.html) (moderne Alternative)

### Best Practices
- Immer UTF-8 Encoding verwenden
- Immer with-Statement verwenden
- Immer Fehlerbehandlung implementieren
- Relative Pfade bevorzugen
- Verzeichnisse vor dem Schreiben erstellen

