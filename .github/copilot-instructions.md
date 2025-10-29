# KI-Agenten Anweisungen

Diese Anweisungen helfen KI-Agenten, sich schnell im Python-Einführungskurs-Projekt zurechtzufinden.

## Projektübersicht

Deutschsprachiger Python-Einführungskurs für absolute Programmieranfänger. Der Kurs ist in 5 Abende gegliedert und verwendet Jupyter Notebooks, interaktive Übungen und praktische Projekte.

### Kernprinzipien

- **Sprache**: Alle Inhalte (Code, Kommentare, Docs) sind auf Deutsch
- **Zielgruppe**: Absolute Anfänger ohne Programmiererfahrung
- **Didaktik**: Schrittweiser Aufbau von Grundlagen zu Mini-Projekten

## Architektur und Komponenten

### Hauptkomponenten

- `ipynb/`: Jupyter Notebooks für interaktives Lernen (00-hello bis 03-Classes-and-Objects)
- `docs/`: AsciiDoc-Dokumentation und Übungsaufgaben
- `introcs/`: 100+ Beispielmodule für CS-Grundlagen (von Princeton inspiriert)
- `stdlib/`: Hilfsmodule für Anfänger (stdio, stddraw, stdrandom)
- `testdaten/`: Testdateien für Übungen (*.txt, *.csv, *.log)

### Wichtige Integrationen

- Die `introcs/`-Module importieren stark von `stdlib/`-Modulen
- Beispiel: `from stdlib import stdio, stddraw` in Grafik-Modulen

## Entwicklungsworkflow

### Setup

```bash
# Abhängigkeiten installieren
uv sync

# Jupyter starten für Notebooks
jupyter notebook
```

### Tests

```bash
# Doctests ausführen (verbose für Details)
python -m doctest <datei.py>
python -m doctest -v <datei.py>
```

### Code-Qualität

- Black-Formatierung (max. 100 Zeichen, bevorzugt 88)
- Type Hints verwenden
- Docstrings mit Doctests auf Deutsch

## Code-Konventionen

### Namensgebung (strikt auf Deutsch)

```python
# Variablen: kleinbuchstaben_mit_unterstrichen
anzahl_versuche = 0
ist_student = True

# Klassen: CamelCase
class Spieler:
    pass
```

### Docstring-Format

```python
def addiere(a: int, b: int) -> int:
    """
    Addiert zwei Zahlen.
    
    Args:
        a: Erste Zahl
        b: Zweite Zahl
        
    Returns:
        Summe der beiden Zahlen
        
    >>> addiere(2, 3)
    5
    """
    return a + b
```

## Bekannte Einschränkungen

- `introcs/`-Module sind nur für Lehrzwecke, nicht für Produktion
- `stdlib/`-Module implementieren custom I/O-Funktionen für Lehrzwecke