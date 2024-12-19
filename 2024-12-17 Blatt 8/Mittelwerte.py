import numpy as np
from matplotlib import pyplot as plt

# Daten einlesen
data = np.loadtxt("Klimadaten FRA.txt", delimiter=";")
x_axis = np.arange(data.shape[0])
tx = data[:, 6]

# Aufgabe 1
def single_mean():
    mean = float(np.mean(tx))
    plt.hlines(mean, x_axis[0], x_axis[-1], color='orange', label='Mittelwert', linestyle='-')

# Aufgabe 2 und 3
def mean_sections(m):
    n_sections = m + 1
    intervals = np.array_split(tx, n_sections)
    means = [np.mean(interval) for interval in intervals]
    x_means = [interval[len(interval) // 2] for interval in np.array_split(x_axis, n_sections)]

    plt.plot(x_means, means, color='orange', label=f'{m} Mittelwerte', linestyle='-')

# Aufgabe 4
def moving_average(n_partners=1, skip_neighbors=False):
    moving_avgs = []
    x_moving = []

    for i in range(n_partners, len(tx) - n_partners, (n_partners * 2 + 1) if skip_neighbors else n_partners):
        avg = np.mean(tx[i - n_partners:i + n_partners])
        moving_avgs.append(avg)
        x_moving.append(x_axis[i])

    plt.plot(x_moving, moving_avgs, color='orange', label='Laufender Mittelwert', linestyle='-')

# Main
if __name__ == "__main__":
    print("Aufgabe wählen:")
    print("1: Einzelner Mittelwert")
    print("2: 3 Mittelwerte")
    print("3: m Mittelwerte")
    print("4: Laufender Mittelwert")
    choice = input("(1-4): ")

    plt.figure(figsize=(10, 5))
    plt.plot(x_axis, tx, color='blue', label='Temperatur', linestyle='', marker='.')

    if choice == "1":
        single_mean()
    elif choice == "2":
        mean_sections(3)
    elif choice == "3":
        n = int(input("Anzahl der Abschnitte: "))
        mean_sections(n)
    elif choice == "4":
        moving_average(1,True)

    plt.legend()
    plt.show()
