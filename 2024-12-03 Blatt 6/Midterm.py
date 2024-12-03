# 1)
print("Aufgabe 1:")
ROMAN_NUMBERS = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII", 9: "IX", 10: "X"}
get_roman_number = lambda n: ROMAN_NUMBERS.get(n, None)
sum_roman = lambda x, y: get_roman_number(x + y) if 0 < x < 11 and 0 < y < 11 and (x + y) <= 10 else "Fehler"
print(f"sum_roman(2, 4) = {get_roman_number(2)} + {get_roman_number(4)} = {sum_roman(2, 4)}")
print(f"sum_roman(12, 3) = {get_roman_number(12)} + {get_roman_number(3)} = {sum_roman(12, 3)}")

# 2)
print("\nAufgabe 2:")
trib = lambda n: 1 if n in [1,2] else 2 if n == 3 else trib(n-1) + trib(n-2) + trib(n-3)
print(f"trib(2) = {trib(2)}")
print(f"trib(12) = {trib(12)}")

# 3)
print("\nAufgabe 3:")
search_max = lambda lst: lst[0] if len(lst) == 1 or lst[0] > (m := search_max(lst[1:])) else m
print(f"search_max([91,812,3,34,6345,23,5,71]) = {search_max([91,812,3,34,6345,23,5,71])}")
