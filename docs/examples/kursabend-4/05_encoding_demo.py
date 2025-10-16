"""
Beispiel 5: Warum encoding='utf-8' wichtig ist
Demonstriert die Bedeutung der richtigen Zeichenkodierung.
"""

# Text mit Umlauten und Sonderzeichen
text_mit_umlauten = """
Grüezi! 🇨🇭
Dies ist ein Text mit deutschen Umlauten: ä, ö, ü, Ä, Ö, Ü, ß
Und Sonderzeichen: € £ ¥ © ® ™
Französisch: à, é, è, ê, ç
"""

print("=== Schreiben mit UTF-8 Encoding ===")
# Richtig: Mit UTF-8 Encoding
with open('text_utf8.txt', 'w', encoding='utf-8') as datei:
    datei.write(text_mit_umlauten)

print("✓ Datei mit UTF-8 geschrieben: text_utf8.txt")

# Lesen mit UTF-8
print("\n=== Lesen mit UTF-8 Encoding ===")
with open('text_utf8.txt', 'r', encoding='utf-8') as datei:
    inhalt = datei.read()
    print(inhalt)

print("\n" + "=" * 60)
print("WICHTIG:")
print("=" * 60)
print("Verwende IMMER encoding='utf-8' beim Öffnen von Dateien!")
print("Sonst können Umlaute und Sonderzeichen falsch dargestellt werden.")
print("=" * 60)
