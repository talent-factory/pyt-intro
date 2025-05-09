# Lösungen zu den Übungsaufgaben des Python-Grundlagen-Tutorials

# Lösung: String-Manipulation
def satz_umkehren(satz):
    """Kehrt die Reihenfolge der Wörter in einem Satz um."""
    woerter = satz.split()
    woerter.reverse()
    return " ".join(woerter)


# Lösung: Zinsberechnung
def zinseszins_berechnen(anfangsbetrag, zinssatz, perioden_pro_jahr, jahre):
    """
    Berechnet den Endbetrag einer Investition mit Zinseszins.
    
    Args:
        anfangsbetrag (float): Der Anfangsbetrag der Investition
        zinssatz (float): Der jährliche Zinssatz als Dezimalzahl (z.B. 0.05 für 5%)
        perioden_pro_jahr (int): Anzahl der Zinsperioden pro Jahr
        jahre (int): Anzahl der Jahre
        
    Returns:
        float: Der Endbetrag nach der angegebenen Zeit
    """
    endbetrag = anfangsbetrag * (1 + zinssatz / perioden_pro_jahr) ** (perioden_pro_jahr * jahre)
    return round(endbetrag, 2)


# Lösung: Listenverarbeitung
def eindeutige_elemente(liste):
    """
    Filtert Duplikate aus einer Liste und gibt eindeutige Elemente in aufsteigender Reihenfolge zurück.
    
    Args:
        liste (list): Die Eingabeliste mit möglichen Duplikaten
        
    Returns:
        list: Eine sortierte Liste mit eindeutigen Elementen
    """
    eindeutig = list(set(liste))
    eindeutig.sort()
    return eindeutig


# Lösung: FizzBuzz
def fizzbuzz(n):
    """
    Implementiert das klassische FizzBuzz-Problem.
    
    Args:
        n (int): Die obere Grenze (inklusive)
    """
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=", ")
        elif i % 3 == 0:
            print("Fizz", end=", ")
        elif i % 5 == 0:
            print("Buzz", end=", ")
        else:
            print(i, end=", ")
    print()  # Neue Zeile am Ende


# Lösung: Passwort-Validator
def passwort_pruefen(passwort):
    """
    Prüft, ob ein Passwort den Sicherheitsanforderungen entspricht.
    
    Args:
        passwort (str): Das zu prüfende Passwort
        
    Returns:
        bool: True, wenn das Passwort stark ist, sonst False
    """
    # Prüfen der Mindestlänge
    if len(passwort) < 8:
        return False

    # Flags für die Anforderungen
    hat_grossbuchstaben = False
    hat_kleinbuchstaben = False
    hat_zahl = False
    hat_sonderzeichen = False

    # Prüfen jedes Zeichens
    for zeichen in passwort:
        if zeichen.isupper():
            hat_grossbuchstaben = True
        elif zeichen.islower():
            hat_kleinbuchstaben = True
        elif zeichen.isdigit():
            hat_zahl = True
        elif not zeichen.isalnum():  # Nicht alphanumerisch = Sonderzeichen
            hat_sonderzeichen = True

    # Alle Anforderungen müssen erfüllt sein
    return (hat_grossbuchstaben and hat_kleinbuchstaben and
            hat_zahl and hat_sonderzeichen)


# Lösung: Mathutils-Modul
def fakultaet(n):
    """
    Berechnet die Fakultät einer Zahl n (n!).
    
    Args:
        n (int): Eine nicht-negative Ganzzahl
        
    Returns:
        int: Die Fakultät von n
    """
    if n < 0:
        raise ValueError("Fakultät ist nur für nicht-negative Zahlen definiert")
    if n == 0 or n == 1:
        return 1

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def fibonacci(n):
    """
    Gibt die n-te Fibonacci-Zahl zurück.
    
    Args:
        n (int): Eine positive Ganzzahl
        
    Returns:
        int: Die n-te Fibonacci-Zahl
    """
    if n <= 0:
        raise ValueError("Fibonacci ist nur für positive Ganzzahlen definiert")
    if n == 1:
        return 0
    if n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def ist_primzahl(n):
    """
    Prüft, ob eine Zahl eine Primzahl ist.
    
    Args:
        n (int): Eine zu prüfende ganze Zahl
        
    Returns:
        bool: True, wenn n eine Primzahl ist, sonst False
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


# Lösung: Dateianalyse
from collections import Counter


def datei_analysieren(dateipfad):
    """
    Analysiert eine Textdatei und gibt Statistiken zurück.
    
    Args:
        dateipfad (str): Pfad zur zu analysierenden Datei
        
    Returns:
        dict: Statistiken der Datei
    """
    try:
        with open(dateipfad, 'r', encoding='utf-8') as datei:
            # Datei einlesen
            inhalt = datei.read()
            zeilen = inhalt.split('\n')

            # Zeichen zählen (inkl. Leerzeichen)
            zeichen_anzahl = len(inhalt)

            # Wörter zählen
            woerter = inhalt.lower().split()
            woerter_anzahl = len(woerter)

            # Häufigste Wörter finden
            woerter_zaehler = Counter(woerter)
            top_woerter = woerter_zaehler.most_common(5)

            return {
                'zeilen': len(zeilen),
                'woerter': woerter_anzahl,
                'zeichen': zeichen_anzahl,
                'top_woerter': top_woerter
            }

    except FileNotFoundError:
        print(f"Fehler: Die Datei '{dateipfad}' wurde nicht gefunden.")
        return {
            'zeilen': 0,
            'woerter': 0,
            'zeichen': 0,
            'top_woerter': []
        }
    except Exception as e:
        print(f"Ein Fehler ist aufgetreten: {e}")
        return {
            'zeilen': 0,
            'woerter': 0,
            'zeichen': 0,
            'top_woerter': []
        }


# Beispiel für Taschenrechner
def taschenrechner():
    """Ein einfacher Taschenrechner mit Grundrechenarten."""
    print("Einfacher Taschenrechner")
    print("Operationen: +, -, *, /, ** (Potenz)")
    print("Eingabe 'q' zum Beenden")

    while True:
        try:
            # Benutzereingabe
            ausdruck = input("\nGeben Sie eine Berechnung ein (z.B. 2 + 3): ")

            # Beenden bei 'q'
            if ausdruck.lower() == 'q':
                print("Taschenrechner wird beendet.")
                break

            # Auswertung des Ausdrucks
            ergebnis = eval(ausdruck)  # Vorsicht: eval() kann in der Praxis unsicher sein
            print(f"Ergebnis: {ergebnis}")

        except Exception as e:
            print(f"Fehler: {e}")


# Wenn das Skript direkt ausgeführt wird, führe einige Testfälle aus
if __name__ == "__main__":
    print("Testfälle für die Lösungen:")

    print("\nTest: satz_umkehren")
    test_satz = "Python ist eine großartige Sprache"
    print(f"Original: {test_satz}")
    print(f"Umgekehrt: {satz_umkehren(test_satz)}")

    print("\nTest: zinseszins_berechnen")
    print(f"1000€ bei 5% Zinsen über 10 Jahre: {zinseszins_berechnen(1000, 0.05, 4, 10)}€")

    print("\nTest: eindeutige_elemente")
    test_liste = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    print(f"Original: {test_liste}")
    print(f"Eindeutig: {eindeutige_elemente(test_liste)}")

    print("\nTest: fizzbuzz bis 20")
    fizzbuzz(20)

    print("\nTest: passwort_pruefen")
    test_passwoerter = [
        "abc123",
        "ABCDEFGH",
        "abcdefgh",
        "abcABC123",
        "Abcd1234!",
        "P@ssw0rt"
    ]
    for pw in test_passwoerter:
        if passwort_pruefen(pw):
            print(f"{pw}: Starkes Passwort")
        else:
            print(f"{pw}: Schwaches Passwort")

    print("\nTest: fakultaet")
    for i in range(6):
        print(f"{i}! = {fakultaet(i)}")

    print("\nTest: fibonacci")
    for i in range(1, 11):
        print(f"Fibonacci({i}) = {fibonacci(i)}")

    print("\nTest: ist_primzahl")
    for i in range(1, 21):
        print(f"{i} ist Primzahl: {ist_primzahl(i)}")

    print("\nFür den Taschenrechner oder die Dateianalyse müssten interaktive Eingaben erfolgen.")
    print("Diese Tests werden hier nicht automatisch ausgeführt.")
