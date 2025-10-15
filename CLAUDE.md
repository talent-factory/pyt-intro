# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projektübersicht

Deutschsprachiger Python-Einführungskurs für Programmieranfänger mit interaktiven Jupyter Notebooks, Beispielcode und Übungen.

**Zielgruppe**: Programmieranfänger ohne Vorkenntnisse
**Sprache**: Alle Inhalte auf Deutsch (Code-Kommentare, Dokumentation, Variablennamen)
**Package Manager**: uv (migriert von Poetry)

### Kursstruktur (5 Abende)

Der Kurs folgt einer didaktischen Progression:

1. **Kursabend 1-2**: Grundlagen (Variablen, Datentypen, Input/Output, Jupyter Notebooks)
2. **Kursabend 3**: Kontrollstrukturen (if/elif/else, Schleifen), Funktionen, Module
3. **Kursabend 4**: Dateiverarbeitung + Praxis-Workshop mit Übungen in 3 Levels
4. **Kursabend 5**: Mini-Projekte (Tagebuch, Quiz, Ausgaben-Tracker, Passwort-Manager)

## Befehle

### Package Management

```bash
uv sync                      # Abhängigkeiten installieren
uv run python <skript>       # Python-Skript ausführen
uv add <paketname>           # Paket hinzufügen
```

### Entwicklung

```bash
jupyter notebook             # Jupyter starten
python -m doctest <datei.py> # Doctest ausführen
python -m doctest -v <datei.py>  # Doctest verbose
```

### Code-Qualität

```bash
black <datei_oder_verzeichnis>   # Code formatieren (PEP 8)
```

## Architektur

### Verzeichnisstruktur

- **`ipynb/`** - Jupyter Notebooks (00-hello bis 03-Classes-and-Objects)
- **`docs/`** - AsciiDoc-Dokumentation, Tutorials, Übungsaufgaben
  - `cheat-sheet.adoc` - Schnellreferenz für Kursabende 4 & 5
  - `tutorials/` - Umfassende Tutorials (Doctest, Grundlagen, Module)
  - `exercises/` - Übungsaufgaben (kursabend-4-aufgaben.adoc, kursabend-5-projekte.adoc)
- **`solutions/`** - Musterlösungen für Kursabend 4 & 5
- **`testdaten/`** - Testdateien für Übungen (beispieltext.txt, produkte.csv, server.log, vokabeln.txt, quiz.txt)
- **`introcs/`** - 100+ Beispielmodule (Algorithmen, Datenstrukturen, Grafik)
- **`stdlib/`** - Hilfsmodule (stdio, stddraw, stdrandom, etc.)

### introcs-Module

Klassische CS-Beispiele für Anfänger:

- Grundprogramme (helloworld.py, useargument.py)
- Algorithmen (binarysearch.py, sortierung)
- Datenstrukturen (arraystack.py, bst.py)
- Mathematik (fibonacci, gaussian, mandelbrot)
- Grafik (turtle graphics, plotting)

**Wichtig**: Viele `introcs/`-Module importieren von `stdlib`-Paket (custom I/O-Funktionen).

### Übungen

Drei Schwierigkeitslevel (Kursabend 4):

- **Level 1**: Zahlenraten mit Highscore, Einkaufsliste, Notizen-App
- **Level 2**: Textanalyse-Tool, CSV-Verarbeitung, Log-File-Analyzer
- **Level 3**: Vokabeltrainer, Kontaktverwaltung

## Codestil-Richtlinien

### Sprache und Benennung

- **Alle Inhalte auf Deutsch**: Kommentare, Docstrings, Variablennamen, Dokumentation
- Variablen: `kleinbuchstaben_mit_unterstrichen` (z.B. `anzahl_versuche`, `ist_student`)
- Klassen: `CamelCase`
- Deutsche Namen bevorzugen (außer etablierte englische Begriffe wie `main`)

### Code-Konventionen

- **PEP 8** strikt befolgen
- **Typhinweise** verwenden: `def addiere(a: int, b: int) -> int:`
- **Docstrings** mit deutscher Beschreibung und doctest-Beispielen:

```python
def addiere(a: int, b: int) -> int:
    """
    Addiert zwei Zahlen.

    Args:
        a: Erste Zahl
        b: Zweite Zahl

    Returns:
        Summe von a und b

    >>> addiere(2, 3)
    5
    >>> addiere(-1, 1)
    0
    """
    return a + b
```

- Fehlerbehandlung mit `try-except` und spezifischen Exceptions
- Properties (`@property`) statt direktem Attributzugriff
- Funktionen klein halten (Single Responsibility)

### Pädagogische Anforderungen

Für Anfänger optimiert:

- Schrittweise Komplexität aufbauen
- Viele erklärende Kommentare
- Praktische, nachvollziehbare Beispiele
- Konsistenz mit bestehenden Notebook-Stilen
- Vermeidung fortgeschrittener Python-Features (außer in späteren Notebooks)

### Dokumentationsformate

- **Markdown** (`.md`): Frei von markdownlint-Fehlern, Leerzeilen um Überschriften/Listen/Code-Blöcke
- **AsciiDoc** (`.adoc`): Für umfangreiche Tutorials und Übungsaufgaben

### Formatierungsprobleme

Bei Markdown-Formatierungsproblemen: Nutze `markdown-syntax-formatter` Agent für automatische Korrektur.
