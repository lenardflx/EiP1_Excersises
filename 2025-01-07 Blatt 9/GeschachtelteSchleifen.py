# Aufgabe 1
# Hier wird eine Schleife ohne Verschachtelung benötigt:
# Wir iterieren  über alle Elemente von arr und prüfen, ob eine Zahl kleinergleich num ist.
# Wenn ja geben wir False zurück, sonst True.

# Aufgabe 2
# Hier brauchen wir drei verschachtelte Schleifen:
# Einmal über Zeilen mat1, einmal über Spalten mat2 und einmal über die Elemente der Zeilen/Spalten, für das Produkt.

def mat_prod(mat1, mat2):
    result = []
    n = len(mat1)
    for i in range(n):
        row = []
        for j in range(n):
            res = 0
            for k in range(n):
                res += mat1[i][k] * mat2[k][j]
            row.append(res)
        result.append(row)
    return result

# Aufgabe 3
# Hier wird eine Schleife ohne Verschachtelung benötigt:
# Wir iterieren über die Länge der Matrix und mat[i][i] gibt uns die Diagonale an.
# Falls beide Diagonalen gemeint sind, könnnen wir -i für die zweite Diagonale nutzen.

# Aufgabe 4a
# Hier wird eine schleife ohne Verschachtelung benötigt:
# Wir iterieren über die Liste der Pins und prüfen, ob der Pin in der Liste enthalten ist.

# Aufgabe 4b
# Hier wird eine Schleife ohne Verschachtelung benötigt:
# Wir iterieren über alle Kombinationen von 0000000000 bis 9999999999 und prüfen, ob dies der Pin ist.

# Aufgabe 5
# Hier werden drei verschachtelte Schleifen benötigt:
# Für jede Liste iterieren wir über alle Elemente und legen sie als Kombination an.

def combine_clothing(shoes, shirts, pants):
    combinations = []
    for shoe in shoes:
        for shirt in shirts:
            for pant in pants:
                combinations.append((shoe, shirt, pant))
    return combinations

# Aufgabe 6
mat1 = [[1,2,5],[2,7,1],[1,7,7]]
mat2 = [[5,1,8],[2,2,2],[1,9,9]]
prod = mat_prod(mat1, mat2)

print("Aufgabe 2: Matrixprodukt")
print(f"{mat1[0]}   {mat2[0]}   {prod[0]}")
print(f"{mat1[1]} x {mat2[1]} = {prod[1]}")
print(f"{mat1[2]}   {mat2[2]}   {prod[2]}\n")

shoes=["vans", "boots", "chucks", "heels"]
shirts=["dotted red shirt", "elegant black shirt", "trashy pink shirt"]
pants=["jeans", "jogging pants", "yoga pants", "shorts"]
combinations = combine_clothing(shoes, shirts, pants)

print("Aufgabe 5: Kleidungskombinationen")
print(f"Anzahl: {len(combinations)}")
for combo in combinations:
    print(", ".join(combo))