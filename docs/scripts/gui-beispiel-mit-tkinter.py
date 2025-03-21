#  Released under MIT License
#
#  Copyright (©) 2025. Talent Factory GmbH
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

import tkinter as tk

# Ein Fenster erstellen
fenster = tk.Tk()
fenster.title("Mein erstes GUI-Programm")

# Fenstergröße festlegen (Breite x Höhe)
fenster.geometry("400x300")  # 400 Pixel breit, 300 Pixel hoch

# Optional: Verhindern, dass das Fenster in der Größe verändert werden kann
fenster.resizable(False, False)  # (width, height) auf False setzen

# Eine Beschriftung hinzufügen
beschriftung = tk.Label(fenster, text="Hallo Welt!")
beschriftung.pack(pady=20)  # Abstand nach oben und unten

# Ein Eingabefeld hinzufügen
eingabe = tk.Entry(fenster, width=30)
eingabe.pack(pady=10)


# Eine Funktion für den Button
def button_klick():
    text = eingabe.get()
    beschriftung.config(text=f"Du hast eingegeben: {text}")


# Einen Button hinzufügen
button = tk.Button(fenster, text="Klick mich!", command=button_klick)
button.pack(pady=10)

# Das Programm starten
fenster.mainloop()
