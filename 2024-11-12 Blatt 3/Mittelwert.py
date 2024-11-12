# Daten
test_list = [7,20,5,-1,3,11,32,17,42]
n = len(test_list)

# Mittelwert berechnen
temp = 0
for x in test_list:
    temp += x
average = 1/n * temp

# Varianz berechnen
temp = 0
for x in test_list:
    temp += (x - average)**2
variance = 1 / n * temp

# Ausgabe
print("Mittelwert:", average)
print("Varianz:", variance)