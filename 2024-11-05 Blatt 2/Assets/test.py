n = 2
x1 = 0.2
genauigkeit = 0.00001  # die fünf Nachkommastellen

while True:
    h = n / x1  # Berechnung von h
    if h == x1:
        print(f"x (näherungsweise Wurzel) gefunden: {x1}")
        break

    x_neu = (x1 + h) / 2  # neuer Näherungswert
    if abs(x_neu - x1) < genauigkeit:
        print(f"x (näherungsweise Wurzel) gefunden: {round(x_neu, 5)}")
        break

    x1 = x_neu  # Aktualisierung von x1 für die nächste Iteration
