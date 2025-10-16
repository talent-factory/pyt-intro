def hello(name="everybody"):
    """Gibt eine personalisierte Begrüßungsnachricht aus.

    Diese Funktion erstellt und gibt eine Begrüßungsnachricht aus, die an eine
    bestimmte Person oder Gruppe gerichtet sein kann. Wenn kein Name angegeben wird,
    wird standardmäßig "everybody" verwendet.

    Args:
        name (str, optional): Der Name der zu begrüßenden Person oder Gruppe.
            Standardwert ist "everybody".

    Returns:
        None: Die Funktion gibt nur Text auf der Konsole aus, hat aber keinen
        Rückgabewert.

    Beispiele:
        Die Funktion kann auf verschiedene Weisen verwendet werden. Hier sind einige
        typische Anwendungsfälle:

        >>> hello()  # Standardaufruf ohne Parameter
        Hello everybody!

        >>> hello("Alice")  # Begrüßung einer bestimmten Person
        Hello Alice!

        >>> hello("Python Community")  # Begrüßung einer Gruppe
        Hello Python Community!

        Die Funktion akzeptiert auch leere Strings:
        >>> hello("")  # Begrüßung mit leerem String
        Hello !

        Sowie Unicode-Zeichen für internationale Namen:
        >>> hello("José")  # Begrüßung mit Unicode-Zeichen
        Hello José!

    Hinweise:
        - Die Funktion verwendet f-Strings für die Formatierung
        - Es findet keine Validierung des Eingabeparameters statt
        - Die Ausgabe erfolgt immer mit einem Ausrufezeichen
    """
    print(f"Hello {name}!")


if __name__ == "__main__":
    import doctest

    hello("Daniel")
    doctest.testmod(verbose=False)
