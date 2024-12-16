import numpy as np
from jguvc_eip import basic_io as bio
from matplotlib import pyplot as plt

# Daten
#data = np.loadtxt("muenchen_flughafen.txt")
data = np.loadtxt("Klimadaten FRA.txt", delimiter=";")
tx = data[:, 6]  # Temperatur TX
rr = data[:, -2]   # Niederschlagsmenge RR
x_axis = np.arange(data.shape[0])
y_height = 300
bins = np.linspace(np.min(rr), np.max(rr), 6)

def display_bio1():
    bio.start()

    # Regeniagramm
    for x in x_axis:
        rsk_from_x = rr[x]
        bio.draw_circle(int(x) + 5, int(y_height - rsk_from_x), 1, border_color=(0, 0, 255))

    # Temperaturdiagramm
    for i in range(len(x_axis) - 1):
        bio.draw_line(
            int(x_axis[i]) + 5, int(y_height - tx[i]),
            int(x_axis[i+1]) + 5, int(y_height - tx[i+1]),
            color=(255,0,0)
        )

    # Achsen
    bio.draw_line(5, y_height, 640, y_height)
    bio.draw_line(5, 0, 5, y_height)
    bio.draw_text(550, y_height + 10, "Tage (x)")
    bio.draw_text(10, 5, "Werte (y)")

    # Ticks
    for x_tick in range(5, 640, 5):
        bio.draw_line(x_tick, y_height, x_tick, y_height + 5)
    for y_tick in range(0, y_height, 5):
        bio.draw_line(0, y_height - y_tick, 5, y_height - y_tick)

    bio.wait_close()

def display_plt1():
    plt.figure(figsize=(10, 5))

    # Diagramme
    plt.plot(x_axis, rr, color='blue', label='Niederschlag', linestyle='', marker='.')
    plt.plot(x_axis, tx, color='red', label='Temperatur', linestyle='-', marker='')

    # Labels
    plt.xlabel("Tage", fontsize=12)
    plt.ylabel("Werte", fontsize=12)
    plt.title("Temperatur und Niederschlag Frankfurt", fontsize=14)
    plt.legend()

    plt.show()

def display_bio2():
    bio.start()

    # Histogramm
    counts, _ = np.histogram(rr, bins=bins)
    highest = max(counts)
    for i, (count, left_edge) in enumerate(zip(counts, bins[:-1])):
        bar_height = round(count * (y_height / highest))
        bar_x = 40 + i*80
        bio.draw_rectangle(bar_x, y_height - bar_height, 80, bar_height, fill_color=(0, 0, 255))
        bio.draw_line(bar_x, y_height, bar_x, y_height + 5)
        bio.draw_text(bar_x - 5, y_height + 10, f"{left_edge:.1f}")

    # Ticks y
    for y_tick in range(0, y_height, 20):
        bio.draw_line(40, y_height - y_tick, 35, y_height - y_tick)
        bio.draw_text(5, y_height - y_tick - 10, str(y_tick * highest // y_height))

    # Achsen
    bio.draw_line(40, y_height, 640, y_height)
    bio.draw_line(40, 0, 40, y_height)
    bio.draw_text(475, y_height + 10, "Menge (x)")
    bio.draw_text(50, 10, "Häufigkeit (y)")

    bio.wait_close()

def display_plt2():
    plt.figure(figsize=(10, 5))

    # Histogramm
    plt.hist(rr, bins=bins, color='blue', edgecolor='black', alpha=0.7)

    # Labels
    plt.xlabel("menge", fontsize=12)
    plt.ylabel("Häufigkeit", fontsize=12)
    plt.title("Histogramm Niederschlagswerte Frankfurt", fontsize=14)

    plt.show()

if __name__ == "__main__":
    if __name__ == "__main__":
        print("Aufgabe wählen:")
        print("1: Aufgabe 1 - Basic-IO")
        print("2: Aufgabe 1 - Matplotlib")
        print("3: Aufgabe 2 - Basic-IO")
        print("4: Aufgabe 2 - Matplotlib")
        choice = input("(1-4): ")
        #choice = "3"
        match = {1: display_bio1, 2: display_plt1, 3: display_bio2, 4: display_plt2}
        if choice in "1234":
            match[int(choice)]()