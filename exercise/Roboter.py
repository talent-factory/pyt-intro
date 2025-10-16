#  Released under MIT License
#
#  Copyright (c) 2024. Talent Factory GmbH
#
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the "Software"), to deal
#  in the Software without restriction, including without limitation the rights to
#  use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#  of the Software, and to permit persons to whom the Software is furnished to
#  do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#  EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
#  OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
#  NON INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
#  HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
#  WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
#  OR OTHER DEALINGS IN THE SOFTWARE.


from enum import Enum


class Orientation(Enum):
    NORTH = "N"
    EAST = "E"
    SOUTH = "S"
    WEST = "W"


class Roboter:
    """
    Implementiert einen Roboter.

    Beispiel:
    >>> roboter = Roboter()
    >>> roboter.name = "Marvin"
    >>> print(roboter)
    Roboter: Marvin, Baujahr: 0
    >>> roboter = Roboter("Peter")
    >>> print(roboter)
    Roboter: Peter, Baujahr: 0
    >>> roboter = Roboter("Marvin", 1975)
    >>> print(roboter)
    Roboter: Marvin, Baujahr: 1975

    Test der Orientierung und Bewegung:
    >>> roboter = Roboter("TestBot")
    >>> roboter.position
    [0, 0]
    >>> roboter.orientation
    <Orientation.NORTH: 'N'>
    >>> roboter.set_orientation(Orientation.NORTH)
    >>> roboter.move(5)
    >>> roboter.position
    [0, 5]
    >>> roboter.set_orientation(Orientation.EAST)
    >>> roboter.move(3)
    >>> roboter.position
    [3, 5]
    >>> roboter.set_orientation(Orientation.SOUTH)
    >>> roboter.move(2)
    >>> roboter.position
    [3, 3]
    >>> roboter.set_orientation(Orientation.WEST)
    >>> roboter.move(1)
    >>> roboter.position
    [2, 3]

    Test der Fehlerbehandlung:
    >>> try:
    ...     roboter.set_orientation("INVALID")
    ... except ValueError as e:
    ...     print(str(e))
    Orientation muss vom Typ Orientation sein

    Test der Position:
    >>> roboter = Roboter("TestBot")
    >>> roboter.position = [10, 20]
    >>> roboter.position
    [10, 20]
    
    Test der Positionsvalidierung:
    >>> try:
    ...     roboter.position = (1, 2)  # Tupel statt Liste
    ... except ValueError as e:
    ...     print(str(e))
    Position muss eine Liste mit genau zwei Zahlen sein
    >>> try:
    ...     roboter.position = [1, 2, 3]  # Zu viele Werte
    ... except ValueError as e:
    ...     print(str(e))
    Position muss eine Liste mit genau zwei Zahlen sein
    >>> try:
    ...     roboter.position = ["1", "2"]  # Keine Zahlen
    ... except ValueError as e:
    ...     print(str(e))
    Position muss eine Liste mit genau zwei Zahlen sein
    """

    def __init__(self, name: str = "", baujahr: int = 0):
        """
        Repräsentiert eine Instanz einer Klasse mit einem optionalen Name- und Baujahr-Attribut. Die Klasse ist
        für die Initialisierung mit Namen- und Baujahr-Parameter und Standardverhalten konzipiert. Dies ermöglicht
        die Erstellung von Objekten mit spezifischen Attributen und Standard-Initialisierung.

        Parameter:
            name (str, optional): Der Name für die Instanz. Standardwert ist ein leerer String.
            baujahr (int, optional): Das Baujahr des Roboters. Standardwert ist 0.
        """
        self.name = name[:10]
        self.__baujahr = baujahr
        self.__position = [0, 0]
        self.__orientation = Orientation.NORTH

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, position):
        """
        Setzt die Position des Roboters.

        Parameter:
            position (list): Eine Liste mit genau zwei Zahlen [x, y]
        
        Raises:
            ValueError: Wenn die Position keine Liste mit genau zwei Zahlen ist
        """
        if not isinstance(position, list) or len(position) != 2 or \
           not all(isinstance(x, (int, float)) for x in position):
            raise ValueError("Position muss eine Liste mit genau zwei Zahlen sein")
        self.__position = position

    @property
    def orientation(self):
        """Gibt die aktuelle Ausrichtung des Roboters zurück."""
        return self.__orientation

    def set_orientation(self, orientation: Orientation):
        """
        Setzt die Ausrichtung des Roboters.

        Parameter:
            orientation (Orientation): Die neue Ausrichtung des Roboters (NORTH, EAST, SOUTH, WEST)
        """
        if not isinstance(orientation, Orientation):
            raise ValueError("Orientation muss vom Typ Orientation sein")
        self.__orientation = orientation

    def move(self, steps: int):
        """
        Bewegt den Roboter in die aktuelle Richtung.

        Parameter:
            steps (int): Die Anzahl der Schritte, die der Roboter in die aktuelle Richtung gehen soll.
        """
        if self.__orientation == Orientation.NORTH:
            self.__position[1] += steps
        elif self.__orientation == Orientation.EAST:
            self.__position[0] += steps
        elif self.__orientation == Orientation.SOUTH:
            self.__position[1] -= steps
        elif self.__orientation == Orientation.WEST:
            self.__position[0] -= steps

    def __str__(self):
        """Gibt eine String-Repräsentation des Roboters zurück."""
        return f"Roboter: {self.name}, Baujahr: {self.__baujahr}"


if __name__ == "__main__":
    import doctest

    doctest.testmod()
