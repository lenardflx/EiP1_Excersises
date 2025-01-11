import numpy as np
from datetime import datetime
str2date = lambda x: datetime.strptime(x, '%Y-%m-%d')
data = np.genfromtxt("ethereum.csv", delimiter=',', dtype=None, converters = {0: str2date}, encoding='utf-8')
dates = [d[0] for d in data]
prices = [d[5] for d in data]

def is_double_top(arr_part):
    tolerance = 0.01
    d1, d2, d3, d4 = arr_part
    return (d2 > d1 and
            d3 < d2 and
            abs(d4-d2) <= tolerance)

def check_prediction(arr_part):
    return arr_part[4] < arr_part[3]

def analyze_double_top_patterns(dates, prices):
    predictions = []
    for i in range(len(prices)-4):
        if is_double_top(prices[i:i+4]):
            print(f"Double top pattern found: {dates[i].strftime('%d.%m.%Y')}")
            prediction = check_prediction(prices[i:i+5])
            predictions.append(prediction)
    if predictions:
        print(f"\nAccuracy: {np.mean(predictions):.2%} ({sum(predictions)}/{len(predictions)})")
    else:
        print("No double top patterns found.")

analyze_double_top_patterns(dates, prices)

# Aufgabe 5
# Das Ergebnis ist vom Toleranzwert abhängig, der je nach Markt angepasst werden müsste.
# Schon kleine Änderungen des Wertes führen einer komplett anderen Anzahl an gefundenen Mustern.
# Außerdem werden wichtige Faktoren wie Markttrends von der reinen Berechnung nicht berücksichtigt.
# Die Trefferquote ist in unserem Fall sehr schlecht, wodurch den Ergebnissen nicht zu vertrauen ist.
# Jedoch kann ein solcher Algorithmus zur Unterstützung von eigener Analyse verwendet werden.