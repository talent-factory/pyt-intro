# Live-Coding Beispiele: Dateiverarbeitung

Dieses Verzeichnis enthält alle Beispiele für die Live-Coding-Session zu Dateiverarbeitung.

## Übersicht der Beispiele

### 1. Datei lesen (`01_datei_lesen.py`)

Zeigt drei verschiedene Methoden, um eine Datei zu lesen:

- Gesamte Datei auf einmal lesen mit `read()`
- Zeilenweise lesen mit `for`-Schleife
- Alle Zeilen in eine Liste mit `readlines()`

**Verwendung:**

```bash
python docs/examples/01_datei_lesen.py
```

### 2. Datei schreiben (`02_datei_schreiben.py`)

Demonstriert die verschiedenen Modi zum Schreiben:

- Modus `'w'`: Datei neu schreiben (überschreibt!)
- Modus `'a'`: An Datei anhängen

**Verwendung:**

```bash
python docs/examples/02_datei_schreiben.py
```

### 3. Fehlerbehandlung (`03_fehlerbehandlung.py`)

Zeigt, wie man mit Fehlern beim Lesen von Dateien umgeht:

- `try-except` für `FileNotFoundError`
- Benutzerfreundliche Fehlermeldungen
- Programm läuft weiter trotz Fehler

**Verwendung:**

```bash
python docs/examples/03_fehlerbehandlung.py
```

### 4. Live-Coding Beispiel (`04_live_coding_beispiel.py`)

**Das Hauptbeispiel für die gemeinsame Session!**

Kombiniert alle Konzepte:

- Datei einlesen
- Zeilen zählen
- Analyse durchführen
- Bericht in neue Datei schreiben
- Fehlerbehandlung

**Verwendung:**

```bash
python docs/examples/04_live_coding_beispiel.py
```

### 5. Encoding Demo (`05_encoding_demo.py`)

Zeigt die Wichtigkeit von `encoding='utf-8'`:

- Umlaute und Sonderzeichen
- Schweizer Zeichen (🇨🇭)
- Verschiedene Sprachen

**Verwendung:**

```bash
python docs/examples/05_encoding_demo.py
```

## Ablauf der Live-Coding-Session (15 Min)

### Phase 1: Erklärung (5 Min)

1. **`with`-Statement erklären:**

   ```python
   with open('datei.txt', 'r', encoding='utf-8') as datei:
       inhalt = datei.read()
   # Datei wird automatisch geschlossen!
   ```

2. **Modi zeigen:**
   - `'r'` - Read (Lesen)
   - `'w'` - Write (Schreiben, überschreibt!)
   - `'a'` - Append (Anhängen)

3. **Encoding betonen:**
   - Immer `encoding='utf-8'` verwenden
   - Wichtig für Umlaute (ä, ö, ü)

4. **Fehlerbehandlung:**

   ```python
   try:
       with open('datei.txt', 'r', encoding='utf-8') as datei:
           inhalt = datei.read()
   except FileNotFoundError:
       print("Datei nicht gefunden!")
   ```

### Phase 2: Live-Coding (10 Min)

**Gemeinsam programmieren:** `04_live_coding_beispiel.py`

1. **Schritt 1:** Datei lesen (3 Min)
   - `with open()` verwenden
   - Zeilen in Liste speichern
   - Anzahl ausgeben

2. **Schritt 2:** Analyse (3 Min)
   - Zeilen zählen
   - Zeichen zählen
   - Nicht-leere Zeilen zählen

3. **Schritt 3:** Bericht schreiben (4 Min)
   - Neue Datei erstellen
   - Statistiken schreiben
   - Inhalt mit Zeilennummern schreiben

**Wichtig:** Studierende sollen mittippen!

## Tipps für die Durchführung

### Vor der Session

- [ ] Alle Beispieldateien testen
- [ ] `beispiel.txt` ist vorhanden
- [ ] Beamer/Projektor bereit
- [ ] Editor mit großer Schrift

### Während der Session

- ✅ **Langsam tippen** - Studierende sollen mitkommen
- ✅ **Laut denken** - Erkläre, was du tust
- ✅ **Fehler machen** - Zeige, wie man debuggt
- ✅ **Fragen stellen** - "Was denkt ihr, passiert hier?"
- ✅ **Testen** - Führe Code regelmäßig aus

### Häufige Fragen

**Q: Warum `with`-Statement?**  
A: Datei wird automatisch geschlossen, auch bei Fehlern.

**Q: Was passiert bei Modus `'w'`?**  
A: Datei wird komplett überschrieben! Alte Inhalte gehen verloren.

**Q: Warum `encoding='utf-8'`?**  
A: Damit Umlaute (ä, ö, ü) korrekt gespeichert werden.

**Q: Was ist `strip()`?**  
A: Entfernt Leerzeichen und Zeilenumbrüche am Anfang und Ende.

## Nach der Session

Die Studierenden können:

- ✅ Dateien lesen mit verschiedenen Methoden
- ✅ Dateien schreiben und anhängen
- ✅ Fehler behandeln mit `try-except`
- ✅ `with`-Statement verwenden
- ✅ Encoding richtig setzen

## Zusätzliche Ressourcen

- Python-Dokumentation: <https://docs.python.org/de/3/tutorial/inputoutput.html#reading-and-writing-files>
- Cheat Sheet: `docs/cheat-sheet.adoc`

## Nächste Schritte

Nach dieser Session können die Studierenden mit den Aufgaben in `docs/exercises/kursabend-4-aufgaben.adoc` beginnen!
