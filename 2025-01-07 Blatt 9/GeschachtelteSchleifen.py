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
# Wir iterieren über alle zahlen bis 10^10, wandeln sie in einen String um, ergänzen vorne Nullen und prüfen den Pin.

def crack_pin(pin_length=10):
    total_pins = 10 ** pin_length
    for i in range(total_pins):
        pin_str = str(i)
        pin = "0" * (pin_length - len(pin_str)) + pin_str
        if check_pin(pin):
            return pin

# Aufgabe 5
# Hier werden drei verschachtelte Schleifen benötigt:
# Für jede Liste iterieren wir über alle Elemente und legen sie als Kombination an.

def combine_clothing(shoes, shirts, pants):
    return [
        (shoe, shirt, pant)
        for shoe in shoes
        for shirt in shirts
        for pant in pants
    ]

# Aufgabe 6
mat1 = [[1,2,5],[2,7,1],[1,7,7]]
mat2 = [[5,1,8],[2,2,2],[1,9,9]]
prod = mat_prod(mat1, mat2)

print("Aufgabe 2: Matrixprodukt")
print(f"{mat1[0]}   {mat2[0]}   {prod[0]}")
print(f"{mat1[1]} x {mat2[1]} = {prod[1]}")
print(f"{mat1[2]}   {mat2[2]}   {prod[2]}\n")

PIN = "0001234321"
def check_pin(pin: str):
    """Checks if a pin is correct. Returns a bool.
    Takes a pin given as a string as input.
    """
    assert isinstance(pin, str), "Pin needs to be a string"
    assert len(pin) == 10, "Pin needs exactly 10 digits"
    return pin == PIN

print("Aufgabe 4b: Pin überprüfen")
print(f"Pin is: {crack_pin()}\n")

shoes=["vans", "boots", "chucks", "heels"]
shirts=["dotted red shirt", "elegant black shirt", "trashy pink shirt"]
pants=["jeans", "jogging pants", "yoga pants", "shorts"]
combinations = combine_clothing(shoes, shirts, pants)

print("Aufgabe 5: Kleidungskombinationen")
print(f"Anzahl: {len(combinations)}")
print("\n".join(", ".join(combo) for combo in combinations))