# Security Policy

## Unterstützte Versionen

Dieses Projekt ist ein Bildungsprojekt für einen Python-Einführungskurs. Wir unterstützen die aktuellste Version des Kursmaterials.

| Version | Unterstützt          |
| ------- | -------------------- |
| latest  | :white_check_mark:   |
| < 1.0   | :x:                  |

## Sicherheitslücken melden

Die Sicherheit dieses Projekts nehmen wir ernst. Obwohl es sich um ein Bildungsprojekt handelt, möchten wir sicherstellen, dass keine schädlichen Inhalte oder unsicheren Praktiken vermittelt werden.

### Meldung von Sicherheitsproblemen

**Bitte melden Sie Sicherheitslücken NICHT über öffentliche GitHub Issues.**

Stattdessen senden Sie bitte eine E-Mail an:

**E-Mail:** <daniel.senften@talent-factory.ch>

**Betreff:** `[SECURITY] pyt-intro: Kurze Beschreibung`

### Was sollte in der Meldung enthalten sein?

Bitte geben Sie so viele der folgenden Informationen wie möglich an:

- **Art des Problems** (z.B. unsichere Code-Beispiele, Injection-Schwachstellen in Übungen)
- **Vollständige Pfade** zu den betroffenen Dateien
- **Ort des betroffenen Codes** (Tag/Branch/Commit oder direkte URL)
- **Schritt-für-Schritt-Anleitung** zur Reproduktion des Problems
- **Proof-of-Concept oder Exploit-Code** (falls möglich)
- **Auswirkungen** des Problems, einschließlich wie ein Angreifer es ausnutzen könnte

### Was passiert nach der Meldung?

1. **Bestätigung**: Sie erhalten innerhalb von 48 Stunden eine Bestätigung
2. **Bewertung**: Wir bewerten die Schwere und Auswirkung des Problems
3. **Behebung**: Wir arbeiten an einem Fix und halten Sie auf dem Laufenden
4. **Veröffentlichung**: Nach der Behebung veröffentlichen wir ein Update
5. **Anerkennung**: Mit Ihrer Erlaubnis werden Sie in den Release Notes erwähnt

## Sicherheits-Best-Practices für Studierende

### Beim Arbeiten mit diesem Projekt

1. **API-Schlüssel und Secrets**
   - Niemals API-Schlüssel in Code committen
   - Verwenden Sie `.env` Dateien (bereits in `.gitignore`)
   - Nutzen Sie Umgebungsvariablen

2. **Dateioperationen**
   - Validieren Sie Benutzereingaben
   - Verwenden Sie `with`-Statements für Dateioperationen
   - Seien Sie vorsichtig mit Dateipfaden

3. **Externe Pakete**
   - Installieren Sie nur vertrauenswürdige Pakete
   - Überprüfen Sie Paket-Quellen
   - Halten Sie Dependencies aktuell

4. **Code-Ausführung**
   - Vermeiden Sie `eval()` und `exec()` mit Benutzereingaben
   - Validieren Sie alle Eingaben
   - Verwenden Sie sichere Alternativen

### Beispiele für unsichere Praktiken (VERMEIDEN)

```python
# ❌ UNSICHER: eval() mit Benutzereingabe
user_input = input("Geben Sie eine Berechnung ein: ")
result = eval(user_input)  # Ermöglicht Code-Injection!

# ❌ UNSICHER: Dateipfad ohne Validierung
filename = input("Dateiname: ")
with open(filename, 'r') as f:  # Path Traversal möglich!
    content = f.read()

# ❌ UNSICHER: API-Schlüssel im Code
api_key = "sk-1234567890abcdef"  # Niemals hardcoden!
```

### Sichere Alternativen

```python
# ✅ SICHER: ast.literal_eval() für sichere Auswertung
import ast
user_input = input("Geben Sie eine Zahl ein: ")
try:
    number = ast.literal_eval(user_input)
except (ValueError, SyntaxError):
    print("Ungültige Eingabe")

# ✅ SICHER: Pfad-Validierung
import os
from pathlib import Path

base_dir = Path("./data")
filename = input("Dateiname: ")
filepath = (base_dir / filename).resolve()

# Prüfen, ob Pfad innerhalb des erlaubten Verzeichnisses liegt
if base_dir.resolve() in filepath.parents:
    with open(filepath, 'r') as f:
        content = f.read()
else:
    print("Ungültiger Dateipfad")

# ✅ SICHER: Umgebungsvariablen verwenden
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
```

## Bekannte Einschränkungen

Da dies ein Bildungsprojekt ist:

- Einige Übungen demonstrieren bewusst **unsichere Praktiken** zu Lernzwecken
- Diese sind klar als **"Nicht für Produktion"** gekennzeichnet
- Produktionsreife Alternativen werden immer bereitgestellt

## Sicherheits-Checkliste für Beitragende

Vor dem Einreichen eines Pull Requests:

- [ ] Keine Secrets oder API-Schlüssel im Code
- [ ] Keine unsicheren Praktiken ohne entsprechende Warnung
- [ ] Benutzereingaben werden validiert
- [ ] Dateipfade werden überprüft
- [ ] Dependencies sind aktuell und vertrauenswürdig
- [ ] Code-Beispiele folgen Best Practices

## Weitere Ressourcen

- [OWASP Top 10](https://owasp.org/www-project-top-ten/)
- [Python Security Best Practices](https://python.readthedocs.io/en/stable/library/security_warnings.html)
- [Bandit - Python Security Linter](https://bandit.readthedocs.io/)

## Kontakt

Für Sicherheitsfragen oder -bedenken:

- **E-Mail:** <daniel.senften@talent-factory.ch>
- **Betreff:** `[SECURITY] pyt-intro`

---

**Letzte Aktualisierung:** 2025-01-16
