# Repository Setup Checkliste

Diese Checkliste hilft bei der Einrichtung des pyt-intro Repositories für einen neuen Kurs.

## 🔒 Branch Protection (WICHTIG!)

- [ ] **Branch Protection für `main` einrichten**
  - [ ] Settings → Branches → Add rule
  - [ ] Branch name pattern: `main`
  - [ ] Require pull request before merging (1 approval)
  - [ ] Restrict who can push (nur Kursleiter)
  - [ ] Disable force pushes
  - [ ] Disable deletions

- [ ] **Branch Protection für `develop` einrichten**
  - [ ] Settings → Branches → Add rule
  - [ ] Branch name pattern: `develop`
  - [ ] Require pull request before merging (1 approval)
  - [ ] Restrict who can push (nur Kursleiter)
  - [ ] Disable force pushes
  - [ ] Disable deletions

- [ ] **CODEOWNERS Datei verifizieren**
  - [ ] `.github/CODEOWNERS` enthält korrekte GitHub-Benutzernamen
  - [ ] Alle Kursleiter sind eingetragen

- [ ] **Branch Protection testen**
  - [ ] Als Studierender-Account testen
  - [ ] Direkter Push auf main sollte blockiert werden
  - [ ] Pull Request sollte funktionieren

## 👥 Zugriffsverwaltung

- [ ] **Repository Collaborators hinzufügen**
  - [ ] Settings → Collaborators and teams
  - [ ] Studierende mit **Read** oder **Triage** Zugriff hinzufügen
  - [ ] Kursleiter mit **Maintain** oder **Admin** Zugriff

- [ ] **Team erstellen (optional)**
  - [ ] Organization → Teams → New team
  - [ ] Team "Python-Intro-Studierende" erstellen
  - [ ] Team dem Repository mit Read-Zugriff hinzufügen

## 🚀 Cloud-Entwicklungsumgebungen

- [ ] **GitHub Codespaces aktivieren**
  - [ ] Settings → Codespaces
  - [ ] Enable Codespaces for this repository
  - [ ] `.devcontainer/devcontainer.json` ist vorhanden

- [ ] **Gitpod testen**
  - [ ] `.gitpod.yml` ist vorhanden
  - [ ] URL `gitpod.io/#<repo-url>` funktioniert
  - [ ] Dependencies werden automatisch installiert

## 📚 Dokumentation

- [ ] **README.md aktualisieren**
  - [ ] Kursinformationen sind aktuell
  - [ ] Links funktionieren
  - [ ] Kontaktinformationen sind korrekt

- [ ] **Backup-Environments Guide verifizieren**
  - [ ] `docs/exercises/backup-environments-quickstart.adoc` ist vorhanden
  - [ ] Git-Workflow ist dokumentiert
  - [ ] Branch-Namenskonventionen sind erklärt

- [ ] **BRANCH_PROTECTION.md gelesen**
  - [ ] Anleitung verstanden
  - [ ] Alle Schritte durchgeführt

## 🔧 Repository-Einstellungen

- [ ] **General Settings**
  - [ ] Repository ist private/public (je nach Anforderung)
  - [ ] Issues aktiviert
  - [ ] Discussions aktiviert (optional)
  - [ ] Wiki deaktiviert (optional)

- [ ] **Actions & Workflows**
  - [ ] GitHub Actions aktiviert (optional)
  - [ ] Workflow-Berechtigungen konfiguriert

- [ ] **Security**
  - [ ] Dependabot aktiviert
  - [ ] Code scanning aktiviert (optional)
  - [ ] Secret scanning aktiviert

## 📋 Vor Kursbeginn

- [ ] **Test-Durchlauf**
  - [ ] Als Studierender einloggen
  - [ ] Repository klonen
  - [ ] Codespace erstellen und testen
  - [ ] Feature-Branch erstellen
  - [ ] Commit und Push testen
  - [ ] Pull Request erstellen

- [ ] **Studierende informieren**
  - [ ] Link zum Repository versenden
  - [ ] Backup-Environments Guide teilen
  - [ ] Git-Workflow erklären
  - [ ] Branch-Konventionen kommunizieren

## ✅ Verifizierung

Nach Abschluss aller Schritte:

```bash
# 1. Branch Protection testen
git clone <repo-url>
cd pyt-intro
git checkout main
echo "test" >> test.txt
git add test.txt
git commit -m "test"
git push origin main
# Sollte mit Fehler abgelehnt werden!

# 2. Korrekter Workflow testen
git checkout -b feature/test
git push origin feature/test
# Sollte erfolgreich sein!
```

## 📞 Support

Bei Fragen oder Problemen:

- **E-Mail:** <daniel.senften@talent-factory.ch>
- **Dokumentation:** `.github/BRANCH_PROTECTION.md`
- **GitHub Docs:** <https://docs.github.com/en/repositories>

---

**Letzte Aktualisierung:** {localdate}  
**Verantwortlich:** Daniel Senften
