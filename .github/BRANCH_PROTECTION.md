# Branch Protection Einrichtung

Diese Anleitung beschreibt, wie Branch Protection Rules für die Branches `main` und `develop` eingerichtet werden, um zu verhindern, dass Studierende direkt auf diese Branches pushen oder mergen können.

## Warum Branch Protection?

- **Verhindert versehentliche Änderungen** auf wichtigen Branches
- **Erzwingt Code-Review-Prozess** durch Pull Requests
- **Schützt die Kursstruktur** vor ungewollten Modifikationen
- **Fördert Best Practices** im Git-Workflow

## Einrichtung in GitHub

### Schritt 1: Repository Settings öffnen

1. Öffnen Sie das Repository auf GitHub.com
2. Navigieren Sie zu **Settings** (Zahnrad-Symbol)
3. Klicken Sie im linken Menü auf **Branches**

### Schritt 2: Branch Protection Rule für `main` erstellen

1. Klicken Sie auf **Add branch protection rule**
2. Konfigurieren Sie folgende Einstellungen:

**Branch name pattern:**

```text
main
```

**Aktivieren Sie folgende Optionen:**

- ✅ **Require a pull request before merging**
  - ✅ Require approvals: `1`
  - ✅ Dismiss stale pull request approvals when new commits are pushed
  - ✅ Require review from Code Owners (optional)

- ✅ **Require status checks to pass before merging**
  - ✅ Require branches to be up to date before merging

- ✅ **Require conversation resolution before merging**

- ✅ **Do not allow bypassing the above settings**

- ✅ **Restrict who can push to matching branches**
  - Fügen Sie hier nur die Kursleiter/Maintainer hinzu
  - Studierende sollten NICHT in dieser Liste sein

- ✅ **Allow force pushes** → **Deaktiviert** (nicht ankreuzen!)

- ✅ **Allow deletions** → **Deaktiviert** (nicht ankreuzen!)

1. Klicken Sie auf **Create** oder **Save changes**

### Schritt 3: Branch Protection Rule für `develop` erstellen

Wiederholen Sie Schritt 2 mit folgenden Anpassungen:

**Branch name pattern:**

```text
develop
```

**Gleiche Einstellungen wie für `main`**, aber optional:

- Require approvals: `1` (kann auch auf 0 gesetzt werden für schnellere Integration)
- Weniger strikt bei Status Checks

### Schritt 4: Zusätzliche Empfehlungen

**Für alle Feature-Branches (optional):**

Branch name pattern:

```text
feature/*
```

- ✅ Require a pull request before merging
- ✅ Require status checks to pass before merging

## Verifizierung

### Test 1: Direkter Push blockiert

```bash
# Als Studierender versuchen, direkt auf main zu pushen
git checkout main
git commit -m "test"
git push origin main

# Erwartetes Ergebnis:
# ! [remote rejected] main -> main (protected branch hook declined)
```

### Test 2: Pull Request erforderlich

```bash
# Korrekter Workflow für Studierende
git checkout -b feature/mein-name
git add .
git commit -m "feat: Meine Änderungen"
git push origin feature/mein-name

# Dann auf GitHub: Pull Request erstellen
```

## Für Studierende

Die Studierenden sollten über die Branch Protection informiert werden. 
Verweisen Sie auf die Datei `docs/exercises/backup-environments-quickstart.adoc`, 
die den korrekten Git-Workflow erklärt.

### Wichtige Punkte für Studierende

1. **Niemals direkt auf `main` oder `develop` pushen**
2. **Immer eigenen Feature-Branch erstellen**
3. **Pull Requests für Integration verwenden**
4. **Regelmässig committen auf eigenem Branch**

## CODEOWNERS (optional)

Die `.github/CODEOWNERS` Datei definiert, wer für Code-Reviews zuständig ist.
Diese Datei wurde bereits erstellt und sollte die Kursleiter enthalten.

## Troubleshooting

### Problem: Studierender kann nicht pushen

**Ursache:** Versuch, direkt auf geschützten Branch zu pushen

**Lösung:**

```bash
# Auf eigenen Branch wechseln
git checkout -b feature/ihr-name

# Änderungen committen
git add .
git commit -m "feat: Beschreibung"

# Auf eigenen Branch pushen
git push origin feature/ihr-name
```

### Problem: Pull Request kann nicht gemerged werden

**Ursache:** Fehlende Approvals oder Merge-Konflikte

**Lösung:**

- Review von Kursleiter einholen
- Merge-Konflikte lokal auflösen
- Branch mit develop/main synchronisieren

## Weitere Ressourcen

- [GitHub Branch Protection Dokumentation](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches)
- [Pull Request Best Practices](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests)

## Wartung

**Regelmässig überprüfen:**

- Branch Protection Rules sind aktiv
- Nur autorisierte Personen haben Push-Rechte
- CODEOWNERS ist aktuell
- Studierende folgen dem korrekten Workflow
