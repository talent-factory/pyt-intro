# Product Requirement Prompt (PRP): Python-Schachprogramm

**Erstellt am**: 2025-10-29
**Projektstatus**: Planung
**Zielgruppe**: Python-Fortgeschrittenenkurs (Demonstrationsprojekt)
**Voraussetzungen**: Abgeschlossener Python-Einführungskurs (Kursabend 1-5), 30+ Stunden Programmiererfahrung

---

## Inhaltsverzeichnis

1. [Glossar](#glossar)
2. [Executive Summary](#executive-summary)
3. [Projektziele und Motivation](#projektziele-und-motivation)
4. [Zielgruppe und Use Cases](#zielgruppe-und-use-cases)
5. [Funktionale Anforderungen](#funktionale-anforderungen)
6. [Technische Spezifikation](#technische-spezifikation)
7. [Architektur und Design](#architektur-und-design)
8. [User Interface und User Experience](#user-interface-und-user-experience)
9. [Implementierungsplan](#implementierungsplan)
10. [Testing und Qualitätssicherung](#testing-und-qualitätssicherung)
11. [Typische Anfängerfehler und Lösungsstrategien](#typische-anfängerfehler-und-lösungsstrategien)
12. [Ressourcen und Referenzen](#ressourcen-und-referenzen)
13. [Erfolgskriterien](#erfolgskriterien)
14. [Risiken und Herausforderungen](#risiken-und-herausforderungen)

---

## Glossar

Wichtige Begriffe, die in diesem Dokument verwendet werden. Diese Konzepte sind zentral für das Verständnis des Schachprogramms.

### Schach-spezifische Begriffe

- **PGN (Portable Game Notation)**: Standardformat für Schachpartien. Eine Textdatei, die alle Züge einer Partie sowie Metadaten (Spieler, Datum, Ergebnis) enthält. Beispiel:
  ```
  [Event "Casual Game"]
  [White "Alice"]
  [Black "Bob"]

  1. e4 e5 2. Nf3 Nc6
  ```

- **FEN (Forsyth-Edwards Notation)**: Kompakte Darstellung einer Schachstellung als String. Beschreibt Position aller Figuren, wer am Zug ist, Rochaderechte etc. Beispiel für Startposition:
  ```
  rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1
  ```

- **UCI (Universal Chess Interface)**: Standardprotokoll zur Kommunikation mit Schach-Engines. Ermöglicht Integration externer KI-Engines wie Stockfish.

- **Algebraische Notation**: Standard-Zugnotation im Schach. Format: `[Figur][Startfeld][Zielfeld]`, z.B. `Nf3` (Springer nach f3) oder `e2e4` (Bauer von e2 nach e4).

- **Rochade**: Spezieller Doppelzug von König und Turm. Wichtig: Mehrere Bedingungen müssen erfüllt sein (König/Turm nicht bewegt, keine Figuren dazwischen, König nicht im Schach).

- **En Passant**: Sonderzug beim Bauernschlag. Kann auftreten, wenn gegnerischer Bauer zwei Felder vorrückt und dabei ein eigenes Bauernfeld "überspringt".

- **Bauernumwandlung**: Erreicht ein Bauer die gegnerische Grundreihe, wird er in Dame, Turm, Läufer oder Springer umgewandelt (meist Dame).

### Algorithmen und KI

- **Minimax-Algorithmus**: Entscheidungsfindungs-Algorithmus für Zwei-Spieler-Spiele. Berechnet rekursiv beste Züge unter der Annahme, dass der Gegner optimal spielt.
  - **Funktionsweise**: Baumartige Suche aller möglichen Züge bis zu einer bestimmten Tiefe
  - **Bewertung**: Stellungen werden numerisch bewertet (positiv = gut für Weiß, negativ = gut für Schwarz)
  - **Entscheidung**: Wählt Zug mit maximalem Minimal-Wert (daher "Minimax")

- **Alpha-Beta Pruning**: Optimierung von Minimax. Schneidet Äste im Suchbaum ab, die das Ergebnis nicht beeinflussen können.
  - **Effekt**: Reduziert Suchraum massiv (oft 50-90% weniger Knoten)
  - **Wichtig**: Findet exakt gleiches Ergebnis wie Minimax, nur schneller
  - **Vorteil**: Ermöglicht tiefere Suche in gleicher Zeit

- **Stellungsbewertung (Evaluation)**: Funktion, die eine Schachposition numerisch bewertet.
  - **Material**: Summe der Figurenwerte (Dame=9, Turm=5, Läufer/Springer=3, Bauer=1)
  - **Position**: Bonus für günstige Figurenstellungen (z.B. Springer in der Mitte)
  - **Mobilität**: Anzahl möglicher Züge (mehr = besser)

- **Suchtiefe (Depth)**: Wie viele Züge vorausschauend die KI rechnet.
  - **Depth 1**: Nur eigener nächster Zug
  - **Depth 2**: Eigener Zug + gegnerische Antwort
  - **Depth 3**: 1.5 Züge voraus (eigener Zug, Gegner, eigener Zug)
  - **Exponentielles Wachstum**: Jede Tiefe vervielfacht Rechenaufwand

### Programmier-Konzepte

- **MVC (Model-View-Controller)**: Architektur-Pattern zur Trennung von Datenmodell, Darstellung und Steuerungslogik.
  - **Model**: Spieldaten (chess.Board, Spielstand)
  - **View**: GUI (pygame Rendering)
  - **Controller**: Event-Handling, Spiellogik

- **Event-Loop**: Hauptschleife eines GUI-Programms. Verarbeitet fortlaufend Ereignisse (Mausklicks, Tastatur, Timer) und aktualisiert Anzeige.

- **Drag-and-Drop**: Interaktionsmuster zum Verschieben von Objekten per Maus.
  - **MouseDown**: Objekt auswählen
  - **MouseMotion**: Objekt bewegen
  - **MouseUp**: Objekt platzieren

- **State Management**: Verwaltung des Programmzustands (aktueller Spielstand, Spielmodus, Menüs etc.)

- **Abstrakte Basisklasse (ABC)**: Klasse, die nicht direkt instanziiert werden kann, sondern als Vorlage für Unterklassen dient. Definiert Interface, das Unterklassen implementieren müssen.

### Python-Bibliotheken

- **python-chess**: Bibliothek mit vollständiger Schachlogik. Übernimmt Zugvalidierung, Regelprüfung, PGN-Handling. Erspart manuelles Implementieren aller Schachregeln.

- **Pygame**: Bibliothek für 2D-Spiele und Multimedia. Bietet Fenster-Management, Grafik-Rendering, Event-Handling, Sound.

- **pytest**: Test-Framework für Python. Ermöglicht automatisierte Unit- und Integration-Tests.

---

## Executive Summary

Dieses Dokument beschreibt die Anforderungen für ein **vollständiges Schachprogramm in Python** mit grafischer Benutzeroberfläche (Pygame). Das Programm dient als **Demonstrationsprojekt** für einen Python-Fortgeschrittenenkurs und zeigt fortgeschrittene Konzepte wie objektorientierte Programmierung, GUI-Entwicklung, Dateiverarbeitung und Event-Handling.

**Hinweis**: Dieses Projekt richtet sich an Studierende, die den Python-Einführungskurs (Kursabend 1-5) bereits abgeschlossen haben und ihre Kenntnisse vertiefen möchten.

### Kernfeatures

- ♟️ **2-Spieler-Modus**: Zwei Spieler am gleichen Computer
- 🤖 **Computergegner (KI)**: Einfache KI mit verschiedenen Schwierigkeitsgraden
- 💾 **Spielstand speichern/laden**: Persistierung im PGN-Format
- 📜 **Zughistorie**: Vollständige Zugliste mit Undo-Funktion
- 🎨 **Grafische Oberfläche**: Pygame-basiertes UI mit Drag-and-Drop

### Technische Basis

- **Programmiersprache**: Python 3.9+
- **Schachlogik**: `python-chess` Bibliothek (v1.11+)
- **GUI-Framework**: Pygame (v2.5+)
- **Package Manager**: uv (gemäß Repository-Standard)

---

## Projektziele und Motivation

### Pädagogische Ziele

1. **OOP-Konzepte demonstrieren**
   - Klassen für Schachbrett, Spieler, KI-Engine
   - Vererbung (verschiedene Spielertypen)
   - Kapselung (Trennung von Logik und UI)

2. **Externe Bibliotheken nutzen**
   - `python-chess` für Schachregeln
   - Pygame für Grafik und Events
   - Integration externer Abhängigkeiten

3. **Software-Architektur zeigen**
   - MVC-Pattern (Model-View-Controller)
   - Modularisierung (separate Module für UI, Logik, KI)
   - Testbare Komponenten

4. **Dateiverarbeitung praktizieren**
   - PGN-Format lesen/schreiben
   - Konfigurationsdateien
   - Fehlerbehandlung bei I/O

5. **Event-Driven Programming**
   - Pygame Event Loop
   - Callback-Funktionen
   - State Management

### Motivation für Studierende

- **Greifbares Endprodukt**: Ein spielbares Schachspiel
- **Erweiterbarkeit**: Einfach weitere Features hinzuzufügen
- **Portfolio-Projekt**: Zeigbares Projekt für Bewerbungen
- **Gamification**: Lernen durch Spielentwicklung

---

## Zielgruppe und Use Cases

### Primäre Zielgruppe

**Studierende** des Python-Einführungskurses nach Kursabend 5, die:
- Grundlegende Python-Syntax beherrschen
- OOP-Konzepte verstehen
- Mit Dateioperationen vertraut sind
- Ein größeres Projekt umsetzen möchten

### Sekundäre Zielgruppe

**Kursleiter**, die das Projekt nutzen als:
- Live-Coding-Demonstration
- Referenzimplementierung für Best Practices
- Basis für Code-Reviews
- Beispiel für Projektstrukturierung

### Use Cases

#### UC1: Zwei Spieler spielen eine Schachpartie

**Akteure**: Zwei menschliche Spieler (Weiß, Schwarz)

**Ablauf**:
1. Programm starten
2. "2-Spieler-Modus" wählen
3. Abwechselnd Züge machen durch Drag-and-Drop
4. Programm validiert Züge automatisch
5. Bei Matt/Remis: Ergebnis anzeigen

**Erfolgskriterium**: Vollständige Partie ohne Fehler spielbar

#### UC2: Gegen Computer spielen

**Akteure**: Menschlicher Spieler, KI

**Ablauf**:
1. Programm starten
2. "Gegen Computer" wählen
3. Schwierigkeitsgrad auswählen (Einfach/Mittel/Schwer)
4. Farbe wählen (Weiß/Schwarz)
5. Spieler macht Zug
6. Computer antwortet automatisch
7. Spiel fortsetzen bis Ende

**Erfolgskriterium**: KI macht legale Züge in angemessener Zeit (<2s)

#### UC3: Spiel speichern und später fortsetzen

**Akteure**: Beliebiger Spieler

**Ablauf**:
1. Während eines Spiels: "Speichern" klicken
2. Dateiname eingeben (oder Standard verwenden)
3. Spiel wird im PGN-Format gespeichert
4. Programm beenden
5. Programm später neu starten
6. "Spiel laden" wählen
7. Gespeicherte Datei auswählen
8. Spiel wird an exakter Position fortgesetzt

**Erfolgskriterium**: Alle Züge und Spielzustand korrekt wiederhergestellt

#### UC4: Zughistorie durchschauen und rückgängig machen

**Akteure**: Beliebiger Spieler

**Ablauf**:
1. Während eines Spiels: Zughistorie-Panel sichtbar
2. Alle bisherigen Züge in Standard-Notation angezeigt
3. "Undo"-Button klicken
4. Letzter Zug wird rückgängig gemacht
5. Ggf. mehrfach wiederholen

**Erfolgskriterium**: Beliebig viele Züge können rückgängig gemacht werden

---

## Funktionale Anforderungen

### Must-Have Features (MVP)

#### F1: Schachbrett-Darstellung

- **F1.1**: 8x8 Schachbrett grafisch darstellen
- **F1.2**: Helle und dunkle Felder abwechselnd
- **F1.3**: Koordinaten anzeigen (a-h, 1-8)
- **F1.4**: Figuren als Symbole oder Bilder darstellen

#### F2: Spielmechanik

- **F2.1**: Züge per Drag-and-Drop oder Klick-Auswahl
- **F2.2**: Legale Züge hervorheben beim Auswählen einer Figur
- **F2.3**: Automatische Zugvalidierung (nur legale Züge erlaubt)
- **F2.4**: Rochade, En Passant, Bauernumwandlung korrekt implementiert
- **F2.5**: Schach-, Matt- und Remis-Erkennung
- **F2.6**: Spieler wechselt automatisch nach jedem Zug

#### F3: Spielmodi

- **F3.1**: 2-Spieler-Modus (Mensch vs. Mensch)
- **F3.2**: Einzelspieler-Modus (Mensch vs. Computer)
- **F3.3**: Farbauswahl (als Weiß oder Schwarz spielen)

#### F4: Computer-Gegner

- **F4.1**: Einfache KI (Random-Züge oder simple Evaluation)
- **F4.2**: Mittlere KI (Minimax mit Alpha-Beta-Pruning, Suchtiefe 2-3)
- **F4.3**: Schwere KI (Minimax, Suchtiefe 4-5, Positionsauswertung)
- **F4.4**: KI-Züge mit kurzer Verzögerung (0.5-1s) für natürlicheres Gefühl
- **F4.5**: Indikator wenn Computer "nachdenkt"

#### F5: Spielstand-Persistierung

- **F5.1**: Spiel im PGN-Format speichern
- **F5.2**: PGN-Dateien laden
- **F5.3**: Mehrere Speicherstände verwalten
- **F5.4**: Metadaten speichern (Datum, Spieler, Modus)

#### F6: Zughistorie

- **F6.1**: Liste aller Züge in Standardnotation (e2-e4)
- **F6.2**: Zugnummer und Spieler anzeigen
- **F6.3**: Undo-Funktion (einzelner Zug rückgängig)
- **F6.4**: Mehrfaches Undo möglich
- **F6.5**: Im 2-Spieler-Modus: Beide Züge rückgängig machen

### Should-Have Features

#### F7: Erweiterte UI-Features

- **F7.1**: Letzter Zug visuell hervorheben
- **F7.2**: Bedrohte Figuren markieren
- **F7.3**: Animationen für Züge
- **F7.4**: Sound-Effekte (Zuggeräusch, Schach, Matt)

#### F8: Spielstatistiken

- **F8.1**: Anzahl Züge
- **F8.2**: Spielzeit
- **F8.3**: Geschlagene Figuren anzeigen
- **F8.4**: Materialvorteil berechnen

#### F9: Analyse-Features

- **F9.1**: Stellungsbewertung anzeigen
- **F9.2**: Zugvorschläge (Hints)
- **F9.3**: Export in verschiedene Formate (PNG, FEN)

### Nice-to-Have Features

#### F10: Zusatzfeatures

- **F10.1**: Online-Multiplayer
- **F10.2**: Verschiedene Schachbrett-Designs
- **F10.3**: Notation-Varianten (algebraisch, beschreibend)
- **F10.4**: Eröffnungsdatenbank
- **F10.5**: Endspiel-Tablebases
- **F10.6**: Training-Modus mit Puzzles

---

## Technische Spezifikation

### Technologie-Stack

#### Core

```yaml
Python: ">=3.9,<3.13"
python-chess: "^1.11.2"
pygame: "^2.5.2"
```

#### Development

```yaml
pytest: "^8.0.0"        # Unit Tests
black: "^24.0.0"         # Code Formatting
ruff: "^0.3.0"           # Linting
mypy: "^1.9.0"           # Type Checking
```

### Dateistruktur

```
schach/
├── src/
│   ├── __init__.py
│   ├── main.py              # Entry Point
│   ├── gui/
│   │   ├── __init__.py
│   │   ├── board_renderer.py    # Schachbrett zeichnen
│   │   ├── piece_renderer.py    # Figuren zeichnen
│   │   ├── event_handler.py     # Event-Loop
│   │   ├── ui_components.py     # Buttons, Panels etc.
│   │   └── animations.py        # Zuganimationen
│   ├── game/
│   │   ├── __init__.py
│   │   ├── chess_game.py        # Game Controller
│   │   ├── player.py            # Spieler-Abstraktion
│   │   ├── human_player.py      # Menschlicher Spieler
│   │   ├── ai_player.py         # KI-Spieler
│   │   └── game_state.py        # Spielzustand
│   ├── ai/
│   │   ├── __init__.py
│   │   ├── engine.py            # KI-Engine (Minimax)
│   │   ├── evaluation.py        # Stellungsbewertung
│   │   └── openings.py          # Eröffnungsbuch (optional)
│   ├── persistence/
│   │   ├── __init__.py
│   │   ├── pgn_handler.py       # PGN I/O
│   │   └── config.py            # Konfiguration
│   └── utils/
│       ├── __init__.py
│       ├── constants.py         # Konstanten (Farben, Größen)
│       └── helpers.py           # Hilfsfunktionen
├── assets/
│   ├── images/
│   │   └── pieces/             # Figurenbilder (PNG)
│   │       ├── white_king.png
│   │       ├── white_queen.png
│   │       └── ...
│   └── sounds/                 # Sound-Dateien (optional)
│       ├── move.wav
│       ├── capture.wav
│       └── check.wav
├── tests/
│   ├── __init__.py
│   ├── test_chess_game.py
│   ├── test_ai_engine.py
│   └── test_pgn_handler.py
├── saves/                      # Gespeicherte Spiele (PGN)
├── docs/
│   ├── architektur.md
│   ├── ki-algorithmus.md
│   └── anleitung.md
├── pyproject.toml
├── README.md
└── .gitignore
```

### Abhängigkeiten und Installation

#### Installation mit uv

```bash
# Repository klonen
git clone <repo-url>
cd pyt-intro

# In Schach-Verzeichnis wechseln
cd schach

# Abhängigkeiten installieren
uv sync

# Programm starten
uv run python src/main.py
```

#### Abhängigkeitserklärung in pyproject.toml

```toml
[project]
name = "python-schachprogramm"
version = "1.0.0"
description = "Schachprogramm mit Pygame-GUI für Python-Einführungskurs"
authors = [{name = "Daniel", email = ""}]
requires-python = ">=3.9,<3.13"
dependencies = [
    "python-chess>=1.11.2",
    "pygame>=2.5.2",
]

[project.optional-dependencies]
dev = [
    "pytest>=8.0.0",
    "black>=24.0.0",
    "ruff>=0.3.0",
    "mypy>=1.9.0",
]

[tool.black]
line-length = 100
target-version = ['py39']

[tool.ruff]
line-length = 100
target-version = "py39"

[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
```

### Datenmodelle

#### ChessGame

```python
from dataclasses import dataclass
from typing import Optional, List
import chess

@dataclass
class ChessGame:
    """
    Hauptspielklasse - verwaltet Spielzustand.

    Attributes:
        board: python-chess Board-Objekt
        white_player: Weißer Spieler (Mensch oder KI)
        black_player: Schwarzer Spieler (Mensch oder KI)
        current_player: Aktiver Spieler
        move_history: Liste aller Züge
        game_over: Spiel beendet?
        winner: Gewinner (None bei Remis)
    """
    board: chess.Board
    white_player: 'Player'
    black_player: 'Player'
    current_player: 'Player'
    move_history: List[chess.Move]
    game_over: bool = False
    winner: Optional[str] = None
```

#### Player (Abstrakte Basisklasse)

```python
from abc import ABC, abstractmethod
import chess

class Player(ABC):
    """
    Abstrakte Basisklasse für Spieler.
    """

    def __init__(self, color: chess.Color, name: str):
        """
        Args:
            color: Spielerfarbe (chess.WHITE oder chess.BLACK)
            name: Spielername
        """
        self.color = color
        self.name = name

    @abstractmethod
    def get_move(self, board: chess.Board) -> chess.Move:
        """
        Fordert Zug vom Spieler an.

        Args:
            board: Aktueller Spielstand

        Returns:
            Gewählter Zug
        """
        pass
```

#### HumanPlayer

```python
class HumanPlayer(Player):
    """
    Menschlicher Spieler - Züge via GUI.
    """

    def get_move(self, board: chess.Board) -> chess.Move:
        """
        Wartet auf GUI-Eingabe.
        """
        # Implementierung in GUI Event Handler
        pass
```

#### AIPlayer

```python
class AIPlayer(Player):
    """
    KI-Spieler mit Minimax-Algorithmus.

    Attributes:
        difficulty: Schwierigkeitsgrad (1-3)
        max_depth: Maximale Suchtiefe
    """

    def __init__(self, color: chess.Color, name: str, difficulty: int = 2):
        super().__init__(color, name)
        self.difficulty = difficulty
        self.max_depth = {1: 2, 2: 3, 3: 5}[difficulty]

    def get_move(self, board: chess.Board) -> chess.Move:
        """
        Berechnet besten Zug mit Minimax.
        """
        return minimax_search(board, self.max_depth)
```

### Schnittstellen

#### python-chess Integration

Das `python-chess` Paket stellt folgende Kernfunktionalität bereit:

```python
import chess

# Board erstellen
board = chess.Board()

# Züge machen
move = chess.Move.from_uci("e2e4")  # UCI-Notation
board.push(move)

# Züge rückgängig machen
board.pop()

# Legale Züge
legal_moves = list(board.legal_moves)

# Spielstatus
is_checkmate = board.is_checkmate()
is_stalemate = board.is_stalemate()
is_check = board.is_check()

# PGN Export/Import
from chess import pgn
game = pgn.Game()
game.headers["Event"] = "Test"
# ... Züge hinzufügen
print(game)  # PGN-String
```

#### Pygame Integration

Grundlegende Event-Loop:

```python
import pygame

def main_loop():
    """
    Haupt-Event-Loop des Spiels.
    """
    clock = pygame.time.Clock()
    running = True

    while running:
        # Events verarbeiten
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                handle_mouse_click(event.pos)
            elif event.type == pygame.MOUSEBUTTONUP:
                handle_mouse_release(event.pos)
            elif event.type == pygame.MOUSEMOTION:
                handle_mouse_drag(event.pos)

        # Zeichnen
        screen.fill(BACKGROUND_COLOR)
        draw_board()
        draw_pieces()
        draw_ui()

        pygame.display.flip()
        clock.tick(60)  # 60 FPS
```

---

## Architektur und Design

### Architektur-Muster: MVC (Model-View-Controller)

```
┌─────────────────────────────────────────────────┐
│                    View (GUI)                    │
│  - board_renderer.py                            │
│  - piece_renderer.py                            │
│  - ui_components.py                             │
└─────────────┬───────────────────────────────────┘
              │
              ↓ Events (Mouse, Keyboard)
┌─────────────────────────────────────────────────┐
│              Controller (Game Logic)             │
│  - event_handler.py                             │
│  - chess_game.py                                │
└─────────────┬───────────────────────────────────┘
              │
              ↓ Updates
┌─────────────────────────────────────────────────┐
│                Model (Data)                      │
│  - chess.Board (python-chess)                   │
│  - game_state.py                                │
│  - player.py                                    │
└─────────────────────────────────────────────────┘
```

### Komponenten-Übersicht

#### 1. GUI-Komponenten (View)

**board_renderer.py**
- Zeichnet das 8x8 Schachbrett
- Koordinaten-Labels
- Hervorhebungen (legale Züge, letzter Zug)

**piece_renderer.py**
- Lädt und zeichnet Figurenbilder
- Drag-and-Drop-Visualisierung
- Animationen

**ui_components.py**
- Buttons (Neu, Speichern, Laden, Undo)
- Zughistorie-Panel
- Info-Panel (Spielstand, Status)
- Menüs

#### 2. Game Logic (Controller)

**event_handler.py**
- Verarbeitet Pygame-Events
- Konvertiert Mausklicks zu Schachfeldern
- Delegiert an ChessGame

**chess_game.py**
- Zentrale Spielsteuerung
- Zugvalidierung (via python-chess)
- Spielerwechsel
- Win/Loss/Draw-Erkennung

#### 3. Daten und Persistierung (Model)

**game_state.py**
- Kapselung von chess.Board
- Zusätzliche Metadaten (Zeit, Statistiken)

**pgn_handler.py**
- Speichert Spiele im PGN-Format
- Lädt PGN-Dateien
- Validierung

#### 4. KI-Engine

**engine.py**
- Minimax-Algorithmus mit Alpha-Beta-Pruning
- Iterative Deepening (optional)
- Transposition Table (optional)

**evaluation.py**
- Materialzählung
- Positionelle Bewertung
- Mobilitätsbewertung

### Klassendiagramm (UML)

```
┌─────────────────────┐
│   ChessGame         │
├─────────────────────┤
│ - board: Board      │
│ - white: Player     │
│ - black: Player     │
├─────────────────────┤
│ + make_move()       │
│ + undo_move()       │
│ + is_game_over()    │
└──────────┬──────────┘
           │
           │ has-a
           ↓
┌─────────────────────┐
│   Player (ABC)      │
├─────────────────────┤
│ - color: Color      │
│ - name: str         │
├─────────────────────┤
│ + get_move()        │◄────────────┐
└─────────────────────┘             │
           △                        │
           │ extends                │
           │                        │
    ┌──────┴──────┐                │
    │             │                │
┌───────────┐ ┌──────────┐         │
│HumanPlayer│ │AIPlayer  │         │
└───────────┘ └──────────┘         │
                   │                │
                   │ uses           │
                   ↓                │
             ┌──────────┐           │
             │  Engine  │           │
             └──────────┘           │
                                    │
┌─────────────────────┐             │
│  BoardRenderer      │             │
├─────────────────────┤             │
│ + draw_board()      │─────uses────┘
│ + draw_pieces()     │
└─────────────────────┘
```

### Sequenzdiagramm: Menschlicher Zug

```
User         GUI           EventHandler    ChessGame     Board (python-chess)
 │            │                 │             │                 │
 │ Click      │                 │             │                 │
 ├───────────►│                 │             │                 │
 │            │ handle_click()  │             │                 │
 │            ├────────────────►│             │                 │
 │            │                 │ select_piece()               │
 │            │                 ├────────────►│                 │
 │            │                 │             │ legal_moves()   │
 │            │                 │             ├────────────────►│
 │            │◄────highlight───┤◄────return──┤◄───────────────┤
 │            │                 │             │                 │
 │ Release    │                 │             │                 │
 ├───────────►│                 │             │                 │
 │            │ handle_release()│             │                 │
 │            ├────────────────►│             │                 │
 │            │                 │ make_move() │                 │
 │            │                 ├────────────►│ push_san()      │
 │            │                 │             ├────────────────►│
 │            │                 │             │                 │
 │            │◄────update──────┤◄────return──┤◄───────────────┤
 │◄───render──┤                 │             │                 │
```

### Sequenzdiagramm: KI-Zug

```
ChessGame    AIPlayer      Engine         Evaluation    Board
    │            │            │               │           │
    │ get_move() │            │               │           │
    ├───────────►│            │               │           │
    │            │ minimax()  │               │           │
    │            ├───────────►│               │           │
    │            │            │ evaluate()    │           │
    │            │            ├──────────────►│           │
    │            │            │               │ count()   │
    │            │            │               ├──────────►│
    │            │            │               │◄──────────┤
    │            │            │◄──────────────┤           │
    │            │◄───────────┤               │           │
    │◄───return──┤            │               │           │
    │ push()     │            │               │           │
    ├───────────────────────────────────────────────────►│
```

### State Machine: Spielablauf

```
┌──────────┐
│  START   │
└────┬─────┘
     │
     ↓
┌──────────────┐
│ MENU         │
│ - Neues Spiel│
│ - Laden      │
│ - Beenden    │
└────┬─────────┘
     │ Neue Partie
     ↓
┌──────────────┐
│ SETUP        │
│ - Modus      │
│ - Farbe      │
│ - Schwierig. │
└────┬─────────┘
     │
     ↓
┌──────────────┐
│ PLAYING      │◄─────┐
│ - Zug warten │      │
│ - Validieren │      │
│ - Ausführen  │      │
└────┬─────────┘      │
     │                │
     ├─ Zug gemacht ──┘
     │
     ├─ Speichern ────► SAVE_DIALOG
     │
     ├─ Undo ─────────► PLAYING (vorheriger Zustand)
     │
     ↓ Matt/Remis
┌──────────────┐
│ GAME_OVER    │
│ - Ergebnis   │
│ - Statistik  │
└────┬─────────┘
     │
     ↓ Neue Partie oder Beenden
┌──────────┐
│   END    │
└──────────┘
```

---

## User Interface und User Experience

### UI-Layout

```
┌───────────────────────────────────────────────────────────────────┐
│  Python-Schach                                          [─][□][×] │
├───────────────────────────────────────────────────────────────────┤
│  [Neu]  [Laden]  [Speichern]  [Undo]  [Optionen]                 │
├──────────────────────────────┬────────────────────────────────────┤
│                              │  Zughistorie                       │
│                              │  ────────────────                  │
│     8 ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜       │  1. e2-e4    e7-e5               │
│     7 ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟       │  2. Nf3      Nc6                 │
│     6 · · · · · · · ·       │  3. Bb5      a6                  │
│     5 · · · · · · · ·       │  4. ...                          │
│     4 · · · · ♙ · · ·       │                                    │
│     3 · · · · · · · ·       │  ────────────────                  │
│     2 ♙ ♙ ♙ ♙ · ♙ ♙ ♙       │                                    │
│     1 ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖       │  Status                            │
│       a b c d e f g h       │  ────────────────                  │
│                              │  Weiß am Zug                       │
│                              │                                    │
│                              │  Geschlagene Figuren               │
│                              │  Schwarz: ♟ ♟                    │
│                              │  Weiß:    ♙                       │
└──────────────────────────────┴────────────────────────────────────┘
```

### Farbschema

```python
# constants.py

# Schachbrett
HELL_FELD = (240, 217, 181)    # Beige
DUNKEL_FELD = (181, 136, 99)   # Braun

# UI
HINTERGRUND = (49, 46, 43)     # Dunkelgrau
TEXT_FARBE = (255, 255, 255)   # Weiß
BUTTON_NORMAL = (70, 130, 180) # Stahlblau
BUTTON_HOVER = (100, 149, 237) # Kornblumenblau

# Hervorhebungen
AUSWAHL = (255, 255, 0, 100)   # Gelb, halbtransparent
LEGALER_ZUG = (0, 255, 0, 80)  # Grün, halbtransparent
LETZTER_ZUG = (255, 200, 0, 100) # Orange
SCHACH = (255, 0, 0, 100)      # Rot
```

### Größen und Abstände

```python
# Layout
FENSTER_BREITE = 1200
FENSTER_HOEHE = 800

# Schachbrett
BRETT_GROESSE = 600
FELD_GROESSE = BRETT_GROESSE // 8  # 75px
BRETT_OFFSET_X = 50
BRETT_OFFSET_Y = 100

# Seitenleiste
SIDEBAR_BREITE = 400
SIDEBAR_X = BRETT_OFFSET_X + BRETT_GROESSE + 50

# UI-Elemente
BUTTON_BREITE = 100
BUTTON_HOEHE = 40
BUTTON_ABSTAND = 10
```

### Interaktions-Design

#### Drag-and-Drop

1. **Mausklick auf Figur**
   - Figur auswählen
   - Legale Züge grün hervorheben
   - Figur "schwebt" unter Mauszeiger

2. **Maus bewegen**
   - Figur folgt Mauszeiger
   - Zielfeld wird bei Hover hervorgehoben

3. **Maus loslassen**
   - Auf legalem Feld: Zug ausführen
   - Auf illegalem Feld: Figur zurück auf Startfeld
   - Zuganimation

#### Alternative: Click-to-Move

1. **Erster Klick**: Figur auswählen
2. **Zweiter Klick**: Zielfeld
3. Bei illegalem Zug: Fehlermeldung

### Fehlerbehandlung und Feedback

```python
def zeige_fehler(nachricht: str):
    """
    Zeigt Fehlermeldung als Overlay an.

    Args:
        nachricht: Fehlermeldung
    """
    # Rotes Popup mit Text
    # Automatisch nach 3 Sekunden ausblenden
    pass

def zeige_erfolg(nachricht: str):
    """
    Zeigt Erfolgsmeldung an.

    Args:
        nachricht: Erfolgsmeldung
    """
    # Grünes Popup
    pass

# Beispiele:
zeige_fehler("Illegaler Zug! Der König steht im Schach.")
zeige_erfolg("Spiel erfolgreich gespeichert.")
```

### Barrierefreiheit

- **Tastatur-Navigation**: Alle Funktionen per Tastatur bedienbar
  - Pfeiltasten: Figur auswählen
  - Enter: Zug bestätigen
  - Strg+Z: Undo
  - Strg+S: Speichern

- **Kontrast**: Hohe Kontraste zwischen Feldern und Figuren

- **Schriftgröße**: Gut lesbare Schriften (≥14pt)

---

## Implementierungsplan

### Phase 1: Grundgerüst (Woche 1)

#### Aufgaben

1. **Projektstruktur erstellen**
   - Verzeichnisse anlegen
   - `pyproject.toml` konfigurieren
   - Git-Repository initialisieren

2. **Basis-Klassen implementieren**
   - `Player` (abstrakt)
   - `HumanPlayer` (Stub)
   - `AIPlayer` (Stub)
   - `ChessGame` (grundlegend)

3. **Pygame-Setup**
   - Fenster erstellen
   - Event-Loop
   - Grundlegende Zeichenfunktionen

4. **Schachbrett zeichnen**
   - 8x8 Gitter
   - Koordinaten
   - Feldfarben

**Deliverables**:
- Lauffähiges Programm, das leeres Schachbrett anzeigt
- Grundlegende Projektstruktur

**Zeitaufwand**: ~5 Stunden

---

### Phase 2: Spielmechanik (Woche 2-3)

#### Aufgaben

1. **Figuren-Rendering**
   - Bilder laden (oder Unicode-Symbole)
   - Figuren auf Brett zeichnen
   - Startposition

2. **python-chess Integration**
   - Board-Objekt erstellen
   - Züge aus python-chess auslesen und anzeigen

3. **Drag-and-Drop**
   - Mausklick-Erkennung auf Feldern
   - Figurauswahl
   - Drag-Visualisierung
   - Drop und Zugausführung

4. **Zugvalidierung**
   - Nur legale Züge erlauben
   - Legale Züge hervorheben

5. **Spielerwechsel**
   - Automatischer Wechsel nach Zug
   - Anzeige des aktiven Spielers

**Deliverables**:
- 2-Spieler-Modus funktionsfähig
- Alle Schachregeln korrekt implementiert (via python-chess)

**Zeitaufwand**: ~12 Stunden

---

### Phase 3: KI-Gegner (Woche 4)

#### Aufgaben

1. **Minimax-Algorithmus**
   - Grundlegender Minimax
   - Alpha-Beta-Pruning
   - Suchtiefe-Parameter

2. **Stellungsbewertung**
   - Materialzählung
   - Einfache Positionsbewertung
   - Mobilitätsbewertung (optional)

3. **AIPlayer implementieren**
   - `get_move()` mit Minimax
   - Schwierigkeitsgrade (Suchtiefe)
   - Threading (KI-Berechnung nicht blockierend)

4. **UI-Integration**
   - "Gegen Computer" Menü
   - Schwierigkeitsauswahl
   - Farbauswahl
   - "Computer denkt..."-Anzeige

**Deliverables**:
- Spielbare KI auf 3 Schwierigkeitsstufen
- Flüssige Integration ohne UI-Freezing

**Zeitaufwand**: ~15 Stunden

---

### Phase 4: Persistierung und Historie (Woche 5)

#### Aufgaben

1. **PGN-Handler**
   - PGN-Export implementieren
   - PGN-Import implementieren
   - Datei-Dialoge (pygame-gui oder tkinter)

2. **Zughistorie-Panel**
   - Liste aller Züge anzeigen
   - Scrollen bei vielen Zügen
   - Formatierung (Zugnummer, Notation)

3. **Undo-Funktion**
   - Einzelnen Zug rückgängig
   - Mehrfaches Undo
   - Undo im 2-Spieler-Modus (beide Züge)

4. **Menü-System**
   - Neues Spiel
   - Spiel speichern
   - Spiel laden
   - Optionen
   - Beenden

**Deliverables**:
- Vollständige Save/Load-Funktionalität
- Zughistorie mit Undo

**Zeitaufwand**: ~10 Stunden

---

### Phase 5: Polish und Testing (Woche 6)

#### Aufgaben

1. **UI-Verbesserungen**
   - Animationen für Züge
   - Sound-Effekte (optional)
   - Letzter Zug hervorheben
   - Status-Anzeigen (Schach, Matt)

2. **Testing**
   - Unit Tests für ChessGame
   - Unit Tests für AI Engine
   - Integration Tests
   - Manuelle Tests (Spielbarkeit)

3. **Dokumentation**
   - README.md
   - Architektur-Dokumentation
   - KI-Algorithmus-Erklärung
   - Benutzer-Anleitung

4. **Code-Qualität**
   - Code-Formatting mit Black
   - Linting mit Ruff
   - Type Checking mit mypy
   - Docstrings vervollständigen

5. **Bug-Fixes**
   - Edge-Cases fixen
   - Performance-Optimierungen

**Deliverables**:
- Vollständig getestetes Programm
- Umfassende Dokumentation
- Release-fähiger Code

**Zeitaufwand**: ~10 Stunden

---

### Gesamtzeitaufwand

**Total**: ~52 Stunden (ca. 1,5 Monate bei 8h/Woche)

---

## Testing und Qualitätssicherung

### Test-Strategie

#### Unit Tests

**game/chess_game.py**

```python
# tests/test_chess_game.py
import pytest
import chess
from src.game.chess_game import ChessGame
from src.game.human_player import HumanPlayer

def test_chess_game_initialisierung():
    """Testet korrekte Initialisierung eines Spiels."""
    white = HumanPlayer(chess.WHITE, "Weiß")
    black = HumanPlayer(chess.BLACK, "Schwarz")
    game = ChessGame(white, black)

    assert game.board.turn == chess.WHITE
    assert len(list(game.board.legal_moves)) == 20
    assert not game.game_over

def test_legaler_zug():
    """Testet Ausführung eines legalen Zugs."""
    white = HumanPlayer(chess.WHITE, "Weiß")
    black = HumanPlayer(chess.BLACK, "Schwarz")
    game = ChessGame(white, black)

    move = chess.Move.from_uci("e2e4")
    result = game.make_move(move)

    assert result == True
    assert game.board.turn == chess.BLACK
    assert len(game.move_history) == 1

def test_illegaler_zug():
    """Testet Ablehnung eines illegalen Zugs."""
    white = HumanPlayer(chess.WHITE, "Weiß")
    black = HumanPlayer(chess.BLACK, "Schwarz")
    game = ChessGame(white, black)

    # Illegaler Zug: König zwei Felder vorwärts
    illegal_move = chess.Move.from_uci("e1e3")
    result = game.make_move(illegal_move)

    assert result == False
    assert len(game.move_history) == 0

def test_schachmatt():
    """Testet Matt-Erkennung (Narrenmatt)."""
    white = HumanPlayer(chess.WHITE, "Weiß")
    black = HumanPlayer(chess.BLACK, "Schwarz")
    game = ChessGame(white, black)

    # Narrenmatt-Sequenz
    game.make_move(chess.Move.from_uci("f2f3"))
    game.make_move(chess.Move.from_uci("e7e6"))
    game.make_move(chess.Move.from_uci("g2g4"))
    game.make_move(chess.Move.from_uci("d8h4"))  # Matt!

    assert game.board.is_checkmate()
    assert game.game_over
    assert game.winner == "Schwarz"
```

**ai/engine.py**

```python
# tests/test_ai_engine.py
import chess
from src.ai.engine import minimax_search, evaluate_position

def test_evaluation_startposition():
    """Testet Evaluation der Startposition (sollte ~0 sein)."""
    board = chess.Board()
    score = evaluate_position(board)
    assert -50 <= score <= 50  # Ungefähr ausgeglichen

def test_evaluation_materialvorteil():
    """Testet Evaluation bei Materialvorteil."""
    board = chess.Board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKB1R w KQkq - 0 1")
    # Weiß fehlt ein Springer (3 Punkte)
    score = evaluate_position(board)
    assert score < -200  # Schwarz hat Vorteil

def test_minimax_findet_matt_in_1():
    """KI sollte Matt in 1 Zug finden."""
    # Position mit Matt in 1 für Weiß
    board = chess.Board("3k4/8/3K4/8/8/8/8/R7 w - - 0 1")
    best_move = minimax_search(board, depth=2)
    board.push(best_move)
    assert board.is_checkmate()
```

**persistence/pgn_handler.py**

```python
# tests/test_pgn_handler.py
import os
import chess
from src.persistence.pgn_handler import save_game_to_pgn, load_game_from_pgn

def test_save_and_load_pgn(tmp_path):
    """Testet Speichern und Laden einer Partie."""
    # Testpartie erstellen
    board = chess.Board()
    board.push(chess.Move.from_uci("e2e4"))
    board.push(chess.Move.from_uci("e7e5"))

    # Speichern
    filepath = tmp_path / "test_game.pgn"
    save_game_to_pgn(board, filepath, event="Test", white="Alice", black="Bob")

    # Laden
    loaded_board = load_game_from_pgn(filepath)

    # Vergleichen
    assert len(list(loaded_board.move_stack)) == 2
    assert loaded_board.fen() == board.fen()
```

#### Integration Tests

```python
# tests/test_integration.py
def test_vollstaendige_partie():
    """Simuliert eine vollständige Partie."""
    white = HumanPlayer(chess.WHITE, "Weiß")
    black = HumanPlayer(chess.BLACK, "Schwarz")
    game = ChessGame(white, black)

    moves = [
        "e2e4", "e7e5",
        "g1f3", "b8c6",
        "f1c4", "f8c5",
        # ... weitere Züge
    ]

    for move_str in moves:
        move = chess.Move.from_uci(move_str)
        assert game.make_move(move)

    assert len(game.move_history) == len(moves)
```

### Test-Abdeckung

**Ziel**: Mindestens 80% Code Coverage

```bash
# Coverage-Report generieren
uv run pytest --cov=src --cov-report=html
```

### Manuelle Tests

#### Testfall 1: Einfaches 2-Spieler-Spiel

1. Programm starten
2. "Neues Spiel" → "2 Spieler"
3. 10 Züge spielen
4. Undo 2x drücken
5. Weiterspielen bis Matt/Remis

**Erwartung**: Flüssiger Ablauf, korrekte Zugvalidierung

#### Testfall 2: Gegen KI spielen

1. "Neues Spiel" → "Gegen Computer"
2. Schwierigkeit: Mittel
3. Farbe: Weiß
4. 20 Züge spielen

**Erwartung**: KI macht legale Züge in <2s

#### Testfall 3: Speichern und Laden

1. Neue Partie starten
2. 15 Züge spielen
3. "Speichern" → Datei wählen
4. Programm beenden
5. Neu starten → "Laden" → Datei wählen

**Erwartung**: Exakt gleiche Position wiederhergestellt

### Performance-Tests

```python
# tests/test_performance.py
import time
import chess
from src.ai.engine import minimax_search

def test_ki_performance():
    """KI sollte Züge in angemessener Zeit berechnen."""
    board = chess.Board()

    start = time.time()
    move = minimax_search(board, depth=3)
    duration = time.time() - start

    assert duration < 2.0  # Max 2 Sekunden für depth=3
```

---

## Typische Anfängerfehler und Lösungsstrategien

Dieses Kapitel dokumentiert häufige Fehler, die beim Implementieren des Schachprogramms auftreten können, sowie bewährte Lösungsstrategien. Es basiert auf Erfahrungen aus ähnlichen Projekten und hilft, typische Stolpersteine zu vermeiden.

### Kategorie 1: pygame-spezifische Fehler

#### Fehler 1.1: Pygame blockiert/friert ein

**Symptom**: Programm reagiert nicht mehr, Fenster wird grau/weiß, Betriebssystem meldet "Programm reagiert nicht".

**Ursache**: Event-Queue wird nicht regelmäßig geleert. pygame erwartet, dass Events in jedem Frame verarbeitet werden.

**Falsch**:
```python
# Keine Event-Verarbeitung in der Hauptschleife
while running:
    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()
    # ❌ Events werden nie verarbeitet!
```

**Richtig**:
```python
while running:
    # ✅ Events in jedem Frame verarbeiten
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # ... weitere Events

    screen.fill(WHITE)
    draw_board()
    pygame.display.flip()
```

**Lösung**: IMMER `pygame.event.get()` in jedem Durchlauf der Hauptschleife aufrufen, auch wenn Events nicht aktiv verarbeitet werden.

---

#### Fehler 1.2: Flackerndes/ruckelndes Bild

**Symptom**: Schachbrett flackert oder zeigt Artefakte beim Zeichnen.

**Ursache**: Kein Double Buffering oder fehlende FPS-Limitierung.

**Falsch**:
```python
screen = pygame.display.set_mode((800, 600))  # ❌ Kein Double Buffer
while running:
    # Zeichnen ohne FPS-Limit
    draw_everything()
    pygame.display.flip()
```

**Richtig**:
```python
# ✅ Double Buffering aktivieren (Standard bei flip())
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

while running:
    # Events...
    draw_everything()
    pygame.display.flip()
    clock.tick(60)  # ✅ 60 FPS Limit
```

**Lösung**:
1. `pygame.display.flip()` statt `update()` verwenden
2. `Clock.tick(60)` für stabile Framerate
3. Hintergrund vor jedem Zeichnen komplett neu füllen

---

#### Fehler 1.3: Mausklicks werden nicht erkannt

**Symptom**: Klicken auf Schachfelder hat keine Wirkung.

**Ursache**: Falsche Koordinaten-Umrechnung zwischen Pixel und Schachfeldern.

**Falsch**:
```python
def get_square_from_pos(pos):
    x, y = pos
    # ❌ Vergisst Board-Offset
    col = x // FELD_GROESSE
    row = y // FELD_GROESSE
    return col, row
```

**Richtig**:
```python
def get_square_from_pos(pos):
    x, y = pos
    # ✅ Berücksichtigt Board-Offset
    x -= BRETT_OFFSET_X
    y -= BRETT_OFFSET_Y

    # Prüfe ob Klick innerhalb des Bretts
    if x < 0 or y < 0 or x >= BRETT_GROESSE or y >= BRETT_GROESSE:
        return None

    col = x // FELD_GROESSE
    row = y // FELD_GROESSE
    return col, row
```

**Lösung**:
1. Board-Offset (Rand) von Pixelkoordinaten abziehen
2. Bounds-Checking: Klick außerhalb des Bretts abfangen
3. Koordinaten-Umrechnung testen mit `print()`-Statements

---

### Kategorie 2: python-chess Integration

#### Fehler 2.1: Verwechslung von Zeilen/Spalten

**Symptom**: Züge werden auf falsche Felder gemacht, Figuren "springen" an unerwartete Positionen.

**Ursache**: python-chess verwendet (file, rank), pygame/Array-Logik oft (row, col).

**Wichtig**:
- python-chess: `file` = Spalte (a-h = 0-7), `rank` = Zeile (1-8 = 0-7)
- Arrays: `board[row][col]` wobei row = Zeile von oben, col = Spalte

**Falsch**:
```python
# ❌ Vertauschte Koordinaten
square = chess.square(row, col)  # Falsch!
```

**Richtig**:
```python
# ✅ Korrekte Reihenfolge: file (Spalte), rank (Zeile)
square = chess.square(col, 7 - row)  # Zeile von unten zählen!

# Oder verwende explizite Namen:
file = col  # a-h
rank = 7 - row  # 1-8 von unten
square = chess.square(file, rank)
```

**Lösung**:
1. Hilfsfunktionen schreiben: `pygame_to_chess()` und `chess_to_pygame()`
2. Konsistente Namensgebung: `file`/`rank` vs. `col`/`row`
3. Schachbrett wird von unten gezählt (Zeile 0 = Reihe 1)

---

#### Fehler 2.2: Züge als Strings statt Move-Objekte

**Symptom**: `TypeError` oder Züge werden nicht erkannt.

**Ursache**: python-chess erwartet `chess.Move`-Objekte, nicht Strings.

**Falsch**:
```python
# ❌ String statt Move-Objekt
board.push("e2e4")  # TypeError!
```

**Richtig**:
```python
# ✅ Move-Objekt erstellen
move = chess.Move.from_uci("e2e4")
board.push(move)

# Oder aus Start/Ziel-Feldern:
from_square = chess.E2
to_square = chess.E4
move = chess.Move(from_square, to_square)
board.push(move)
```

**Lösung**:
1. Immer `chess.Move`-Objekte verwenden
2. Bei UCI-Notation: `chess.Move.from_uci(string)`
3. Bei SAN-Notation: `board.parse_san(string)`

---

#### Fehler 2.3: Bauernumwandlung vergessen

**Symptom**: Bauer erreicht letzte Reihe, aber nichts passiert oder Fehler.

**Ursache**: Bauernumwandlung muss explizit im Move angegeben werden.

**Falsch**:
```python
# ❌ Bauernumwandlung nicht angegeben
move = chess.Move(chess.E7, chess.E8)
board.push(move)  # Fehler oder undefined behavior!
```

**Richtig**:
```python
# ✅ Umwandlungsfigur angeben
move = chess.Move(chess.E7, chess.E8, promotion=chess.QUEEN)
board.push(move)

# Oder Benutzer fragen:
if is_promotion_move(from_square, to_square):
    piece = ask_user_promotion()  # GUI-Dialog
    move = chess.Move(from_square, to_square, promotion=piece)
else:
    move = chess.Move(from_square, to_square)
```

**Lösung**:
1. Prüfe ob Zug eine Bauernumwandlung ist (Bauer auf letzter Reihe)
2. Zeige Dialog zur Figurwahl
3. `promotion`-Parameter beim Move setzen

---

### Kategorie 3: KI/Minimax-Algorithmus

#### Fehler 3.1: Endlosrekursion/Stack Overflow

**Symptom**: `RecursionError: maximum recursion depth exceeded`

**Ursache**: Keine Abbruchbedingung oder Tiefenzähler wird nicht dekrementiert.

**Falsch**:
```python
def minimax(board, depth):
    # ❌ Keine Abbruchbedingung!
    for move in board.legal_moves:
        board.push(move)
        score = minimax(board, depth)  # depth bleibt gleich!
        board.pop()
```

**Richtig**:
```python
def minimax(board, depth, maximizing_player):
    # ✅ Abbruchbedingungen
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if maximizing_player:
        max_eval = float('-inf')
        for move in board.legal_moves:
            board.push(move)
            eval = minimax(board, depth - 1, False)  # ✅ depth - 1
            board.pop()
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        # ... analog für minimizing
```

**Lösung**:
1. IMMER Tiefenzähler dekrementieren: `depth - 1`
2. Klare Abbruchbedingungen: `depth == 0` oder `game_over()`
3. Maximale Tiefe begrenzen (z.B. max. 10)

---

#### Fehler 3.2: KI blockiert UI

**Symptom**: Programm friert ein während KI rechnet, keine UI-Updates.

**Ursache**: KI-Berechnung läuft im Hauptthread und blockiert Event-Loop.

**Falsch**:
```python
def on_ai_turn():
    # ❌ Blockiert UI für mehrere Sekunden
    best_move = minimax_search(board, depth=5)
    board.push(best_move)
```

**Richtig**:
```python
import threading

def on_ai_turn():
    # ✅ KI in separatem Thread
    ai_thinking = True

    def compute_move():
        nonlocal ai_thinking
        best_move = minimax_search(board, depth=5)
        # Move in Queue legen, nicht direkt ausführen!
        move_queue.put(best_move)
        ai_thinking = False

    thread = threading.Thread(target=compute_move)
    thread.start()

    # Hauptschleife zeigt "Denkt..."-Animation
    while ai_thinking:
        draw_thinking_indicator()
```

**Alternative (einfacher)**:
```python
# ✅ Tiefe begrenzen für schnelle Antwort
best_move = minimax_search(board, depth=3, max_time=2.0)
```

**Lösung**:
1. Threading für längere KI-Berechnungen
2. Oder Iterative Deepening mit Zeitlimit
3. "Denkt..."-Indikator anzeigen

---

#### Fehler 3.3: Falsche Stellungsbewertung

**Symptom**: KI macht unsinnige Züge, verschenkt Figuren.

**Ursache**: Evaluation-Funktion bewertet Stellung aus falscher Perspektive.

**Falsch**:
```python
def evaluate(board):
    # ❌ Berücksichtigt nicht, wer am Zug ist
    score = 0
    for piece in board.piece_map().values():
        score += piece_values[piece.piece_type]
    return score
```

**Richtig**:
```python
def evaluate(board):
    """
    Bewertet Stellung aus Sicht von Weiß.
    Positiv = gut für Weiß, Negativ = gut für Schwarz.
    """
    score = 0
    for square, piece in board.piece_map().items():
        value = piece_values[piece.piece_type]
        # ✅ Weiße Figuren positiv, schwarze negativ
        if piece.color == chess.WHITE:
            score += value
        else:
            score -= value
    return score

# Im Minimax:
def minimax(board, depth, maximizing_player):
    if depth == 0:
        eval = evaluate(board)
        # ✅ Aus Perspektive des Spielers am Zug
        if board.turn == chess.BLACK:
            eval = -eval
        return eval
```

**Lösung**:
1. Evaluation immer aus einer Perspektive (z.B. Weiß)
2. Im Minimax: Vorzeichen wechseln je nach Spieler
3. Testen mit bekannten Stellungen (z.B. Matt in 1)

---

### Kategorie 4: Datei-I/O und Persistierung

#### Fehler 4.1: PGN-Dateien können nicht gelesen werden

**Symptom**: `ValueError` oder leere Partien beim Laden.

**Ursache**: Fehlerhafte PGN-Syntax oder fehlende Fehlerbehandlung.

**Falsch**:
```python
def load_game(filename):
    # ❌ Keine Fehlerbehandlung
    with open(filename) as f:
        game = chess.pgn.read_game(f)
    return game.board()
```

**Richtig**:
```python
def load_game(filename):
    try:
        with open(filename, encoding='utf-8') as f:
            game = chess.pgn.read_game(f)

            if game is None:
                raise ValueError("Leere oder ungültige PGN-Datei")

            # ✅ Durchlaufe alle Züge um finalen Zustand zu erhalten
            board = game.board()
            for move in game.mainline_moves():
                board.push(move)

            return board

    except FileNotFoundError:
        print(f"Fehler: Datei '{filename}' nicht gefunden.")
        return None
    except Exception as e:
        print(f"Fehler beim Laden: {e}")
        return None
```

**Lösung**:
1. Umfassende Fehlerbehandlung (`try-except`)
2. Encoding explizit angeben (`encoding='utf-8'`)
3. Prüfe ob `read_game()` `None` zurückgibt
4. Alle Züge durchlaufen für finalen Zustand

---

#### Fehler 4.2: Spiel überschreibt sich selbst beim Speichern

**Symptom**: Nur die letzte gespeicherte Partie ist verfügbar.

**Ursache**: Dateien werden überschrieben statt angehängt oder mit eindeutigen Namen gespeichert.

**Falsch**:
```python
def save_game(board):
    # ❌ Überschreibt immer die gleiche Datei
    with open('game.pgn', 'w') as f:
        exporter = chess.pgn.Game()
        f.write(str(exporter))
```

**Richtig**:
```python
from datetime import datetime

def save_game(board, base_name='chess_game'):
    # ✅ Eindeutiger Dateiname mit Timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f'{base_name}_{timestamp}.pgn'

    game = chess.pgn.Game()
    # Metadaten setzen
    game.headers["Event"] = "Casual Game"
    game.headers["Date"] = datetime.now().strftime('%Y.%m.%d')

    # Züge hinzufügen
    node = game
    for move in board.move_stack:
        node = node.add_variation(move)

    with open(filename, 'w', encoding='utf-8') as f:
        print(game, file=f)

    return filename
```

**Lösung**:
1. Eindeutige Dateinamen (Timestamp oder Counter)
2. Oder Benutzer nach Dateiname fragen
3. Metadaten (Datum, Spieler) speichern

---

### Kategorie 5: Architektur und Design

#### Fehler 5.1: Zu viel Code in einer Datei/Funktion

**Symptom**: `main.py` hat 2000+ Zeilen, schwer wartbar.

**Ursache**: Keine Modularisierung, alles in einer Datei.

**Falsch**:
```python
# main.py (2000 Zeilen)
# - Pygame Setup
# - Event Handling
# - Rendering
# - Game Logic
# - AI Engine
# - File I/O
# - ...
```

**Richtig**:
```
src/
├── main.py              (50 Zeilen: Einstiegspunkt)
├── gui/
│   ├── board_renderer.py   (Rendering)
│   └── event_handler.py    (Events)
├── game/
│   └── chess_game.py       (Spiellogik)
├── ai/
│   └── engine.py           (KI)
└── persistence/
    └── pgn_handler.py      (I/O)
```

**Lösung**:
1. Eine Verantwortlichkeit pro Datei
2. Klare Verzeichnisstruktur (siehe PRP)
3. Funktionen < 50 Zeilen
4. Klassen < 300 Zeilen

---

#### Fehler 5.2: Zirkuläre Imports

**Symptom**: `ImportError: cannot import name 'X' from partially initialized module`

**Ursache**: Datei A importiert B, B importiert A.

**Falsch**:
```python
# game/chess_game.py
from gui.board_renderer import render_board

# gui/board_renderer.py
from game.chess_game import ChessGame  # ❌ Zirkular!
```

**Richtig**:
```python
# game/chess_game.py
# ✅ Keine GUI-Imports in Game-Logik

# gui/board_renderer.py
from game.chess_game import ChessGame  # ✅ Nur eine Richtung

# Oder: Type Hints ohne Import
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from game.chess_game import ChessGame
```

**Lösung**:
1. Klare Abhängigkeitsrichtung: `GUI → Game ← AI`
2. Game-Logik kennt keine GUI
3. `TYPE_CHECKING` für Type Hints

---

#### Fehler 5.3: Globale Variablen statt Zustand

**Symptom**: Bugs schwer nachzuvollziehen, Side-Effects überall.

**Ursache**: Globale Variablen statt Klassen mit Zustand.

**Falsch**:
```python
# ❌ Globale Variablen
board = chess.Board()
selected_square = None
player_color = chess.WHITE

def handle_click(pos):
    global selected_square
    # ... modifiziert globalen Zustand
```

**Richtig**:
```python
class ChessGame:
    """Kapselt Spielzustand."""

    def __init__(self):
        self.board = chess.Board()
        self.selected_square = None
        self.player_color = chess.WHITE

    def handle_click(self, pos):
        # ✅ Arbeitet mit self
        if self.selected_square is None:
            self.selected_square = self._pos_to_square(pos)
        # ...
```

**Lösung**:
1. Zustand in Klassen kapseln
2. Funktionen als Methoden
3. Globale Variablen nur für Konstanten

---

### Kategorie 6: Performance

#### Fehler 6.1: Unnötiges Neuzeichnen

**Symptom**: Niedrige FPS, CPU-Last sehr hoch.

**Ursache**: Komplettes Bild wird jeden Frame neu gezeichnet, auch wenn nichts passiert ist.

**Optimierung**:
```python
class GameRenderer:
    def __init__(self):
        self.dirty = True  # Neuzeichnen nötig?

    def render(self, screen, board):
        if not self.dirty:
            return  # ✅ Nichts zu tun

        # Zeichne nur bei Änderungen
        self.draw_board(screen)
        self.draw_pieces(screen, board)
        pygame.display.flip()

        self.dirty = False

    def mark_dirty(self):
        self.dirty = True

# Bei Änderungen:
def on_move_made():
    renderer.mark_dirty()
```

**Lösung**:
1. "Dirty Flag" für Neuzeichnen
2. Nur zeichnen wenn nötig
3. Dirty Rects für partielle Updates

---

#### Fehler 6.2: KI zu langsam

**Symptom**: KI braucht >10 Sekunden pro Zug.

**Ursache**: Keine Alpha-Beta-Pruning oder zu hohe Suchtiefe.

**Optimierungen**:
```python
# 1. Alpha-Beta Pruning implementieren
def minimax(board, depth, alpha, beta, maximizing):
    # ... Standardlogik
    for move in board.legal_moves:
        score = minimax(board, depth-1, alpha, beta, not maximizing)
        if maximizing:
            alpha = max(alpha, score)
        else:
            beta = min(beta, score)

        # ✅ Pruning
        if beta <= alpha:
            break  # Abschneiden

# 2. Move Ordering (bessere Züge zuerst)
def order_moves(board):
    moves = list(board.legal_moves)
    # Schlagzüge zuerst
    captures = [m for m in moves if board.is_capture(m)]
    non_captures = [m for m in moves if not board.is_capture(m)]
    return captures + non_captures

# 3. Transposition Table (Cache)
transposition_table = {}

def minimax_with_cache(board, depth):
    fen = board.fen()
    if fen in transposition_table:
        return transposition_table[fen]

    score = minimax(board, depth)
    transposition_table[fen] = score
    return score
```

**Lösung**:
1. Alpha-Beta Pruning (50-90% schneller)
2. Move Ordering (Captures zuerst)
3. Transposition Table (Cache)
4. Iterative Deepening mit Zeitlimit

---

### Best Practices Zusammenfassung

**DO**:
- ✅ Events in jedem Frame verarbeiten
- ✅ FPS limitieren (60 FPS)
- ✅ Hilfsfunktionen für Koordinaten-Umrechnung
- ✅ Fehlerbehandlung bei Datei-I/O
- ✅ Modularisierung (ein Modul = eine Aufgabe)
- ✅ Zustand in Klassen kapseln
- ✅ Alpha-Beta Pruning für KI
- ✅ Ausführliche Kommentare (warum, nicht was)

**DON'T**:
- ❌ Globale Variablen für Zustand
- ❌ Event-Loop blockieren
- ❌ Koordinaten verwechseln (row/col vs. file/rank)
- ❌ Züge als Strings statt Move-Objekte
- ❌ KI im Hauptthread ohne Zeitlimit
- ❌ Dateien ohne Fehlerbehandlung öffnen
- ❌ Alles in einer Datei
- ❌ Ohne Abbruchbedingung rekursieren

---

## Ressourcen und Referenzen

### Externe Bibliotheken

#### python-chess

- **Offizielle Dokumentation**: https://python-chess.readthedocs.io/
- **GitHub**: https://github.com/niklasf/python-chess
- **PyPI**: https://pypi.org/project/python-chess/
- **Lizenz**: GPL-3.0

**Wichtige Features**:
- Vollständige Schachregeln (Rochade, En Passant, Umwandlung)
- PGN-Parser und -Writer
- FEN-String-Unterstützung
- UCI-Engine-Unterstützung (optional für stärkere KI)

#### Pygame

- **Offizielle Dokumentation**: https://www.pygame.org/docs/
- **Tutorials**: https://www.pygame.org/wiki/tutorials
- **PyPI**: https://pypi.org/project/pygame/
- **Lizenz**: LGPL

**Verwendete Module**:
- `pygame.display` - Fenster-Management
- `pygame.event` - Event-Handling
- `pygame.draw` - Zeichenfunktionen
- `pygame.image` - Bild-Laden
- `pygame.font` - Text-Rendering

### Tutorials und Artikel

1. **"Building a Simple Chess Game in Python" (PyShine)**
   - URL: https://www.pyshine.com/Make-a-simple-chess-game-in-python/
   - Beschreibung: Text-basiertes Schachspiel mit Pygame
   - Relevanz: Grundlegende Struktur

2. **"Create a Chess Game in Python" (GeeksforGeeks)**
   - URL: https://www.geeksforgeeks.org/python/create-a-chess-game-in-python/
   - Beschreibung: Umfassendes Tutorial mit Pygame
   - Relevanz: UI-Design-Ideen

3. **"Introduction to Chess Programming" (stoeckl.ai)**
   - URL: https://www.stoeckl.ai/einfuehrung-in-die-schachprogrammierung/
   - Beschreibung: Deutscher Artikel zu Schach-KI
   - Relevanz: Minimax-Algorithmus

4. **"Minimax Algorithm with Alpha-Beta Pruning"**
   - URL: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
   - Beschreibung: Theoretische Grundlagen
   - Relevanz: KI-Optimierung

### Assets

#### Figurenbilder

Empfohlene Quellen (lizenzfrei):

1. **Wikimedia Commons - Chess Pieces**
   - URL: https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces
   - Lizenz: Public Domain / CC0
   - Format: SVG (konvertierbar zu PNG)

2. **Chess.com Assets**
   - Verschiedene Stil-Varianten
   - Hinweis: Lizenz prüfen!

3. **Unicode-Schachsymbole** (Fallback)
   ```python
   UNICODE_PIECES = {
       'K': '♔', 'Q': '♕', 'R': '♖', 'B': '♗', 'N': '♘', 'P': '♙',
       'k': '♚', 'q': '♛', 'r': '♜', 'b': '♝', 'n': '♞', 'p': '♟'
   }
   ```

#### Sound-Effekte (optional)

- **Freesound.org**: https://freesound.org/
- Suchbegriffe: "chess move", "chess capture", "checkmate"
- Lizenz: CC0 oder CC-BY

### Repository-Patterns

Orientierung an bestehenden Lösungen in `solutions/`:

- **solutions/kursabend-5/projekt_3_quiz.py**
  - Menü-System
  - Datei-I/O
  - Fehlerbehandlung

- **solutions/kursabend-4/aufgabe_3_2_kontaktverwaltung.py**
  - Klassenstruktur
  - CRUD-Operationen
  - Datenpersistierung

### Coding-Standards

Siehe `CLAUDE.md` und `CONTRIBUTING.md`:

- PEP 8 mit max. 100 Zeichen
- Deutsche Kommentare und Docstrings
- Type Hints
- Doctest-Beispiele in Docstrings

---

## Erfolgskriterien

### Funktionale Kriterien

| Kriterium | Beschreibung | Gewichtung |
|-----------|-------------|------------|
| **Spielbarkeit** | Vollständige Schachpartie ohne Crashes | 30% |
| **Regelkonformität** | Alle Schachregeln korrekt (via python-chess) | 20% |
| **KI-Funktionalität** | KI macht sinnvolle Züge auf allen Levels | 15% |
| **Persistierung** | Save/Load funktioniert fehlerfrei | 10% |
| **Undo-Funktion** | Beliebig viele Züge rückgängig machbar | 10% |
| **UI-Usability** | Intuitive Bedienung, keine Fehlklicks | 15% |

**Mindestanforderung**: 80% aller Kriterien erfüllt

### Nicht-Funktionale Kriterien

| Kriterium | Beschreibung | Zielwert |
|-----------|-------------|----------|
| **Performance** | KI-Zugberechnung (Depth 3) | <2 Sekunden |
| **FPS** | Bildwiederholrate | 60 FPS konstant |
| **Speichergröße** | Größe gespeicherter PGN-Dateien | <100 KB pro Partie |
| **Code-Coverage** | Unit-Test-Abdeckung | ≥80% |
| **Linting** | Ruff-Warnungen | 0 Fehler |
| **Type-Check** | mypy-Fehler | 0 Fehler |

### Akzeptanzkriterien

**Das Projekt gilt als erfolgreich, wenn:**

1. ✅ Zwei Personen können eine vollständige Partie spielen
2. ✅ KI schlägt Anfänger auf Schwierigkeitsstufe "Mittel"
3. ✅ Gespeicherte Partien können ohne Datenverlust geladen werden
4. ✅ Alle Schachregeln korrekt implementiert (matt, patt, rochade, etc.)
5. ✅ Code ist gut dokumentiert (README + Inline-Kommentare)
6. ✅ Alle Unit-Tests bestehen
7. ✅ Programm läuft stabil ohne Memory Leaks
8. ✅ UI ist intuitiv bedienbar (keine Einarbeitungszeit)

---

## Risiken und Herausforderungen

### Technische Risiken

#### Risiko 1: Performance-Probleme bei KI

**Wahrscheinlichkeit**: Mittel
**Impact**: Hoch

**Beschreibung**: Minimax-Algorithmus kann bei hoher Suchtiefe (>4) sehr langsam werden.

**Mitigation**:
- Alpha-Beta-Pruning implementieren
- Transposition Tables nutzen
- Iterative Deepening mit Zeitlimit
- KI-Berechnung in separatem Thread

**Fallback**: Suchtiefe auf 3 begrenzen

---

#### Risiko 2: Pygame-Performance bei Animationen

**Wahrscheinlichkeit**: Niedrig
**Impact**: Mittel

**Beschreibung**: Ruckelige Animationen oder FPS-Drops.

**Mitigation**:
- Double Buffering aktivieren
- Nur veränderte Bereiche neu zeichnen (Dirty Rect)
- Sprites verwenden statt Neuzeichnen
- FPS-Limiter (60 FPS)

**Fallback**: Animationen deaktivierbar machen

---

#### Risiko 3: PGN-Parsing-Fehler

**Wahrscheinlichkeit**: Niedrig
**Impact**: Mittel

**Beschreibung**: Fehlerhafte PGN-Dateien können Programm zum Absturz bringen.

**Mitigation**:
- Strikte Validierung beim Laden
- Try-Except-Blöcke um I/O
- Fehlermeldungen für Benutzer
- python-chess PGN-Parser nutzen (robust)

**Fallback**: Fehlende Züge überspringen, nicht crashen

---

### Pädagogische Herausforderungen

#### Herausforderung 1: Komplexität für Anfänger

**Problem**: Großes Projekt mit vielen Komponenten könnte Anfänger überfordern.

**Lösung**:
- Modulare Struktur mit klaren Verantwortlichkeiten
- Schrittweise Entwicklung (Phase 1-5)
- Ausführliche Dokumentation
- Code-Kommentare auf Deutsch

---

#### Herausforderung 2: Debugging von GUI-Code

**Problem**: Pygame-Fehler sind schwer zu debuggen (keine Stack Traces für Zeichenfehler).

**Lösung**:
- Logging einbauen
- Assertions für Vorbedingungen
- Separates Testing der Rendering-Logik
- Visual Debugging (Debug-Overlays)

---

### Zeitliche Risiken

#### Risiko: Unterschätzter Aufwand

**Wahrscheinlichkeit**: Hoch
**Impact**: Hoch

**Beschreibung**: Projekt könnte länger dauern als 52 Stunden.

**Mitigation**:
- Puffer einplanen (20% Reserve)
- Iterative Entwicklung (funktionierende Zwischenstände)
- Nice-to-Have Features optional lassen

**Fallback**: MVP zuerst fertigstellen, dann erweitern

---

## Nächste Schritte

### Sofort

1. **Repository-Setup**
   ```bash
   mkdir schach
   cd schach
   uv init
   uv add python-chess pygame
   ```

2. **Projektstruktur anlegen**
   ```bash
   mkdir -p src/{gui,game,ai,persistence,utils}
   mkdir -p tests assets/{images,sounds} saves docs
   touch src/main.py
   ```

3. **Erste Commits**
   ```bash
   git init
   git add .
   git commit -m "feat: Initiales Projekt-Setup für Schachprogramm"
   ```

### Diese Woche

- [ ] Phase 1 starten: Grundgerüst
- [ ] Leeres Schachbrett zeichnen
- [ ] Event-Loop implementieren

### Nächste Woche

- [ ] Phase 2: Spielmechanik
- [ ] Figuren zeichnen
- [ ] Drag-and-Drop

### Support

Bei Fragen oder Problemen:
- Issues auf GitHub erstellen
- Code-Reviews anfordern
- Dokumentation aktualisieren

---

## Anhang

### Referenzen

- [python-chess Docs](https://python-chess.readthedocs.io/)
- [Pygame Docs](https://www.pygame.org/docs/)
- [PGN-Spezifikation](http://www.saremba.de/chessgml/standards/pgn/pgn-complete.htm)
- [Minimax-Tutorial](https://en.wikipedia.org/wiki/Minimax)

---

**Ende des Product Requirement Prompt**
