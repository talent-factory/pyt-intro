#  Released under MIT License
#
#  Copyright (©) 2024. Talent Factory GmbH
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


class ShoppingCart:
    """
    Eine Klasse zur Verwaltung eines Einkaufswagens.

    Examples:
        >>> cart = ShoppingCart()
        >>> cart.add_item("Apfel", 0.5, 3)
        >>> cart.add_item("Banane", 0.3, 2)
        >>> cart.get_total()
        2.1
        >>> cart.get_item_count()
        5
        >>> cart.remove_item("Apfel", 1)
        >>> cart.get_total()
        1.6
    """

    def __init__(self):
        """Initialisiert einen leeren Einkaufswagen."""
        self.items = {}  # Format: {name: {'price': price, 'quantity': quantity}}

    def add_item(self, name, price, quantity=1):
        """Fügt einen Artikel zum Einkaufswagen hinzu oder aktualisiert die Menge."""
        if name in self.items:
            self.items[name]["quantity"] += quantity
        else:
            self.items[name] = {"price": price, "quantity": quantity}

    def remove_item(self, name, quantity=1):
        """Entfernt eine bestimmte Menge eines Artikels."""
        if name in self.items:
            self.items[name]["quantity"] -= quantity
            if self.items[name]["quantity"] <= 0:
                del self.items[name]

    def get_total(self):
        """Berechnet die Gesamtsumme."""
        return sum(item["price"] * item["quantity"] for item in self.items.values())

    def get_item_count(self):
        """Gibt die Gesamtanzahl der Artikel zurück."""
        return sum(item["quantity"] for item in self.items.values())

    def clear(self):
        """Leert den Einkaufswagen."""
        self.items.clear()


if __name__ == "__main__":
    import doctest

    doctest.testmod()
