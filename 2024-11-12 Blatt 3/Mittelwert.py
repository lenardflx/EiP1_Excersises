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

# Da namentlich genannt auch Standardabweichung:
standard_deviation = variance ** 0.5 # Mal 0.5 => sqrt

# Ausgabe
print("Mittelwert:", average)
print("Varianz:", variance)
print("Standardabweichung:", standard_deviation)
