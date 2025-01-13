import numpy as np
from datetime import datetime
str2date = lambda x: datetime.strptime(x, '%Y-%m-%d')
data = np.genfromtxt("ethereum.csv", delimiter=',', dtype=None, converters = {0: str2date}, encoding='utf-8')
dates = [d[0] for d in data]
prices = [d[5] for d in data]

def is_double_top(arr_part):
    tolerance = 0.01
    return (arr_part[0] < arr_part[1] and
            arr_part[2] < arr_part[1] and
            abs(arr_part[3]-arr_part[1]) < tolerance)

def check_prediction(arr_part):
    return arr_part[3] > arr_part[4]

predictions = []
for i in range(len(prices)-4):
    if is_double_top(prices[i:i+4]):
        print(f"Double top pattern found: {dates[i].strftime('%d.%m.%Y')}")
        predictions.append(check_prediction(prices[i:i+5]))
print("\nAccuracy:", f"{np.mean(predictions):.2%} ({sum(predictions)}/{len(predictions)})"
      if predictions else "No double top patterns.")

# Aufgabe 5
# Das Ergebnis ist vom Toleranzwert abhängig, der je nach Markt angepasst werden müsste.
# Schon kleine Änderungen des Wertes führen einer komplett anderen Anzahl an gefundenen Mustern.
# Außerdem werden wichtige Faktoren wie Markttrends von der reinen Berechnung nicht berücksichtigt.
# Die Trefferquote ist in unserem Fall sehr schlecht, wodurch den Ergebnissen nicht zu vertrauen ist.
# Jedoch kann so ein Algorithmus zur Hilfe verwendet werden.