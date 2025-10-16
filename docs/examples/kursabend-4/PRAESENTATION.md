# Präsentations-Skript: Dateiverarbeitung (15 Min)

## Zeitplan

| Zeit | Aktivität | Datei |
|------|-----------|-------|
| 0-5 Min | Theorie-Input | Whiteboard + Code-Snippets |
| 5-15 Min | Live-Coding | `04_live_coding_beispiel.py` |

---

## Teil 1: Theorie-Input (5 Min)

### 1. Das `with`-Statement (1 Min)

**Am Whiteboard zeichnen:**

```text
┌─────────────────────────────────────┐
│  with open('datei.txt', 'r') as f:  │
│      inhalt = f.read()              │
│                                     │
│  # Datei automatisch geschlossen!   │
└─────────────────────────────────────┘
```

**Sagen:**
> "Das `with`-Statement ist wie ein Sicherheitsnetz. Es stellt sicher, dass die Datei immer geschlossen wird - auch wenn ein Fehler auftritt. Ihr müsst euch nicht darum kümmern!"

**Zeigen:** `01_datei_lesen.py` (kurz durchscrollen)

---

### 2. Die drei Modi (2 Min)

**Am Whiteboard:**

```text
┌──────┬─────────────────────────────────┐
│ 'r'  │ Read    - Lesen                 │
│ 'w'  │ Write   - Schreiben (VORSICHT!) │
│ 'a'  │ Append  - Anhängen              │
└──────┴─────────────────────────────────┘
```

**Demonstrieren:** `02_datei_schreiben.py`

```bash
python docs/examples/02_datei_schreiben.py
```

**Betonen:**
> "⚠️ WICHTIG: Modus 'w' überschreibt die komplette Datei! Alle alten Inhalte sind weg. Wenn ihr nur anhängen wollt, nutzt 'a'."

**Frage ans Publikum:**
> "Was denkt ihr, passiert wenn ich eine Datei mit 'w' öffne, die schon existiert?"

---

### 3. Encoding (1 Min)

**Am Whiteboard:**

```
encoding='utf-8'  ✅

Warum?
→ Umlaute: ä, ö, ü
→ Sonderzeichen: €, ©, ™
→ Emoji: 🇨🇭, 😊
```

**Demonstrieren:** `05_encoding_demo.py`

```bash
python docs/examples/05_encoding_demo.py
```

**Sagen:**
> "In der Schweiz haben wir Umlaute. Ohne UTF-8 werden die falsch dargestellt. Merkt euch: IMMER `encoding='utf-8'` verwenden!"

---

### 4. Fehlerbehandlung (1 Min)

**Am Whiteboard:**

```python
try:
    with open('datei.txt', 'r') as f:
        inhalt = f.read()
except FileNotFoundError:
    print("Datei nicht gefunden!")
```

**Demonstrieren:** `03_fehlerbehandlung.py`

```bash
python docs/examples/03_fehlerbehandlung.py
# Eingabe: nicht_existiert.txt
# Dann: beispiel.txt
```

**Sagen:**
> "Dateien können fehlen, umbenannt oder gelöscht worden sein. Mit `try-except` stürzt euer Programm nicht ab, sondern zeigt eine hilfreiche Fehlermeldung."

---

## Teil 2: Live-Coding (10 Min)

### Vorbereitung

**Sagen:**
> "Jetzt programmieren wir gemeinsam ein kleines Programm. Bitte tippt mit! Es ist wichtig, dass ihr selbst tippt - nur so lernt ihr die Syntax."

**Ziel zeigen:**
> "Wir wollen eine Textdatei einlesen, analysieren (Zeilen zählen, Zeichen zählen) und einen Bericht in eine neue Datei schreiben."

---

### Schritt 1: Grundgerüst (2 Min)

**Neue Datei erstellen:** `live_demo.py`

```python
"""
Live-Demo: Textdatei analysieren
"""

def analysiere_datei(dateiname):
    """Analysiert eine Textdatei."""
    # Hier kommt unser Code hin
    pass

# Hauptprogramm
if __name__ == '__main__':
    analysiere_datei('beispiel.txt')
```

**Ausführen:**

```bash
python live_demo.py
```

**Sagen:**
> "Noch passiert nichts. Jetzt füllen wir die Funktion."

---

### Schritt 2: Datei lesen (2 Min)

```python
def analysiere_datei(dateiname):
    """Analysiert eine Textdatei."""
    # Datei lesen
    with open(dateiname, 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()
    
    print(f"Datei gelesen: {len(zeilen)} Zeilen")
```

**Ausführen:**

```bash
python live_demo.py
```

**Fragen:**
> "Was seht ihr? Wie viele Zeilen hat unsere Datei?"

---

### Schritt 3: Analyse (2 Min)

```python
def analysiere_datei(dateiname):
    """Analysiert eine Textdatei."""
    # Datei lesen
    with open(dateiname, 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()
    
    # Analyse
    anzahl_zeilen = len(zeilen)
    anzahl_zeichen = sum(len(zeile) for zeile in zeilen)
    
    print(f"Zeilen: {anzahl_zeilen}")
    print(f"Zeichen: {anzahl_zeichen}")
```

**Ausführen und erklären:**
> "Die Funktion `sum()` addiert alle Längen. Für jede Zeile nehmen wir `len(zeile)` und addieren alles zusammen."

---

### Schritt 4: Bericht schreiben (3 Min)

```python
def analysiere_datei(dateiname):
    """Analysiert eine Textdatei."""
    # Datei lesen
    with open(dateiname, 'r', encoding='utf-8') as datei:
        zeilen = datei.readlines()
    
    # Analyse
    anzahl_zeilen = len(zeilen)
    anzahl_zeichen = sum(len(zeile) for zeile in zeilen)
    
    print(f"Zeilen: {anzahl_zeilen}")
    print(f"Zeichen: {anzahl_zeichen}")
    
    # Bericht schreiben
    with open('bericht.txt', 'w', encoding='utf-8') as datei:
        datei.write("TEXTANALYSE-BERICHT\n")
        datei.write("=" * 40 + "\n")
        datei.write(f"Datei: {dateiname}\n")
        datei.write(f"Zeilen: {anzahl_zeilen}\n")
        datei.write(f"Zeichen: {anzahl_zeichen}\n")
    
    print("\n✓ Bericht wurde in 'bericht.txt' gespeichert!")
```

**Ausführen:**

```bash
python live_demo.py
```

**Dann Bericht öffnen und zeigen:**

```bash
cat bericht.txt
# oder im Editor öffnen
```

**Sagen:**
> "Seht ihr? Wir haben eine Datei gelesen, analysiert und einen Bericht erstellt. Das ist die Grundlage für viele praktische Anwendungen!"

---

### Schritt 5: Fehlerbehandlung hinzufügen (1 Min)

```python
def analysiere_datei(dateiname):
    """Analysiert eine Textdatei."""
    try:
        # Datei lesen
        with open(dateiname, 'r', encoding='utf-8') as datei:
            zeilen = datei.readlines()
        
        # ... rest des Codes ...
        
    except FileNotFoundError:
        print(f"❌ Datei '{dateiname}' nicht gefunden!")
```

**Testen mit falscher Datei:**

```python
if __name__ == '__main__':
    analysiere_datei('gibt_es_nicht.txt')
```

**Sagen:**
> "Jetzt stürzt das Programm nicht mehr ab, sondern zeigt eine hilfreiche Meldung!"

---

## Abschluss (1 Min)

**Zusammenfassung am Whiteboard:**

```text
✅ with-Statement verwenden
✅ Modi kennen: 'r', 'w', 'a'
✅ encoding='utf-8' nicht vergessen
✅ Fehler behandeln mit try-except
```

**Sagen:**
> "Das war's! Ihr habt jetzt alles, was ihr für die Übungen braucht. Die Beispiele findet ihr in `docs/examples/`. Jetzt seid ihr dran - viel Erfolg beim Üben!"

**Überleitung zu Übungen:**
> "Öffnet jetzt bitte die Aufgaben in `docs/exercises/kursabend-4-aufgaben.adoc`. Beginnt mit Level 1, Aufgabe 1.1. Wenn ihr Fragen habt, meldet euch!"

---

## Tipps für die Durchführung

### Vor dem Start

- [ ] Alle Beispieldateien getestet
- [ ] `beispiel.txt` ist vorhanden
- [ ] Editor mit großer Schrift (min. 16pt)
- [ ] Terminal-Schrift groß genug
- [ ] Whiteboard/Flipchart bereit

### Während der Präsentation

- ✅ **Langsam tippen** - Studierende brauchen Zeit
- ✅ **Laut denken** - "Jetzt öffne ich die Datei..."
- ✅ **Fehler zeigen** - Mache absichtlich einen Fehler und korrigiere ihn
- ✅ **Fragen stellen** - Halte Studierende aktiv
- ✅ **Pausen machen** - Nach jedem Schritt kurz warten

### Häufige Stolpersteine

**Problem:** Studierende kommen nicht mit beim Tippen  
**Lösung:** Langsamer tippen, nach jedem Block warten

**Problem:** Encoding-Fehler  
**Lösung:** Zeige den Fehler, dann die Lösung mit `encoding='utf-8'`

**Problem:** Datei nicht gefunden  
**Lösung:** Erkläre relative Pfade, zeige `ls` oder `dir`

**Problem:** Einrückungsfehler  
**Lösung:** Betone die Wichtigkeit von korrekter Einrückung

### Nach der Session

- [ ] Frage, ob alles klar ist
- [ ] Zeige nochmal, wo die Beispiele sind
- [ ] Erinnere an Cheat Sheet
- [ ] Starte die Übungsphase

---

## Backup-Plan

Falls die Zeit knapp wird:

1. **Kürze Schritt 4:** Schreibe nur 2-3 Zeilen in den Bericht
2. **Überspringe Schritt 5:** Fehlerbehandlung nur erwähnen
3. **Zeige fertiges Beispiel:** `04_live_coding_beispiel.py` ausführen

Falls Zeit übrig ist:

1. **Zeige weitere Beispiele:** `01_datei_lesen.py`, `02_datei_schreiben.py`
2. **Frage-Runde:** Gibt es Fragen?
3. **Erste Aufgabe gemeinsam:** Beginne Aufgabe 1.1 gemeinsam

---

## Erfolg messen

Die Session war erfolgreich, wenn die Studierenden:

- ✅ Verstehen, was das `with`-Statement macht
- ✅ Die drei Modi unterscheiden können
- ✅ Wissen, warum `encoding='utf-8'` wichtig ist
- ✅ Eine einfache Datei lesen und schreiben können
- ✅ Motiviert sind, mit den Übungen zu beginnen

**Viel Erfolg! 🚀**
