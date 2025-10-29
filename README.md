# Python Programmierung Basis

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)](CONTRIBUTING.md)

Einführungskurs in die Python-Programmierung für Anfänger ohne Vorkenntnisse.

## Kursinformationen

**Dauer:** 5 Abende à 4 Lektionen  
**Zielgruppe:** Programmieranfänger ohne Vorkenntnisse  
**Sprache:** Deutsch

## Inhalt

- Programmieren - was heisst das?
- Erste Schritte mit der Python Shell
- Die Entwicklungsumgebung IDLE
- Variablen und Operatoren
- Datentypen
- Grundlagen der prozeduralen Programmierung
- Objekte und Referenzen
- Dateien lesen und schreiben
- Modularisierung

## Lernziele

- Sie kennen die wichtigsten Programmiergrundlagen
- Sie kennen die Grundlagen der prozeduralen Programmierung
- Sie können einfache Python-Programme selbstständig schreiben
- Sie verstehen grundlegende Kontrollstrukturen (Bedingungen, Schleifen)
- Sie können Funktionen definieren und verwenden

## Kursübersicht

### 1. Kursabend: Einführung und Installation

- Einleitung ins Programmieren
- Installation der benötigten Software (Python, Git, uv, IDE)
- Erste Schritte mit Python
- Hello World Programm

### 2. Kursabend: Eingabe und Jupyter Notebooks

- Eingabe mit `input()`
- Arbeiten mit Jupyter Notebooks
- Praktische Aufgaben:
  - Berechnen des Hundealters
  - Palindrome erkennen

### 3. Kursabend: Kontrollstrukturen und Funktionen

- Bedingte Anweisungen (`if`, `elif`, `else`)
- Blöcke und Einrückung
- Schleifen (`for`, `while`)
- Funktionen definieren und aufrufen
- Tutorials:
  - Doctest Tutorial
  - Python Grundlagen Tutorial
  - Python Module Tutorial

### 4. Kursabend: Dateiverarbeitung und Praxis-Workshop

- Einführung in Dateiverarbeitung (lesen, schreiben, with-Statement)
- Praktische Übungen in drei Schwierigkeitsstufen:
  - Level 1: Zahlenraten mit Highscore, Einkaufsliste, Notizen-App
  - Level 2: Textanalyse-Tool, CSV-Verarbeitung, Log-File-Analyzer
  - Level 3: Vokabeltrainer, Kontaktverwaltung
- Fokus auf selbstständiges Üben und Anwenden

### 5. Kursabend: Mini-Projekte und Abschluss

- Auswahl aus vier Mini-Projekten:
  - Digitales Tagebuch
  - Ausgaben-Tracker
  - Quiz-Generator
  - Passwort-Generator und -Manager
- Selbstständige Projektarbeit (einzeln oder zu zweit)
- Präsentation der Ergebnisse
- Ausblick auf weiterführende Themen

## Fortgeschrittenen-Projekte

Nach Abschluss des Einführungskurses stehen umfangreichere Projekte zur Verfügung:

### Python-Schachprogramm

Vollständiges Demonstrationsprojekt für Fortgeschrittene (30+ Stunden Erfahrung):

- **Features**: Pygame-GUI mit Drag-and-Drop, KI-Gegner (Minimax-Algorithmus), Spielstand speichern/laden (PGN), Zughistorie mit Undo
- **Lernziele**: MVC-Architektur, Event-Driven Programming, externe Bibliotheken (python-chess, pygame), Algorithmen-Implementierung
- **Dokumentation**: `docs/prp/schachprogramm-prp.md`
- **Zeitaufwand**: ~52 Stunden (6 Wochen bei 8h/Woche)

Das Projekt zeigt fortgeschrittene Konzepte und eignet sich als Portfolio-Projekt oder für einen weiterführenden Python-Kurs.

## Projektstruktur

```text
pyt-intro/
├── docs/                   # Dokumentation in AsciiDoc
│   ├── 01-einleitung.adoc  # Einführung ins Programmieren
│   ├── cheat-sheet.adoc    # Schnellreferenz für Kursabende 4 & 5
│   ├── tutorials/          # Umfassende Tutorials
│   ├── exercises/          # Übungsaufgaben
│   │   ├── kursabend-4-aufgaben.adoc
│   │   └── kursabend-5-projekte.adoc
│   └── prp/                # Product Requirement Prompts (Fortgeschrittene)
│       └── schachprogramm-prp.md
├── ipynb/                  # Jupyter Notebooks
│   ├── 00-hello.ipynb
│   ├── 01-Introduction-to-Python.ipynb
│   ├── 02-Functions-and-Modules.ipynb
│   └── 03-Classes-and-Objects.ipynb
├── exercise/               # Übungsaufgaben und Lösungen
├── solutions/              # Musterlösungen
│   ├── kursabend-4/        # Lösungen für Kursabend 4
│   └── kursabend-5/        # Lösungen für Kursabend 5
├── testdaten/              # Testdaten für Übungen
│   ├── beispieltext.txt
│   ├── produkte.csv
│   ├── server.log
│   ├── vokabeln.txt
│   └── quiz.txt
├── introcs/                # Beispielcode-Sammlung
└── stdlib/                 # Hilfsmodule
```

## Installation und Setup

### Voraussetzungen

- Python 3.13 oder höher
- Git
- uv (Package Manager)

### Installation

```bash
# Repository klonen
git clone <repository-url>
cd pyt-intro

# Abhängigkeiten installieren
uv sync
```

### Entwicklungsumgebungen

Im Kurs werden folgende IDEs vorgestellt:

- **Windsurf (Cascade)** - Hauptentwicklungsumgebung mit AI-Unterstützung
- **Visual Studio Code (Augie)** - Alternative IDE mit AI-Features
- **PyCharm** - Professionelle Python-IDE

## Nützliche Befehle

### Package Management

```bash
# Abhängigkeiten installieren
uv sync

# Python-Skript ausführen
uv run python <skript_pfad>

# Paket hinzufügen
uv add <paketname>
```

### Jupyter Notebooks

```bash
# Jupyter Notebook starten
jupyter notebook

# Notebook zu Markdown konvertieren
jupyter nbconvert --to markdown <notebook.ipynb>

# Markdown zu PDF konvertieren
pandoc -s -o <output.pdf> <input.md>
```

### Testing

```bash
# Doctest ausführen
python -m doctest <datei.py>

# Doctest mit ausführlicher Ausgabe
python -m doctest -v <datei.py>
```

## Git-Workflow für Studierende

⚠️ **Wichtig:** Die Branches `main` und `develop` sind geschützt!

**Korrekter Workflow:**

1. Eigenen Feature-Branch erstellen: `git checkout -b feature/ihr-name`
2. Änderungen committen: `git commit -m "feat: Beschreibung"`
3. Branch pushen: `git push origin feature/ihr-name`
4. Pull Request auf GitHub erstellen

Detaillierte Anleitung: `docs/exercises/backup-environments-quickstart.adoc`

## Ressourcen

- [Offizielle Python-Dokumentation](https://docs.python.org/de/3/)
- [Python Tutorial (deutsch)](https://pythonbuch.com/index.html)
- Kurs-Dokumentation: `docs/index.html`
- Branch Protection Setup: `.github/BRANCH_PROTECTION.md` (für Kursleiter)

## Contributing

Beiträge sind willkommen! Bitte lesen Sie [CONTRIBUTING.md](CONTRIBUTING.md) für Details zum Entwicklungsprozess und wie Sie Pull Requests einreichen können.

### Community-Richtlinien

- [Code of Conduct](CODE_OF_CONDUCT.md) - Verhaltenskodex für die Community
- [Security Policy](SECURITY.md) - Sicherheitsrichtlinien und Meldeverfahren
- [Changelog](CHANGELOG.md) - Versionshistorie und Änderungen

## Lizenz

Dieses Projekt ist unter der [MIT License](LICENSE) lizenziert - siehe die LICENSE-Datei für Details.

## Autor

**Daniel Senften**  
E-Mail: <daniel.senften@talent-factory.ch>  
Organisation: [Talent Factory](https://www.talent-factory.xyz)

## Danksagungen

Vielen Dank an alle Studierenden und Beitragenden, die dieses Projekt unterstützen!
