import numpy as np
from jguvc_eip import basic_io as bio
from matplotlib import pyplot as plt

# Daten
data = np.loadtxt("Klimadaten FRA.txt", delimiter=";")
tx = data[:, 6]  # Temperatur TX
rr = data[:, -2]   # Niederschlagsmenge RR
x_axis = np.arange(data.shape[0])
y_height = 150

# Histogrammdaten
rr_min = np.min(rr)
rr_max = np.max(rr)
bins = np.linspace(rr_min, rr_max, 6)
counts, bin_edges = np.histogram(rr, bins=bins)

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
            int(x_axis[i + 1]) + 5, int(y_height - tx[i + 1]),
            color=(255, 0, 0)
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
        bio.draw_line(0, y_height - y_tick, +5, y_height - y_tick)

    bio.wait_close()

def display_plt1():
    plt.figure(figsize=(10, 5))

    # Diagramme
    plt.scatter(x_axis, rr, color='blue', label='Niederschlag', marker='o')
    plt.plot(x_axis, tx, color='red', label='Temperatur', linestyle='-', marker='')

    # Labels
    plt.xlabel("Tage", fontsize=12)
    plt.ylabel("Werte", fontsize=12)
    plt.title("Temperatur und Niederschlag", fontsize=14)
    plt.legend()

    plt.show()

def display_bio2():
    bio.start()

    # Histogramm
    bin_width = 75
    max_count = max(counts)
    for i, (count, left_edge) in enumerate(zip(counts, bin_edges[:-1])):
        bar_height = int(count * (y_height / max_count))
        bar_x = 40 + i * bin_width
        bio.draw_rectangle(bar_x, y_height - bar_height, bin_width - 5, bar_height, fill_color=(0, 0, 255))
        bio.draw_line(bar_x, y_height, bar_x, y_height + 5)
        bio.draw_text(bar_x - 5, y_height + 10, f"{left_edge:.1f}")

    # Ticks y
    for y_tick in range(0, y_height, 20):
        bio.draw_line(40, y_height - y_tick, 35, y_height - y_tick)
        bio.draw_text(5, y_height - y_tick - 5, str(y_tick * max_count // y_height))

    # Achsen
    bio.draw_line(40, y_height, 640, y_height)
    bio.draw_line(40, 0, 40, y_height)
    bio.draw_text(475, y_height + 20, "Wertebereich (x)")
    bio.draw_text(30, 10, "Anzahl (y)")

    bio.wait_close()

def display_plt2():
    plt.figure(figsize=(10, 5))

    # Histogramm
    plt.hist(rr, bins=bins, color='blue', edgecolor='black', alpha=0.7)

    # Labels
    plt.xlabel("Wertebereich", fontsize=12)
    plt.ylabel("Anzahl", fontsize=12)
    plt.title("Histogramm der Niederschlagswerte", fontsize=14)

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