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

# Zuerst müssen wir Streamlit importieren
import streamlit as st

# 1. Titel und Überschriften
# -------------------------
# Haupttitel der App
st.title("Meine erste Streamlit App")

# Verschiedene Überschriften
st.header("Das ist eine grosse Überschrift")
st.subheader("Das ist eine kleinere Überschrift")

# 2. Textelemente
# --------------
# Normaler Text
st.text("Das ist ein einfacher Text ohne Formatierung")

# Formatierter Text (unterstützt Markdown)
st.markdown("Das ist **fetter Text** und *kursiver Text*")

# Eine Fehlermeldung
st.error("Dies ist eine Fehlermeldung!")

# 3. Eingabeelemente
# -----------------
# Texteingabefeld
name = st.text_input("Wie heisst du?", "Max Mustermann")


# 3. Eingabeelemente
# -----------------
# Texteingabefeld
name = st.text_input("Wie heißt du?", "Max Mustermann")

# Mehrzeiliges Textfeld
beschreibung = st.text_area("Beschreibe dich:", "Ich bin ein Student...")

# Zahlen-Eingabe
alter = st.number_input("Wie alt bist du?", min_value=0, max_value=120, value=20)

# Schieberegler
gewicht = st.slider("Wähle ein Gewicht (kg)", 0, 200, 70)

# 4. Auswahlmöglichkeiten
# ----------------------
# Checkbox
if st.checkbox("Zeige mehr Details"):
    st.write("Hier sind mehr Details!")

# Radio-Buttons
programmiererfahrung = st.radio(
    "Welche Programmiererfahrung hast du?", ["Keine", "Etwas", "Viel"]
)

# Dropdown-Menü
lieblingssprache = st.selectbox(
    "Was ist deine Lieblingsprogrammiersprache?",
    ["Python", "Java", "JavaScript", "C++"],
)

# Mehrfachauswahl
hobbies = st.multiselect(
    "Wähle deine Hobbies:", ["Programmieren", "Lesen", "Sport", "Musik", "Gaming"]
)

# 5. Buttons
# ---------
if st.button("Klick mich!"):
    st.write("Button wurde geklickt!")

# 6. Fortschrittsanzeige
# ---------------------
import time

fortschritt = st.progress(0)
for i in range(100):
    # Simuliere eine Berechnung
    time.sleep(0.01)
    fortschritt.progress(i + 1)

# 7. Daten anzeigen
# ----------------
# Als Tabelle
daten = {
    "Name": ["Anna", "Ben", "Clara"],
    "Alter": [20, 25, 22],
    "Stadt": ["Berlin", "Hamburg", "München"],
}
st.table(daten)

# Als DataFrame
import pandas as pd

df = pd.DataFrame(daten)
st.dataframe(df)

# 8. Sidebar
# ---------
# Elemente können auch in der Seitenleiste platziert werden
with st.sidebar:
    st.header("Seitenleiste")
    name_sidebar = st.text_input("Name in der Seitenleiste")
    alter_sidebar = st.slider("Alter in der Seitenleiste", 0, 100, 25)
