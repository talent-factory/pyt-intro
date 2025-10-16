# mathutils.py
# Hilfsfunktionen für mathematische Berechnungen

def fakultaet(n):
    """
    Berechnet die Fakultät einer Zahl n (n!).
    
    Args:
        n (int): Eine nicht-negative Ganzzahl
        
    Returns:
        int: Die Fakultät von n
        
    Examples:
        >>> fakultaet(0)
        1
        >>> fakultaet(1)
        1
        >>> fakultaet(5)
        120
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
        
    Examples:
        >>> fibonacci(1)
        0
        >>> fibonacci(2)
        1
        >>> fibonacci(7)
        8
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
        
    Examples:
        >>> ist_primzahl(1)
        False
        >>> ist_primzahl(2)
        True
        >>> ist_primzahl(11)
        True
        >>> ist_primzahl(15)
        False
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


def ggt(a, b):
    """
    Berechnet den grössten gemeinsamen Teiler zweier Zahlen.
    
    Args:
        a (int): Erste Zahl
        b (int): Zweite Zahl
        
    Returns:
        int: Der größte gemeinsame Teiler
        
    Examples:
        >>> ggt(8, 12)
        4
        >>> ggt(17, 23)
        1
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


def kgv(a, b):
    """
    Berechnet das kleinste gemeinsame Vielfache zweier Zahlen.
    
    Args:
        a (int): Erste Zahl
        b (int): Zweite Zahl
        
    Returns:
        int: Das kleinste gemeinsame Vielfache
        
    Examples:
        >>> kgv(4, 6)
        12
        >>> kgv(3, 5)
        15
    """
    return abs(a * b) // ggt(a, b) if a and b else 0


# Beispielaufruf innerhalb des Moduls selbst bei direkter Ausführung
if __name__ == "__main__":
    import doctest

    doctest.testmod()

    print("Einige Beispiele:")
    print(f"5! = {fakultaet(5)}")
    print(f"10. Fibonacci-Zahl: {fibonacci(10)}")
    print(f"Ist 7 eine Primzahl? {ist_primzahl(7)}")
    print(f"Ist 12 eine Primzahl? {ist_primzahl(12)}")
    print(f"GGT von 48 und 18: {ggt(48, 18)}")
    print(f"KGV von 6 und 8: {kgv(6, 8)}")
