# CLAUDE.md

Diese Datei bietet Anleitung für Claude Code (claude.ai/code) bei der Arbeit mit Code in diesem Repository.

## Projektübersicht

- Python-Einführungskurs/Tutorial auf Deutsch
- Verwendet Poetry für die Abhängigkeitsverwaltung

## Befehle

- Python-Skript ausführen: `python <skript_pfad>`
- Tests ausführen: `python -m doctest <datei.py>` oder Modul direkt ausführen
- Code formatieren: `black <datei_oder_verzeichnis>`
- Jupyter starten: `jupyter notebook`
- Abhängigkeiten installieren: `poetry install`

## Richtlinien zum Codestil

- PEP 8 Konventionen
- Typhinweise für Funktionsparameter und Rückgabewerte verwenden
- Variablenbenennung: kleinbuchstaben_mit_unterstrichen
- Klassenbenennung: CamelCase
- Umfassende Docstrings mit Beispielen (doctest)
- Fehlerbehandlung mit angemessenen Ausnahmetypen
- Bevorzugung von Properties (@property) gegenüber direktem Attributzugriff
- Funktionen klein und auf eine einzelne Verantwortlichkeit konzentriert halten

Beim Hinzufügen von Code die bestehenden Muster in ähnlichen Dateien befolgen und den pädagogischen Charakter der
Codebasis beibehalten.
