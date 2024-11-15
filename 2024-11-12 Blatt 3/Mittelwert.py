# Daten
values = [7, 20, 5, -1, 3, 11, 32, 17, 42]
n = len(values)

# Mittelwert berechnen
temp = 0
for x in values:
    temp += x
average = 1 / n * temp

# Varianz berechnen
temp = 0
for x in values:
    temp += (x - average) ** 2
variance = 1 / n * temp

# Zusatz: Standardabweichung
std_dev = variance ** 0.5

# Ausgabe
print("Mittelwert:", average)
print("Varianz:", variance)
print("Standardabweichung:", std_dev)
