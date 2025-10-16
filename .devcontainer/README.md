# GitHub Codespaces Konfiguration

Diese Konfiguration ermöglicht es, das Python-Intro-Projekt direkt in GitHub Codespaces zu verwenden.

## Features

- **Python 3.13** vorinstalliert
- **uv Package Manager** für Dependency Management
- **Jupyter Notebook** Support
- **VS Code Extensions** automatisch installiert:
  - Python
  - Pylance (IntelliSense)
  - Jupyter
  - Ruff (Linting & Formatting)

## Automatische Setup-Schritte

Beim Erstellen eines Codespace werden automatisch folgende Schritte ausgeführt:

1. Python 3.13 Image wird geladen
2. Git und GitHub CLI werden installiert
3. uv Package Manager wird installiert
4. Projekt-Abhängigkeiten werden mit `uv sync` installiert
5. Port 8888 wird für Jupyter Notebook weitergeleitet

## Verwendung

1. Öffnen Sie das Repository auf GitHub
2. Klicken Sie auf "Code" → "Codespaces" → "Create codespace on main"
3. Warten Sie 2-3 Minuten bis die Umgebung bereit ist
4. Starten Sie Jupyter Notebook mit: `jupyter notebook`
5. Oder führen Sie Python-Skripte aus mit: `uv run python <script.py>`

## Anpassungen

Falls Sie die Konfiguration anpassen möchten, bearbeiten Sie die Datei `devcontainer.json`:

- **Extensions hinzufügen:** Ergänzen Sie die Liste unter `customizations.vscode.extensions`
- **Ports hinzufügen:** Erweitern Sie `forwardPorts` und `portsAttributes`
- **Setup-Befehle ändern:** Passen Sie `postCreateCommand` an

## Weitere Informationen

- [GitHub Codespaces Dokumentation](https://docs.github.com/en/codespaces)
- [Dev Container Specification](https://containers.dev/)
