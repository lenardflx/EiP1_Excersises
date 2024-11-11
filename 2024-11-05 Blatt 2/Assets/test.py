n = 2
x1 = 0.2
genauigkeit = 0.00001  # die fünf Nachkommastellen

while abs(n / x1 - x1) >= genauigkeit:
    x1 = (x1 + n / x1) / 2

print(f"x (näherungsweise Wurzel) gefunden: {round(x1, 5)}")
