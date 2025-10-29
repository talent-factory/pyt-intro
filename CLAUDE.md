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

### Fortgeschrittenen-Projekte

Für Studierende, die den Einführungskurs abgeschlossen haben (30+ Stunden Erfahrung):

- **Schachprogramm** (`docs/prp/schachprogramm-prp.md`): Vollständiges Demonstrationsprojekt mit Pygame-GUI, KI-Gegner (Minimax-Algorithmus), PGN-Persistierung und allen Schachregeln. Zeigt fortgeschrittene Konzepte wie MVC-Architektur, Event-Driven Programming, externe Bibliotheken (python-chess, pygame) und Algorithmen-Implementierung.

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
  - `tutorials/` - Umfassende Tutorials (Doctest, Grundlagen, Module, OOP, Pydantic, SQLAlchemy)
  - `exercises/` - Übungsaufgaben (kursabend-4-aufgaben.adoc, kursabend-5-projekte.adoc)
  - `prp/` - Product Requirement Prompts für Fortgeschrittenen-Projekte (schachprogramm-prp.md)
- **`solutions/`** - Musterlösungen für Kursabend 4 & 5
- **`testdaten/`** - Testdateien für Übungen (beispieltext.txt, produkte.csv, server.log, vokabeln.txt, quiz.txt)
- **`introcs/`** - 100+ Beispielmodule (Algorithmen, Datenstrukturen, Grafik)
- **`stdlib/`** - Hilfsmodule (stdio, stddraw, stdrandom, etc.)

### introcs-Module

Klassische CS-Beispiele für Anfänger inspiriert von Princeton's "Introduction to Computer Science":

- Grundprogramme (helloworld.py, useargument.py)
- Algorithmen (binarysearch.py, sortierung)
- Datenstrukturen (arraystack.py, bst.py, linkedqueue.py)
- Mathematik (fibonacci, gaussian, mandelbrot)
- Grafik (turtle graphics, plotting)
- Simulationen (percolation, mandelbrot, brownian motion)

**Wichtig**: Viele `introcs/`-Module importieren von `stdlib`-Paket (custom I/O-Funktionen wie stdio, stddraw). Diese Module sind Lehrmaterial und sollten nicht für Production-Code verwendet werden.

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

- **PEP 8** strikt befolgen (max. 100 Zeichen Zeilenlänge, bevorzugt 88)
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

    Examples:
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
- Viele erklärende Kommentare (warum, nicht was)
- Praktische, nachvollziehbare Beispiele aus dem Alltag
- Konsistenz mit bestehenden Notebook-Stilen
- Vermeidung fortgeschrittener Python-Features (außer in späteren Notebooks)
- Deutsche Fehlermeldungen und hilfreiche Hinweise für Benutzer

### Dokumentationsformate

- **Markdown** (`.md`): Frei von markdownlint-Fehlern, Leerzeilen um Überschriften/Listen/Code-Blöcke
- **AsciiDoc** (`.adoc`): Für umfangreiche Tutorials und Übungsaufgaben mit erweiterten Features (TOC, Admonitions, etc.)

## Git-Workflow

### Branch Protection

Die Branches `main` und `develop` sind geschützt (siehe `.github/BRANCH_PROTECTION.md`):

- Studierende können **nicht** direkt pushen
- Nur Pull Requests mit Review erlaubt
- Kursleiter/Maintainer haben spezielle Rechte

### Korrekter Workflow für Studierende

```bash
# Eigenen Feature-Branch erstellen
git checkout -b feature/ihr-name

# Änderungen committen mit Conventional Commits
git commit -m "feat: Beschreibung"

# Branch pushen
git push origin feature/ihr-name

# Pull Request auf GitHub erstellen
```

### Commit-Konventionen

Wir verwenden [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` - Neue Features
- `fix:` - Bugfixes
- `docs:` - Dokumentationsänderungen
- `style:` - Formatierung (keine Code-Änderungen)
- `refactor:` - Code-Umstrukturierung
- `test:` - Tests hinzufügen/ändern
- `chore:` - Wartungsarbeiten (Dependencies, Config)

## Cloud-Entwicklungsumgebungen

Das Projekt unterstützt mehrere Cloud-Entwicklungsumgebungen für Studierende ohne lokales Setup:

- **GitHub Codespaces**: Siehe `.devcontainer/devcontainer.json`
- **Gitpod**: Siehe `.gitpod.yml`

Detaillierte Anleitung: `docs/exercises/backup-environments-quickstart.adoc`

## Wichtige Ressourcen

- **Cheat Sheet**: `docs/cheat-sheet.adoc` - Schnellreferenz für Python-Grundlagen
- **Tutorials**: `docs/tutorials/` - Umfassende Anleitungen zu Doctest, Grundlagen, Modulen, OOP
- **Übungen**: `docs/exercises/` - Aufgaben für Kursabende 4 & 5
- **Branch Protection**: `.github/BRANCH_PROTECTION.md` - Setup-Anleitung für Kursleiter
- **Contributing Guide**: `CONTRIBUTING.md` - Entwicklungs-Workflow und Standards

## Besonderheiten

### Slash-Commands

Das Projekt verwendet Claude Code Slash-Commands (siehe `docs/slash-commands.adoc` für Konzepte). Die verfügbaren Commands sind in `.claude/commands/` definiert.

### Musterlösungen

Die Musterlösungen in `solutions/` sind bewusst **Beispiele**, nicht die einzig richtigen Lösungen. Studierende sollen ermutigt werden, eigene Wege zu finden.

### Testdaten

Die Dateien in `testdaten/` sind speziell für Übungen erstellt:

- `beispieltext.txt` - Für Textanalyse (Aufgabe 2.1)
- `produkte.csv` - Für CSV-Verarbeitung (Aufgabe 2.2)
- `server.log` - Für Log-File-Analyzer (Aufgabe 2.3)
- `vokabeln.txt` - Für Vokabeltrainer (Aufgabe 3.1)
- `quiz.txt` - Für Quiz-Generator (Kursabend 5)
