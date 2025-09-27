# Einfacher Python-Rechner
# Dieser Code führt Grundoperationen aus: Addition, Subtraktion, Multiplikation, Division

def add(a, b):
    # Addition von zwei Zahlen
    return a + b

def subtract(a, b):
    # Subtraktion von zwei Zahlen
    return a - b

def multiply(a, b):
    # Multiplikation von zwei Zahlen
    return a * b

def divide(a, b):
    # Division von zwei Zahlen mit Fehlerbehandlung
    if b == 0:
        return "Fehler: Division durch Null!"
    return a / b

print("Willkommen zum Python-Rechner! 😃")
print("Wähle eine Operation:")
print("1. Addition")
print("2. Subtraktion")
print("3. Multiplikation")
print("4. Division")

wahl = input("Gib die Nummer der Operation ein (1/2/3/4): ")

zahl1 = float(input("Gib die erste Zahl ein: "))
zahl2 = float(input("Gib die zweite Zahl ein: "))

if wahl == "1":
    print("Ergebnis:", add(zahl1, zahl2))
elif wahl == "2":
    print("Ergebnis:", subtract(zahl1, zahl2))
elif wahl == "3":
    print("Ergebnis:", multiply(zahl1, zahl2))
elif wahl == "4":
    print("Ergebnis:", divide(zahl1, zahl2))
else:
    print("Ungültige Eingabe!")
