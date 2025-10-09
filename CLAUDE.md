# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Projektübersicht

Dies ist ein deutschsprachiger Python-Einführungskurs mit interaktiven Jupyter Notebooks und Beispielcode. Das Projekt verwendet **uv** als Package Manager (migriert von Poetry).

**Zielgruppe**: Programmieranfänger
**Sprache**: Alle Inhalte, Kommentare und Dokumentation sind auf Deutsch

### Projektstruktur

- `ipynb/` - Jupyter Notebooks mit Tutorial-Inhalten:
  - `00-hello.ipynb` - Einstieg
  - `01-Introduction-to-Python.ipynb` - Grundlagen (Variablen, Datentypen, Kontrollstrukturen)
  - `02-Functions-and-Modules.ipynb` - Funktionen und Module
  - `03-Classes-and-Objects.ipynb` - Objektorientierte Programmierung
- `introcs/` - Beispielcode-Sammlung (100+ Module): Algorithmen, Datenstrukturen, grafische Beispiele
- `exercise/` - Übungsaufgaben (`.adoc` Format) und Lösungen
- `docs/` - Zusätzliche Dokumentation und Tutorials (AsciiDoc und HTML)
- `stdlib/` - Hilfsmodule für Standardfunktionalität

## Befehle

### Package Management (uv)

- Abhängigkeiten installieren: `uv sync`
- Python-Skript ausführen: `uv run python <skript_pfad>`
- Paket hinzufügen: `uv add <paketname>`

### Entwicklung

- Jupyter Notebook starten: `jupyter notebook` (oder direkt `uv run jupyter notebook`)
- Python-Skript direkt ausführen: `python <skript_pfad>` (wenn venv aktiviert)
- Modul als Skript ausführen: `python -m <modulname>`
- Doctest ausführen: `python -m doctest <datei.py>` oder `python -m doctest -v <datei.py>` für verbose

### Formatierung

- Code formatieren: `black <datei_oder_verzeichnis>`
- Linting würde normalerweise mit `ruff` erfolgen (nicht in pyproject.toml konfiguriert)

## Architektur und Besonderheiten

### Tutorial-Notebooks

Die Jupyter Notebooks folgen einer didaktischen Progression:

1. Grundkonzepte (Variablen, Operatoren, Datentypen)
2. Kontrollstrukturen (Bedingungen, Schleifen)
3. Funktionen und Module
4. Objektorientierung

Notebooks enthalten:

- Markdown-Zellen mit deutschen Erklärungen
- Code-Zellen mit ausführbaren Beispielen
- Referenzen zur offiziellen Python-Dokumentation

### introcs-Module

Die `introcs/`-Sammlung enthält klassische CS-Beispiele:

- Grundlegende Programme (`helloworld.py`, `useargument.py`)
- Algorithmen (Sortierung, Suche, Rekursion)
- Datenstrukturen (Stack, Queue, BST, Hash Table)
- Mathematische/wissenschaftliche Beispiele (Fibonacci, Gaussian, Mandelbrot)
- Grafik/Visualisierung (Turtle Graphics, Plotting)

Viele Module importieren von einem benutzerdefinierten `stdlib`-Paket.

### Übungen

Übungsaufgaben sind in AsciiDoc (`.adoc`) geschrieben und behandeln praktische Anwendungen wie Palindrome, Textanalyse, Einkaufswagen-Simulation.

## Richtlinien zum Codestil

**Wichtig**: Alle neuen Inhalte müssen auf **Deutsch** verfasst werden - sowohl Code-Kommentare als auch Dokumentation.

### Code-Konventionen

- **PEP 8** Konventionen strikt befolgen
- Typhinweise für Funktionsparameter und Rückgabewerte verwenden
- **Variablenbenennung**: `kleinbuchstaben_mit_unterstrichen` (deutsche Namen bevorzugt)
- **Klassenbenennung**: `CamelCase`
- **Umfassende Docstrings** mit deutschen Beschreibungen und doctest-Beispielen
- Fehlerbehandlung mit angemessenen Ausnahmetypen
- Properties (`@property`) gegenüber direktem Attributzugriff bevorzugen
- Funktionen klein halten und auf eine einzelne Verantwortlichkeit konzentrieren

### Pädagogische Anforderungen

- Code muss für Anfänger verständlich sein
- Schrittweise Komplexität aufbauen
- Viele Kommentare zur Erklärung hinzufügen
- Praktische, nachvollziehbare Beispiele verwenden
- Konsistenz mit bestehenden Notebook-Stilen wahren

### Markdown-Qualität

- Alle Markdown-Dateien (`.md`) müssen **frei von markdownlint-Fehlern** sein
- Überschriften müssen von Leerzeilen umgeben sein
- Listen müssen von Leerzeilen umgeben sein
- Code-Blöcke müssen von Leerzeilen umgeben sein
- Konsistente Formatierung und Struktur
- **Bei Markdown-Formatierungsproblemen**: Nutze den `markdown-syntax-formatter` Agent, um automatisch korrekte Markdown-Syntax zu gewährleisten

### Doctest-Beispiele

Funktionen sollten doctest-Beispiele enthalten:

```python
def addiere(a: int, b: int) -> int:
    """
    Addiert zwei Zahlen.

    >>> addiere(2, 3)
    5
    >>> addiere(-1, 1)
    0
    """
    return a + b
```

Beim Hinzufügen von Code die bestehenden Muster in ähnlichen Dateien befolgen und den pädagogischen Charakter der Codebasis beibehalten.
