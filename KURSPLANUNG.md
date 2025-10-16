# Kursplanung: Python Programmierung Basis

## Übersicht

Dieses Dokument bietet eine Übersicht über die Kursplanung für die letzten beiden Kursabende.

## Kursabend 4: Dateiverarbeitung und Praxis-Workshop

### Zeitplan (4 Lektionen à 45 Min = 180 Min)

| Zeit | Aktivität | Inhalt |
|------|-----------|--------|
| **Lektion 1** (45 Min) | Input + Setup | - Mini-Wiederholung (15 Min)<br>- Einführung Dateiverarbeitung (15 Min)<br>- Live-Coding Beispiel (15 Min) |
| **Lektion 2-3** (90 Min) | Geleitetes Üben | - Studierende arbeiten an Aufgaben<br>- Du zirkulierst und hilfst<br>- Aufgaben in 3 Levels |
| **Lektion 4** (45 Min) | Review & Reflexion | - Code-Präsentationen (30 Min)<br>- Gemeinsame Besprechung (15 Min) |

### Materialien

- **Aufgabenstellung:** `docs/exercises/kursabend-4-aufgaben.adoc`
- **Testdaten:** `testdaten/` Verzeichnis
- **Musterlösungen:** `solutions/kursabend-4/`
- **Cheat Sheet:** `docs/cheat-sheet.adoc`

### Vorbereitung

#### Vor dem Kurs

1. ✅ Aufgaben-PDF generieren (optional):
   ```bash
   asciidoctor-pdf docs/exercises/kursabend-4-aufgaben.adoc
   ```

2. ✅ Cheat Sheet-PDF generieren (optional):
   ```bash
   asciidoctor-pdf docs/cheat-sheet.adoc
   ```

3. ✅ Testdaten auf Moodle hochladen oder Link zum Repository teilen

4. ✅ Beamer/Projektor für Live-Coding vorbereiten

#### Während des Kurses

- **Wiederholung (15 Min):**
  - Frage Studierende: Was haben wir letzte Woche gelernt?
  - Kurze interaktive Wiederholung: if, for, while, Funktionen
  - Zeige Beispiel aus vorheriger Woche

- **Dateiverarbeitung (15 Min):**
  - Erkläre `open()`, `with`-Statement
  - Zeige Modi: `'r'`, `'w'`, `'a'`
  - Wichtigkeit von `encoding='utf-8'`
  - Fehlerbehandlung mit `try-except FileNotFoundError`

- **Live-Coding (15 Min):**
  - Erstelle gemeinsam ein einfaches Beispiel
  - Z.B.: Textdatei einlesen, Zeilen zählen, in neue Datei schreiben
  - Studierende sollen mittippen

### Tipps für die Durchführung

**Während der Übungsphase:**

- ✅ Ermutige Studierende, mit einfachen Aufgaben zu beginnen
- ✅ Betone, dass Fehler normal und Teil des Lernprozesses sind
- ✅ Fördere Zusammenarbeit zwischen Studierenden
- ✅ Gib Hilfestellung, aber nicht die komplette Lösung
- ✅ Achte darauf, dass niemand "verloren" geht

**Häufige Probleme:**

1. **Datei nicht gefunden:** Pfade erklären (relativ vs. absolut)
2. **Encoding-Fehler:** Immer `encoding='utf-8'` verwenden
3. **Datei nicht geschlossen:** `with`-Statement verwenden
4. **Leere Zeilen:** `strip()` verwenden

### Bewertung

Keine formale Bewertung, aber beobachte:

- Wer kommt gut voran?
- Wer braucht mehr Unterstützung?
- Welche Konzepte sind noch unklar?

## Kursabend 5: Mini-Projekte und Abschluss

### Zeitplan (4 Lektionen à 45 Min = 180 Min)

| Zeit | Aktivität | Inhalt |
|------|-----------|--------|
| **Lektion 1** (45 Min) | Projekt-Briefing | - Vorstellung der 4 Projekte (15 Min)<br>- Projektwahl und Planung (15 Min)<br>- Erste Schritte (15 Min) |
| **Lektion 2-3** (90 Min) | Projekt-Arbeit | - Selbstständige Arbeit<br>- Pair Programming erlaubt<br>- Du unterstützt bei Problemen |
| **Lektion 4** (45 Min) | Präsentation & Abschluss | - Projekt-Präsentationen (25 Min)<br>- Feedback (10 Min)<br>- Ausblick (10 Min) |

### Materialien

- **Projektbeschreibungen:** `docs/exercises/kursabend-5-projekte.adoc`
- **Testdaten:** `testdaten/quiz.txt`, `testdaten/vokabeln.txt`
- **Musterlösungen:** `solutions/kursabend-5/`
- **Cheat Sheet:** `docs/cheat-sheet.adoc`

### Vorbereitung

#### Vor dem Kurs

1. ✅ Projekt-PDF generieren (optional)
2. ✅ Entscheide: Einzelarbeit oder Pair Programming?
3. ✅ Bereite Präsentations-Reihenfolge vor (freiwillig!)
4. ✅ Überlege dir Feedback-Punkte

#### Während des Kurses

- **Projekt-Briefing (15 Min):**
  - Stelle alle 4 Projekte kurz vor
  - Zeige Beispiel-Output (optional)
  - Erkläre Mindestanforderungen vs. Erweiterungen
  - Betone: Lieber einfach und fertig als komplex und halb

- **Projektwahl (15 Min):**
  - Studierende wählen Projekt
  - Optional: Teams bilden (max. 2 Personen)
  - Kurze Planung: Welche Funktionen zuerst?

- **Erste Schritte (15 Min):**
  - Studierende beginnen mit Programmieren
  - Du gehst herum, beantwortest erste Fragen

### Tipps für die Durchführung

**Während der Projekt-Arbeit:**

- ✅ Lass Studierende möglichst selbstständig arbeiten
- ✅ Gib Denkanstöße statt fertige Lösungen
- ✅ Ermutige zum Testen nach jeder neuen Funktion
- ✅ Erinnere an das Cheat Sheet
- ✅ Zeitmanagement: 30 Min vor Schluss → Warnung

**Präsentationen:**

- ✅ Freiwillig, kein Zwang!
- ✅ Kurz halten (3-5 Min pro Person/Team)
- ✅ Fokus auf: Was funktioniert? Was war schwierig?
- ✅ Positive Atmosphäre schaffen
- ✅ Applaus nach jeder Präsentation!

### Feedback-Vorlage

Für jede Präsentation:

1. **Was war besonders gut?** (mindestens 1 positiver Punkt)
2. **Was könnte man noch verbessern?** (konstruktiv)
3. **Was hast du gelernt?** (Frage an Studierende)

### Abschluss und Ausblick (10 Min)

**Zusammenfassung:**

- Was haben wir in diesem Kurs gelernt?
- Welche Erfolge haben wir gefeiert?
- Wie geht es weiter?

**Weiterführende Themen erwähnen:**

- Objektorientierte Programmierung
- Web-Entwicklung mit Flask/Django
- Datenanalyse mit pandas
- Automatisierung
- APIs

**Ressourcen teilen:**

- Python-Dokumentation
- Online-Kurse (Codecademy, Real Python)
- YouTube-Kanäle
- Python-Communities

**Feedback einholen:**

- Was hat euch gefallen?
- Was könnte besser sein?
- Welche Themen interessieren euch?

## Checkliste: Vor jedem Kursabend

### Kursabend 4

- [ ] Beamer/Projektor getestet
- [ ] Beispiel-Code für Live-Coding vorbereitet
- [ ] Testdaten verfügbar (Moodle oder Repository)
- [ ] Cheat Sheet ausgedruckt oder digital verfügbar
- [ ] Musterlösungen bereit (für dich)
- [ ] Whiteboard/Flipchart für Erklärungen

### Kursabend 5

- [ ] Projekt-Beschreibungen verfügbar
- [ ] Testdaten für Quiz und Vokabeltrainer bereit
- [ ] Präsentations-Reihenfolge überlegt
- [ ] Feedback-Notizen vorbereitet
- [ ] Ausblick-Material (Links, Ressourcen)
- [ ] Eventuell: Zertifikate oder Teilnahmebestätigungen

## Notizen und Beobachtungen

### Kursabend 4

**Datum:** _______________

**Anwesend:** _____ / _____

**Gut gelaufen:**

- 
- 

**Verbesserungspotenzial:**

- 
- 

**Schwierige Konzepte:**

- 
- 

**Für nächstes Mal:**

- 
- 

### Kursabend 5

**Datum:** _______________

**Anwesend:** _____ / _____

**Projekte gewählt:**

- Tagebuch: _____ Personen
- Ausgaben-Tracker: _____ Personen
- Quiz: _____ Personen
- Passwort-Generator: _____ Personen

**Präsentationen:**

- Anzahl: _____
- Besonders gelungen: 
- 

**Feedback der Studierenden:**

- 
- 

**Für nächsten Kurs:**

- 
- 

## Zusätzliche Ressourcen

### Für Studierende

- **Cheat Sheet:** `docs/cheat-sheet.adoc`
- **Testdaten:** `testdaten/`
- **Musterlösungen:** `solutions/` (nach dem Kurs freigeben)

### Für dich als Dozent

- **Pädagogische Hinweise:** Siehe Aufgaben-Dokumente
- **Zeitmanagement:** Nutze Timer für Übungsphasen
- **Motivation:** Betone Fortschritte, nicht Perfektion

## Kontakt und Support

Bei Fragen oder Problemen:

- **Moodle-Forum:** Für asynchrone Fragen
- **E-Mail:** Für dringende Anliegen
- **Office Hours:** Optional, wenn angeboten

---

**Viel Erfolg mit den letzten beiden Kursabenden! 🚀**

Die Studierenden haben bereits viel gelernt. Jetzt ist es Zeit, das Wissen anzuwenden und Erfolgserlebnisse zu schaffen!
