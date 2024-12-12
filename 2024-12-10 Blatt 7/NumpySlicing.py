import numpy as np
np.set_printoptions(threshold=10) # damit nicht alle Elemente angezeigt werden

start = 42
stop = 420
array = np.arange(start, stop+1)
print(f"Array: \n{array}")

arr_sum = np.sum(array)
arr_prod = np.prod(array)
print(f"Summe: {arr_sum}")
print(f"Produkt: {arr_prod}\n")
# Produkt = 0, da 64bit überschritten werden [formel: (start-1)! / (stop-1)! → fakultät 420 zu groß]
# arr_prod = np.prod(array, dtype=np.object_)

arr_slice = array[:18]
print(f"Erste 18 Elemente: \n{arr_slice}")
arr_sum = np.sum(arr_slice)
print(f"Summe erste 18 Elemente: {arr_sum}\n")

arr_slice = array[::2]
print(f"Jedes 2. Element: {arr_slice}")
arr_sum = np.sum(arr_slice)
print(f"Summe aller 2. Elemente: {arr_sum}\n")

arr_slice = array[-18:]
print(f"Letzte 18 Elemente: \n{arr_slice}")
arr_sum = np.sum(arr_slice)
print(f"Summe letzte 18 Elemente: {arr_sum}\n")

mask = array % 2 == 1
arr_slice = array[mask]
print(f"Alle ungeraden Zahlen: {arr_slice}\n")

array = np.random.randint(0, 11, (20, 30))
print(f"Array: \n{array}")

mask = array[:, :2] >= 2
arr_sum = np.sum(mask)
print(f"Anzahl  Zahlen >= 2 in ersten beiden Spalten: {arr_sum}")

array[[0, -1], :] = -1   # Oben und unten
array[:, [0, -1]] = -1   # Links und rechts
print(f"Array mit Rändern: \n{array}")

random_row = np.random.randint(0, 20)
array[random_row, -1] = -2
print(f"Array mit -2 in letzter Spalte: \n{array}")