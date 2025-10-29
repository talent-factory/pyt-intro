# Musterlösungen Kursabend 4

Dieses Verzeichnis enthält Musterlösungen für alle Aufgaben von Kursabend 4: Dateiverarbeitung und Praxis-Workshop.

## ⚠️ Wichtiger Hinweis

Diese Lösungen sind **Beispiele** und zeigen **einen** möglichen Lösungsweg. Es gibt oft mehrere richtige Wege, ein Problem zu lösen!

**Empfehlung:** Versuche zuerst selbst eine Lösung zu finden, bevor du hier nachschaust.

## Übersicht der Musterlösungen

### Level 1: Aufwärmen

Diese Aufgaben wiederholen die Grundlagen und führen sanft in die Dateiverarbeitung ein.

#### 1.1 Zahlenraten mit Highscore
**Datei:** `aufgabe_1_1_zahlenraten_highscore.py`

**Was du lernst:**
- Dateien lesen und schreiben
- Highscore-System implementieren
- Datum und Zeit verwenden
- Fehlerbehandlung mit try-except

**Besondere Features:**
- Speichert den besten Rekord mit Datum
- Zeigt beim Start den aktuellen Rekord an
- Gratuliert bei neuem Rekord

#### 1.2 Einkaufsliste
**Datei:** `aufgabe_1_2_einkaufsliste.py`

**Was du lernst:**
- Listen verwalten
- Menü-System erstellen
- Daten persistent speichern
- Benutzerinteraktion

**Besondere Features:**
- Automatisches Laden beim Start
- Sicherheitsabfrage vor dem Beenden
- Nummerierte Artikelliste

#### 1.3 Notizen-App
**Datei:** `aufgabe_1_3_notizen_app.py`

**Was du lernst:**
- Mehrere Dateien verwalten
- Zeitstempel erstellen
- Verzeichnisse erstellen
- Dateien durchsuchen

**Besondere Features:**
- Automatische Dateinamen mit Zeitstempel
- Suchfunktion über alle Notizen
- Übersichtliche Auflistung

### Level 2: Herausforderung

Diese Aufgaben kombinieren mehrere Konzepte und erfordern mehr Planung.

#### 2.1 Textanalyse-Tool
**Datei:** `aufgabe_2_1_textanalyse.py`

**Was du lernst:**
- Textdateien analysieren
- Statistiken berechnen
- Collections verwenden (Counter)
- Berichte erstellen

**Besondere Features:**
- Umfassende Textstatistiken
- Wortfrequenz-Analyse
- Formatierter Bericht
- Beispieldatei-Generator

#### 2.2 CSV-Verarbeitung
**Datei:** `aufgabe_2_2_csv_verarbeitung.py`

**Was du lernst:**
- CSV-Dateien verarbeiten
- Daten strukturieren (Dictionaries)
- Berechnungen durchführen
- Tabellarische Ausgabe

**Besondere Features:**
- Robuste CSV-Verarbeitung
- Umfangreiche Statistiken
- Formatierte Tabellen
- Beispiel-CSV-Generator

#### 2.3 Log-File-Analyzer
**Datei:** `aufgabe_2_3_log_analyzer.py`

**Was du lernst:**
- Log-Dateien durchsuchen
- Muster erkennen
- Fehler filtern
- Berichte generieren

**Besondere Features:**
- Mehrere Schlüsselwörter gleichzeitig
- Statistik mit Prozentangaben
- Separate Fehler-Datei
- Beispiel-Log-Generator

### Level 3: Für Schnelle

Diese Aufgaben sind anspruchsvoller und kombinieren alle bisherigen Konzepte.

#### 3.1 Vokabeltrainer
**Datei:** `aufgabe_3_1_vokabeltrainer.py`

**Was du lernst:**
- Intelligente Auswahl (gewichtet)
- Statistik führen
- Lernfortschritt tracken
- Adaptive Schwierigkeit

**Besondere Features:**
- Schwierige Vokabeln werden häufiger abgefragt
- Detaillierte Statistik pro Vokabel
- Erfolgsquote berechnen
- Beispiel-Vokabeln

#### 3.2 Kontaktverwaltung
**Datei:** `aufgabe_3_2_kontaktverwaltung.py`

**Was du lernst:**
- CRUD-Operationen (Create, Read, Update, Delete)
- Datenvalidierung
- Suchfunktionen
- Export-Funktionen

**Besondere Features:**
- Vollständige Kontaktverwaltung
- Intelligente Suche
- Duplikat-Prüfung
- Lesbare Export-Funktion
- Änderungs-Tracking

## Verwendung

### Programme ausführen

```bash
# Mit Python direkt
python aufgabe_1_1_zahlenraten_highscore.py

# Mit uv (empfohlen)
uv run python aufgabe_1_1_zahlenraten_highscore.py
```

### Beispieldateien

Viele Programme können automatisch Beispieldateien erstellen, wenn die benötigte Datei nicht gefunden wird. Folge einfach den Anweisungen im Programm.

## Gemeinsame Konzepte

Alle Musterlösungen verwenden:

### 1. Funktionen
Jedes Programm ist in sinnvolle Funktionen aufgeteilt:
- Eine Funktion = Eine Aufgabe
- Sprechende Funktionsnamen
- Docstrings zur Dokumentation

### 2. Fehlerbehandlung
```python
try:
    with open('datei.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```

### 3. with-Statement
Für sichere Dateiverarbeitung:
```python
with open('datei.txt', 'w', encoding='utf-8') as datei:
    datei.write("Inhalt")
# Datei wird automatisch geschlossen
```

### 4. Encoding
Immer `encoding='utf-8'` verwenden für korrekte Umlaute!

### 5. Benutzerfreundlichkeit
- Klare Menüs
- Hilfreiche Fehlermeldungen
- Bestätigungen bei kritischen Aktionen
- Visuelle Trenner (=, -)

## Tipps zum Lernen

### 1. Code lesen
Lies den Code Zeile für Zeile und versuche zu verstehen, was passiert.

### 2. Kommentare beachten
Die Docstrings und Kommentare erklären die Logik.

### 3. Experimentieren
Ändere Werte und schaue, was passiert:
- Ändere Texte
- Füge neue Funktionen hinzu
- Verbessere die Ausgabe

### 4. Debuggen
Füge `print()`-Statements ein, um zu sehen, was in Variablen steht.

### 5. Erweitern
Ideen für Erweiterungen:
- Farbige Ausgabe (mit colorama)
- Grafische Oberfläche (mit tkinter)
- Datenbank statt Textdateien (mit sqlite3)
- Web-Interface (mit Flask)

## Häufige Muster

### Datei lesen
```python
try:
    with open('datei.txt', 'r', encoding='utf-8') as datei:
        inhalt = datei.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```

### Datei schreiben
```python
with open('datei.txt', 'w', encoding='utf-8') as datei:
    datei.write("Inhalt\n")
```

### Datei zeilenweise lesen
```python
with open('datei.txt', 'r', encoding='utf-8') as datei:
    for zeile in datei:
        zeile = zeile.strip()
        print(zeile)
```

### Menü-Schleife
```python
while True:
    zeige_menu()
    wahl = input("Wähle: ")
    
    if wahl == '1':
        funktion1()
    elif wahl == '2':
        funktion2()
    elif wahl == 'q':
        break
```

## Code-Qualität

Die Musterlösungen demonstrieren:

✅ **Sprechende Namen**
```python
# Gut
anzahl_versuche = 0

# Schlecht
x = 0
```

✅ **Docstrings**
```python
def lade_highscore():
    """
    Lädt den Highscore aus der Datei.
    
    Returns:
        dict: Dictionary mit 'versuche' und 'datum'
    """
```

✅ **Fehlerbehandlung**
```python
try:
    # Kritischer Code
except FileNotFoundError:
    # Spezifische Fehlerbehandlung
```

✅ **Konstanten**
```python
DATEINAME = 'highscore.txt'
MAX_VERSUCHE = 10
```

## Unterschiede zu deiner Lösung?

Das ist völlig normal und sogar gut! Wichtig ist:

✅ Dein Code funktioniert  
✅ Dein Code ist lesbar  
✅ Du verstehst, was dein Code macht  
✅ Dein Code behandelt Fehler

Verschiedene Lösungswege zeigen Kreativität!

## Nächste Schritte

1. **Verstehen:** Stelle sicher, dass du jede Zeile verstehst
2. **Anpassen:** Ändere die Programme nach deinen Wünschen
3. **Erweitern:** Füge neue Features hinzu
4. **Kombinieren:** Kombiniere Konzepte aus verschiedenen Lösungen
5. **Eigenes Projekt:** Entwickle dein eigenes Projekt mit den gelernten Konzepten

## Fragen?

Bei Fragen zu den Musterlösungen:

1. Markiere die unklare Stelle
2. Notiere deine Frage
3. Bringe sie zum nächsten Kursabend mit
4. Oder stelle sie im Moodle-Forum

Viel Erfolg beim Lernen! 🚀

