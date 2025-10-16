# Contributing zu pyt-intro

Vielen Dank für Ihr Interesse, zu diesem Projekt beizutragen! 🎉

## 📋 Inhaltsverzeichnis

- [Code of Conduct](#code-of-conduct)
- [Wie kann ich beitragen?](#wie-kann-ich-beitragen)
- [Entwicklungs-Workflow](#entwicklungs-workflow)
- [Coding Standards](#coding-standards)
- [Commit-Konventionen](#commit-konventionen)
- [Pull Request Prozess](#pull-request-prozess)

## Code of Conduct

Dieses Projekt folgt dem [Contributor Covenant Code of Conduct](CODE_OF_CONDUCT.md). Durch Ihre Teilnahme verpflichten Sie sich, diesen Code einzuhalten.

## Wie kann ich beitragen?

### 🐛 Fehler melden

Wenn Sie einen Fehler gefunden haben:

1. **Prüfen Sie**, ob der Fehler bereits gemeldet wurde (Issues durchsuchen)
2. **Erstellen Sie ein neues Issue** mit:
   - Klarer Beschreibung des Problems
   - Schritten zur Reproduktion
   - Erwartetes vs. tatsächliches Verhalten
   - Python-Version und Betriebssystem
   - Screenshots (falls relevant)

### 💡 Features vorschlagen

Für neue Feature-Vorschläge:

1. **Erstellen Sie ein Issue** mit dem Label `enhancement`
2. **Beschreiben Sie**:
   - Das Problem, das gelöst werden soll
   - Ihre vorgeschlagene Lösung
   - Mögliche Alternativen
   - Zusätzlichen Kontext

### 📝 Dokumentation verbessern

Dokumentations-Verbesserungen sind immer willkommen:

- Tippfehler korrigieren
- Unklare Erklärungen verbessern
- Neue Beispiele hinzufügen
- Tutorials erweitern

### 🎓 Für Studierende

Als Studierender des Kurses:

1. **Arbeiten Sie auf Ihrem eigenen Branch**: `feature/ihr-name`
2. **Teilen Sie Ihre Lösungen** über Pull Requests
3. **Helfen Sie anderen** durch Code-Reviews
4. **Stellen Sie Fragen** in Issues oder Discussions

## Entwicklungs-Workflow

### 1. Repository forken und klonen

```bash
# Repository forken auf GitHub, dann:
git clone https://github.com/IHR-USERNAME/pyt-intro.git
cd pyt-intro
```

### 2. Entwicklungsumgebung einrichten

```bash
# Python 3.13+ erforderlich
python --version

# Dependencies installieren
uv sync

# Oder mit pip
pip install -e .
```

### 3. Branch erstellen

```bash
# Für Features
git checkout -b feature/beschreibung

# Für Bugfixes
git checkout -b fix/beschreibung

# Für Dokumentation
git checkout -b docs/beschreibung
```

### 4. Änderungen vornehmen

- Schreiben Sie klaren, gut dokumentierten Code
- Folgen Sie den Coding Standards
- Fügen Sie Tests hinzu (falls zutreffend)
- Aktualisieren Sie die Dokumentation

### 5. Tests ausführen

```bash
# Doctests ausführen
python -m doctest datei.py

# Alle Python-Dateien testen
find . -name "*.py" -exec python -m doctest {} \;
```

### 6. Änderungen committen

```bash
git add .
git commit -m "feat: Kurze Beschreibung"
```

Siehe [Commit-Konventionen](#commit-konventionen) für Details.

### 7. Push und Pull Request

```bash
git push origin feature/beschreibung
```

Erstellen Sie dann einen Pull Request auf GitHub.

## Coding Standards

### Python Style Guide

Wir folgen [PEP 8](https://pep8.org/) mit einigen Anpassungen:

- **Einrückung**: 4 Leerzeichen
- **Zeilenlänge**: Max. 100 Zeichen (bevorzugt 88)
- **Imports**: Gruppiert (stdlib, third-party, local)
- **Naming**:
  - Klassen: `PascalCase`
  - Funktionen/Variablen: `snake_case`
  - Konstanten: `UPPER_CASE`

### Dokumentation

```python
def funktion_name(parameter: str) -> int:
    """
    Kurze Beschreibung der Funktion.
    
    Args:
        parameter: Beschreibung des Parameters
        
    Returns:
        Beschreibung des Rückgabewerts
        
    Examples:
        >>> funktion_name("test")
        42
    """
    return 42
```

### Docstrings

- Verwenden Sie **deutsche Sprache** für Kommentare und Docstrings
- Fügen Sie **Beispiele** mit doctest hinzu
- Dokumentieren Sie **Parameter und Rückgabewerte**

## Commit-Konventionen

Wir verwenden [Conventional Commits](https://www.conventionalcommits.org/):

### Format

```text
type: Kurze Beschreibung (max. 50 Zeichen)

Detaillierte Erklärung (optional)
- Änderung 1
- Änderung 2
```

### Types

- `feat:` - Neue Features
- `fix:` - Bugfixes
- `docs:` - Dokumentationsänderungen
- `style:` - Formatierung (keine Code-Änderungen)
- `refactor:` - Code-Umstrukturierung
- `test:` - Tests hinzufügen/ändern
- `chore:` - Wartungsarbeiten (Dependencies, Config)

### Beispiele

```bash
# Feature
git commit -m "feat: Neue Übungsaufgabe für Kursabend 4 hinzugefügt"

# Bugfix
git commit -m "fix: Korrektur der Palindrom-Funktion"

# Dokumentation
git commit -m "docs: Tutorial für Dateiverarbeitung erweitert"

# Refactoring
git commit -m "refactor: Vereinfachung der Highscore-Logik"
```

## Pull Request Prozess

### Vor dem Erstellen

- ✅ Code folgt den Coding Standards
- ✅ Tests wurden ausgeführt und bestehen
- ✅ Dokumentation wurde aktualisiert
- ✅ Commit-Messages folgen den Konventionen
- ✅ Branch ist aktuell mit `develop`

### Pull Request erstellen

1. **Titel**: Klare, beschreibende Überschrift
2. **Beschreibung**:
   - Was wurde geändert?
   - Warum wurde es geändert?
   - Wie wurde es getestet?
   - Screenshots (falls UI-Änderungen)
3. **Labels**: Passende Labels hinzufügen
4. **Reviewer**: Kursleiter als Reviewer zuweisen

### Template

```markdown
## Beschreibung
Kurze Zusammenfassung der Änderungen.

## Art der Änderung
- [ ] Bugfix
- [ ] Neues Feature
- [ ] Dokumentation
- [ ] Refactoring

## Wie wurde getestet?
Beschreibung der durchgeführten Tests.

## Checkliste
- [ ] Code folgt den Style Guidelines
- [ ] Selbst-Review durchgeführt
- [ ] Dokumentation aktualisiert
- [ ] Tests bestehen
```

### Review-Prozess

1. **Automatische Checks** müssen bestehen
2. **Code-Review** durch Kursleiter erforderlich
3. **Änderungen umsetzen** basierend auf Feedback
4. **Merge** nach Approval

## Projektstruktur

```text
pyt-intro/
├── .github/              # GitHub-spezifische Dateien
│   ├── BRANCH_PROTECTION.md
│   ├── CODEOWNERS
│   └── workflows/        # CI/CD (zukünftig)
├── docs/                 # Dokumentation (AsciiDoc)
│   ├── tutorials/
│   └── exercises/
├── exercise/             # Übungsaufgaben
├── solutions/            # Musterlösungen
├── ipynb/               # Jupyter Notebooks
├── introcs/             # Beispielcode
├── stdlib/              # Hilfsmodule
└── testdaten/           # Testdaten für Übungen
```

## Entwicklungsumgebungen

### Lokal

```bash
# Mit uv
uv sync
uv run python script.py

# Mit pip
pip install -e .
python script.py
```

### Cloud (für Studierende)

- **GitHub Codespaces**: Siehe `.devcontainer/devcontainer.json`
- **Gitpod**: Siehe `.gitpod.yml`

Anleitung: `docs/exercises/backup-environments-quickstart.adoc`

## Fragen?

- **Issues**: Für Bugs und Feature-Requests
- **Discussions**: Für allgemeine Fragen
- **E-Mail**: <daniel.senften@talent-factory.ch>

## Lizenz

Durch Ihren Beitrag stimmen Sie zu, dass Ihre Änderungen unter der [MIT License](LICENSE) lizenziert werden.

---

**Vielen Dank für Ihren Beitrag! 🙏**
