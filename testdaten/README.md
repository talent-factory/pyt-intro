# Testdaten für Kursabende 4 & 5

Dieses Verzeichnis enthält Testdaten für die Übungsaufgaben der Kursabende 4 und 5.

## Verfügbare Dateien

### beispieltext.txt

Beispieltext über Python für die Textanalyse-Aufgabe.

**Verwendung:** Aufgabe 2.1 - Textanalyse-Tool

### produkte.csv

CSV-Datei mit Produktdaten (Name, Preis, Anzahl).

**Format:**

```csv
Name,Preis,Anzahl
Apfel,1.50,10
```

**Verwendung:** Aufgabe 2.2 - CSV-Verarbeitung

### server.log

Beispiel-Log-Datei eines Servers mit verschiedenen Log-Levels (INFO, WARNING, ERROR).

**Verwendung:** Aufgabe 2.3 - Log-File-Analyzer

### vokabeln.txt

Deutsch-Englisch Vokabeln für den Vokabeltrainer.

**Format:**

```text
Deutsch:Englisch
Haus:house
```

**Verwendung:** Aufgabe 3.1 - Vokabeltrainer

### quiz.txt

Quiz-Fragen mit Multiple-Choice-Antworten.

**Format:**

```text
Frage?
A) Antwort 1
B) Antwort 2
C) Antwort 3
D) Antwort 4
B
---
```

**Verwendung:** Projekt 3 - Quiz-Generator (Kursabend 5)

## Verwendung

Kopiere die benötigten Dateien in dein Arbeitsverzeichnis oder passe die Pfade in deinem Code entsprechend an.

**Beispiel:**

```python
# Wenn Testdaten im gleichen Verzeichnis
with open('beispieltext.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()

# Wenn Testdaten in Unterverzeichnis
with open('testdaten/beispieltext.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
```
