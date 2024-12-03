# 1)
print("Aufgabe 1:")
ROMAN_NUMBERS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
get_roman_number = lambda n: ROMAN_NUMBERS.get(n, None)

def sum_roman(x: int, y: int) -> str:
    if 0 < x < 11 and 0 < y < 11 and (x + y) <= 10:
        return get_roman_number(x + y)
    return "Fehler"

print(f"sum_roman(2, 4) = {sum_roman(2, 4)}")
print(f"sum_roman(12, 3) = {sum_roman(12, 3)}")

# 2)
print("\nAufgabe 2:")
def trib(n: int) -> int:
    if n in [1, 2]:
        return 1
    if n == 3:
        return 2
    return trib(n - 1) + trib(n - 2) + trib(n - 3)

print(f"trib(2) = {trib(2)}")
print(f"trib(12) = {trib(12)}")

# 3)
print("\nAufgabe 3:")
def search_max(some_list: list) -> int:
    if len(some_list) == 1:
        return some_list[0]
    other_max = search_max(some_list[1:])
    return some_list[0] if some_list[0] > other_max else other_max

print(f"search_max([91,812,3,34,6345,23,5,71]) = {search_max([91,812,3,34,6345,23,5,71])}")
